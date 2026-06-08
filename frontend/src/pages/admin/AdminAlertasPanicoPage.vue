<template>
  <div class="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(239,68,68,0.18),_transparent_28%),linear-gradient(180deg,#fff7ed_0%,#ffffff_54%,#fff1f2_100%)] pt-16 text-slate-900">
    <header class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
      <div class="flex flex-wrap items-center justify-between gap-4 rounded-[2rem] border border-rose-100 bg-white p-6 shadow-lg">
        <div>
          <p class="text-xs font-bold uppercase tracking-[0.35em] text-rose-600">Administración</p>
          <h1 class="mt-2 text-3xl font-black">Alertas de pánico</h1>
          <p class="mt-2 text-sm text-slate-600">Revisa alertas activas, cambia su estado y da seguimiento a cada envío anónimo.</p>
        </div>
        <router-link to="/admin/sector-publico" class="rounded-full bg-slate-950 px-4 py-2 text-sm font-bold text-white">Volver</router-link>
      </div>
    </header>

    <main class="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8">
      <div class="grid gap-4 md:grid-cols-3">
        <article class="rounded-[1.75rem] border border-rose-100 bg-white p-5 shadow-sm"><p class="text-xs font-bold uppercase tracking-[0.25em] text-rose-500">Totales</p><h2 class="mt-2 text-4xl font-black">{{ alerts.length }}</h2></article>
        <article class="rounded-[1.75rem] border border-orange-100 bg-white p-5 shadow-sm"><p class="text-xs font-bold uppercase tracking-[0.25em] text-orange-500">Abiertas</p><h2 class="mt-2 text-4xl font-black">{{ countByStatus('open') }}</h2></article>
        <article class="rounded-[1.75rem] border border-emerald-100 bg-white p-5 shadow-sm"><p class="text-xs font-bold uppercase tracking-[0.25em] text-emerald-500">Cerradas</p><h2 class="mt-2 text-4xl font-black">{{ countByStatus('closed') }}</h2></article>
      </div>

      <section class="mt-8 grid gap-4">
        <article v-for="alert in alerts" :key="alert.id" class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-lg">
          <div class="flex flex-wrap items-start justify-between gap-4">
            <div>
              <div class="flex items-center gap-2"><span class="rounded-full bg-rose-50 px-3 py-1 text-xs font-bold text-rose-700">{{ alert.status }}</span><h3 class="font-black text-slate-900">{{ alert.symptom || 'Sin síntoma' }}</h3></div>
              <p class="mt-2 text-sm text-slate-600">{{ formatDate(alert.created_at) }}</p>
              <p class="mt-1 text-xs text-slate-500">{{ toLabel(alert.latitude, alert.longitude) }}</p>
            </div>
            <div class="flex flex-wrap gap-2">
              <button v-for="status in statuses" :key="status.value" type="button" class="rounded-full px-3 py-2 text-xs font-bold" :class="alert.status === status.value ? 'bg-slate-950 text-white' : 'bg-slate-100 text-slate-600'" @click="updateStatus(alert.id, status.value)">{{ status.label }}</button>
            </div>
          </div>
        </article>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { apiUrl } from '@/utils/api';
import { type PanicAlert, toNumber } from '../client/public-sector';

const alerts = ref<PanicAlert[]>([]);
const statuses = [
  { value: 'open', label: 'Abierta' },
  { value: 'acknowledged', label: 'Reconocida' },
  { value: 'closed', label: 'Cerrada' },
] as const;

async function loadAlerts(): Promise<void> {
  const response = await fetch(apiUrl('/panic-alerts/'));
  alerts.value = response.ok ? ((await response.json()) as PanicAlert[]) : [];
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
});
</script>
