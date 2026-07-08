<template>
  <div class="space-y-6">
    <main class="grid gap-6">
      <div class="flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-slate-200 bg-white px-4 py-3 shadow-sm">
        <p class="text-sm text-slate-500">Ultima sincronizacion: {{ lastSyncLabel }}</p>
        <button type="button" class="rounded-full bg-slate-950 px-4 py-2 text-sm font-bold text-white" @click="loadConsultations">
          Actualizar ahora
        </button>
      </div>

      <section class="grid gap-4">
        <article v-for="consultation in consultations" :key="consultation.id" class="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
          <div class="flex flex-wrap items-start justify-between gap-4">
            <div>
              <div class="flex items-center gap-2">
                <span class="rounded-full bg-violet-50 px-3 py-1 text-xs font-bold text-violet-700">{{ consultation.status }}</span>
                <h3 class="font-black text-slate-900">{{ topicLabel(consultation.topic) }}</h3>
              </div>
              <p class="mt-2 text-sm text-slate-600">{{ consultation.question || 'Consulta sin texto' }}</p>
            </div>
            <p class="text-xs text-slate-500">{{ (consultation.session_token || '').slice(0, 8) || 'sin-token' }}…</p>
          </div>

          <div class="mt-4 grid gap-3 md:grid-cols-[1fr_220px]">
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Respuesta</span>
              <textarea v-model="replyDraft[consultation.id]" rows="4" class="input-base" placeholder="Escribe una respuesta segura y breve..."></textarea>
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Moderador</span>
              <input v-model="moderatorDraft[consultation.id]" type="text" class="input-base" placeholder="Nombre del moderador" />
              <button type="button" class="mt-3 w-full rounded-full bg-gradient-to-r from-[#7C3AED] to-[#F97316] px-4 py-3 text-sm font-black text-white" @click="saveReply(consultation.id)">Guardar respuesta</button>
              <button type="button" class="mt-2 w-full rounded-full bg-slate-100 px-4 py-3 text-sm font-bold text-slate-600" @click="closeConsultation(consultation.id)">Cerrar</button>
            </label>
          </div>
        </article>

        <div v-if="consultations.length === 0" class="rounded-[2rem] border border-dashed border-violet-200 bg-white px-6 py-12 text-center shadow-sm">
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-violet-600">Sin consultas pendientes</p>
          <h3 class="mt-3 text-2xl font-black text-slate-900">Todavia no hay consultas adolescentes</h3>
          <p class="mx-auto mt-3 max-w-2xl text-sm leading-6 text-slate-600">
            Las consultas anonimas creadas desde la vista publica apareceran aqui para responderlas o cerrarlas.
          </p>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, reactive, ref } from 'vue';
import { apiUrl } from '@/utils/api';
import { toApiList, type AdolescentConsultation } from '../client/public-sector';

const consultations = ref<AdolescentConsultation[]>([]);
const replyDraft = reactive<Record<number, string>>({});
const moderatorDraft = reactive<Record<number, string>>({});
const lastSyncAt = ref<Date | null>(null);
let refreshIntervalId: number | null = null;

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

async function loadConsultations(): Promise<void> {
  const response = await fetch(apiUrl('/adolescent-consultations/'), {
    cache: 'no-store',
  });

  if (!response.ok) {
    consultations.value = [];
    lastSyncAt.value = new Date();
    return;
  }

  const payload = (await response.json()) as unknown;
  consultations.value = toApiList<AdolescentConsultation>(payload);

  for (const consultation of consultations.value) {
    if (!(consultation.id in replyDraft)) {
      replyDraft[consultation.id] = consultation.answer || '';
    }
    if (!(consultation.id in moderatorDraft)) {
      moderatorDraft[consultation.id] = consultation.responder_name || '';
    }
  }

  lastSyncAt.value = new Date();
}

function topicLabel(topic: AdolescentConsultation['topic']): string {
  if (topic === 'contracepcion') return 'Anticoncepción';
  if (topic === 'prevencion') return 'Prevención';
  if (topic === 'ciclo') return 'Ciclo menstrual';
  return 'Otra consulta';
}

async function saveReply(consultationId: number): Promise<void> {
  await fetch(apiUrl(`/adolescent-consultations/${consultationId}/`), {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      answer: replyDraft[consultationId] ?? '',
      responder_name: moderatorDraft[consultationId] ?? '',
      status: replyDraft[consultationId] ? 'answered' : 'pending',
    }),
  });
  await loadConsultations();
}

async function closeConsultation(consultationId: number): Promise<void> {
  await fetch(apiUrl(`/adolescent-consultations/${consultationId}/`), {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status: 'closed' }),
  });
  await loadConsultations();
}

onMounted(async () => {
  document.title = 'Admin consultas | Mesa de Maternidad';
  await loadConsultations();
  refreshIntervalId = window.setInterval(() => {
    void loadConsultations();
  }, 8000);
});

onBeforeUnmount(() => {
  if (refreshIntervalId !== null) {
    window.clearInterval(refreshIntervalId);
  }
});
</script>

<style scoped>
.input-base {
  width: 100%;
  border-radius: 1rem;
  border: 1px solid rgb(226 232 240);
  background: rgb(248 250 252);
  color: rgb(15 23 42);
  padding: 0.75rem 1rem;
  outline: none;
}

.input-base::placeholder {
  color: rgb(148 163 184);
}

.input-base:focus {
  border-color: rgb(124 58 237);
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1);
}
</style>
