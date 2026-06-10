<template>
  <div class="space-y-6">
    <main class="grid gap-6">
      <div class="grid gap-4 md:grid-cols-3">
        <article class="rounded-3xl border border-rose-100 bg-white p-5 shadow-sm">
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-rose-500">Totales</p>
          <h2 class="mt-2 text-4xl font-black">{{ alerts.length }}</h2>
        </article>
        <article class="rounded-3xl border border-orange-100 bg-white p-5 shadow-sm">
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-orange-500">Abiertas</p>
          <h2 class="mt-2 text-4xl font-black">{{ countByStatus('open') }}</h2>
        </article>
        <article class="rounded-3xl border border-emerald-100 bg-white p-5 shadow-sm">
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-emerald-500">Cerradas</p>
          <h2 class="mt-2 text-4xl font-black">{{ countByStatus('closed') }}</h2>
        </article>
      </div>

      <div class="flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-slate-200 bg-white px-4 py-3 shadow-sm">
        <p class="text-sm text-slate-500">Ultima sincronizacion: {{ lastSyncLabel }}</p>
        <button type="button" class="rounded-full bg-slate-950 px-4 py-2 text-sm font-bold text-white" @click="loadAlerts">
          Actualizar ahora
        </button>
      </div>

      <section class="grid gap-4">
        <article v-for="alert in alerts" :key="alert.id" class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-lg">
          <div class="flex flex-wrap items-start justify-between gap-4">
            <div>
              <div class="flex items-center gap-2">
                <span class="rounded-full bg-rose-50 px-3 py-1 text-xs font-bold text-rose-700">{{ alert.status }}</span>
                <h3 class="font-black text-slate-900">{{ alert.symptom || 'Sin síntoma' }}</h3>
              </div>
              <p class="mt-2 text-sm text-slate-600">{{ formatDate(alert.created_at) }}</p>
              <p class="mt-1 text-xs text-slate-500">{{ toLabel(alert.latitude, alert.longitude) }}</p>
            </div>
            <div class="flex flex-wrap gap-2">
              <button v-for="status in statuses" :key="status.value" type="button" class="rounded-full px-3 py-2 text-xs font-bold" :class="alert.status === status.value ? 'bg-slate-950 text-white' : 'bg-slate-100 text-slate-600'" @click="updateStatus(alert.id, status.value)">{{ status.label }}</button>
            </div>
          </div>
        </article>

        <div v-if="alerts.length === 0" class="rounded-[2rem] border border-dashed border-rose-200 bg-white px-6 py-12 text-center shadow-sm">
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-rose-500">Sin alertas registradas</p>
          <h3 class="mt-3 text-2xl font-black text-slate-900">Todavia no llegaron alertas de panico</h3>
          <p class="mx-auto mt-3 max-w-2xl text-sm leading-6 text-slate-600">
            Cuando una usuaria use el boton de panico desde la vista publica, las alertas apareceran aqui con su estado y ubicacion.
          </p>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue';
import { apiUrl } from '@/utils/api';
import { toApiList, type PanicAlert, toNumber } from '../client/public-sector';

const alerts = ref<PanicAlert[]>([]);
const lastSyncAt = ref<Date | null>(null);
let refreshIntervalId: number | null = null;
const statuses = [
  { value: 'open', label: 'Abierta' },
  { value: 'acknowledged', label: 'Reconocida' },
  { value: 'closed', label: 'Cerrada' },
] as const;

const lastSyncLabel = computed(() => {
  if (!lastSyncAt.value) {
    return 'sin sincronizar';
  }

  return lastSyncAt.value.toLocaleTimeString('es-BO', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  });
});

async function loadAlerts(): Promise<void> {
  const response = await fetch(apiUrl('/panic-alerts/'), {
    cache: 'no-store',
  });

  if (!response.ok) {
    alerts.value = [];
    lastSyncAt.value = new Date();
    return;
  }

  const payload = (await response.json()) as unknown;
  alerts.value = toApiList<PanicAlert>(payload);
  lastSyncAt.value = new Date();
}

async function updateStatus(alertId: number, status: 'open' | 'acknowledged' | 'closed'): Promise<void> {
  await fetch(apiUrl(`/panic-alerts/${alertId}/`), {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status }),
  });
  await loadAlerts();
}

function countByStatus(status: 'open' | 'acknowledged' | 'closed'): number {
  return alerts.value.filter((alert) => alert.status === status).length;
}

function formatDate(value: string): string {
  return new Date(value).toLocaleString('es-BO', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' });
}

function toLabel(latitude: number | string, longitude: number | string): string {
  return `${toNumber(latitude).toFixed(4)}, ${toNumber(longitude).toFixed(4)}`;
}

onMounted(async () => {
  document.title = 'Admin alertas | Mesa de Maternidad';
  await loadAlerts();
  refreshIntervalId = window.setInterval(() => {
    void loadAlerts();
  }, 8000);
});

onBeforeUnmount(() => {
  if (refreshIntervalId !== null) {
    window.clearInterval(refreshIntervalId);
  }
});
</script>
