<template>
  <div class="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(15,118,110,0.16),_transparent_28%),linear-gradient(180deg,#0f172a_0%,#ffffff_54%,#fff7ed_100%)] pt-16 text-slate-900">
    <header class="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
      <div class="rounded-[2rem] border border-white/20 bg-slate-950 p-8 text-white shadow-[0_30px_90px_-40px_rgba(15,23,42,0.95)]">
        <p class="text-xs font-bold uppercase tracking-[0.35em] text-teal-200">Admin público</p>
        <h1 class="mt-3 text-3xl font-black md:text-5xl">Panel de operación del sector público</h1>
        <p class="mt-4 max-w-3xl text-sm leading-6 text-slate-300 md:text-base">
          Desde aquí se crean los centros de salud, se monitorean alertas de pánico y se responden consultas anónimas de adolescentes.
        </p>
      </div>
    </header>

    <main class="mx-auto grid max-w-7xl gap-8 px-4 pb-12 sm:px-6 lg:px-8 xl:grid-cols-[1fr_1fr]">
      <section class="space-y-8">
        <div class="rounded-[2rem] border border-teal-100 bg-white p-6 shadow-lg">
          <div class="flex items-center justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-teal-600">Centros de salud</p>
              <h2 class="mt-2 text-2xl font-black text-slate-900">Crear o editar centros</h2>
            </div>
            <button class="rounded-full bg-teal-50 px-4 py-2 text-sm font-semibold text-teal-700 transition hover:bg-teal-100" type="button" @click="resetCenterForm">
              Nuevo
            </button>
          </div>

          <form class="mt-6 grid gap-4 md:grid-cols-2" @submit.prevent="saveCenter">
            <label class="space-y-2 md:col-span-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Nombre</span>
              <input v-model="centerForm.nombre" class="input-base" type="text" required />
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Nivel</span>
              <select v-model="centerForm.nivel" class="input-base" required>
                <option value="I">Nivel I</option>
                <option value="II">Nivel II</option>
                <option value="III">Nivel III</option>
              </select>
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Ciudad</span>
              <input v-model="centerForm.ciudad" class="input-base" type="text" required />
            </label>
            <label class="space-y-2 md:col-span-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Dirección</span>
              <input v-model="centerForm.direccion" class="input-base" type="text" required />
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Teléfono</span>
              <input v-model="centerForm.telefono" class="input-base" type="text" required />
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Teléfono emergencia</span>
              <input v-model="centerForm.telefono_emergencia" class="input-base" type="text" />
            </label>
            <label class="space-y-2 md:col-span-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Horario</span>
              <input v-model="centerForm.horario" class="input-base" type="text" />
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Latitud</span>
              <input v-model="centerForm.latitude" class="input-base" type="number" step="0.000001" required />
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Longitud</span>
              <input v-model="centerForm.longitude" class="input-base" type="number" step="0.000001" required />
            </label>
            <label class="flex items-center gap-3 md:col-span-2">
              <input v-model="centerForm.ambulancia_disponible" type="checkbox" class="h-5 w-5 rounded border-slate-300 text-teal-600" />
              <span class="text-sm font-semibold text-slate-700">Ambulancia disponible</span>
            </label>
            <div class="md:col-span-2 flex flex-wrap gap-3">
              <button type="submit" class="rounded-full bg-gradient-to-r from-[#0F766E] to-[#14B8A6] px-5 py-3 text-sm font-black text-white shadow-lg shadow-teal-200 transition hover:-translate-y-0.5">
                {{ editingCenterId ? 'Actualizar centro' : 'Guardar centro' }}
              </button>
              <button type="button" class="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 transition hover:border-teal-200 hover:text-teal-700" @click="resetCenterForm">
                Limpiar
              </button>
            </div>
          </form>
        </div>

        <div class="rounded-[2rem] border border-rose-100 bg-white p-6 shadow-lg">
          <div class="flex items-center justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-rose-600">Alertas de pánico</p>
              <h2 class="mt-2 text-2xl font-black text-slate-900">Monitoreo y estados</h2>
            </div>
            <span class="rounded-full bg-rose-50 px-3 py-1 text-xs font-bold text-rose-600">{{ alerts.length }} alertas</span>
          </div>

          <div class="mt-5 space-y-3">
            <article v-for="alert in alerts" :key="alert.id" class="rounded-[1.5rem] border border-slate-100 bg-slate-50 p-4">
              <div class="flex flex-wrap items-start justify-between gap-3">
                <div>
                  <p class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">{{ alert.session_token.slice(0, 8) }}…</p>
                  <h3 class="mt-1 font-black text-slate-900">{{ alert.symptom || 'Sin síntoma' }}</h3>
                  <p class="mt-1 text-sm text-slate-600">{{ toLabel(alert.latitude, alert.longitude) }}</p>
                </div>
                <span class="rounded-full px-3 py-1 text-xs font-bold" :class="statusClass(alert.status)">{{ alert.status }}</span>
              </div>
              <div class="mt-4 flex flex-wrap gap-2">
                <button v-for="status in alertStatuses" :key="status.value" type="button" class="rounded-full px-3 py-2 text-xs font-bold transition" :class="status.value === alert.status ? 'bg-slate-950 text-white' : 'bg-white text-slate-600 hover:bg-rose-50'" @click="updateAlertStatus(alert.id, status.value)">
                  {{ status.label }}
                </button>
              </div>
            </article>
          </div>
        </div>
      </section>

      <section class="space-y-8">
        <div class="rounded-[2rem] border border-violet-100 bg-white p-6 shadow-lg">
          <div class="flex items-center justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-violet-600">Consultas anónimas</p>
              <h2 class="mt-2 text-2xl font-black text-slate-900">Responder al historial</h2>
            </div>
            <span class="rounded-full bg-violet-50 px-3 py-1 text-xs font-bold text-violet-700">{{ consultations.length }} casos</span>
          </div>

          <div class="mt-5 space-y-4">
            <article v-for="consultation in consultations" :key="consultation.id" class="rounded-[1.5rem] border border-slate-100 bg-slate-50 p-4">
              <div class="flex flex-wrap items-start justify-between gap-3">
                <div>
                  <p class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">{{ consultation.session_token.slice(0, 8) }}…</p>
                  <h3 class="mt-1 font-black text-slate-900">{{ topicLabel(consultation.topic) }}</h3>
                  <p class="mt-2 text-sm text-slate-600">{{ consultation.question }}</p>
                </div>
                <span class="rounded-full px-3 py-1 text-xs font-bold" :class="consultation.status === 'answered' ? 'bg-emerald-100 text-emerald-700' : 'bg-violet-100 text-violet-700'">{{ consultation.status }}</span>
              </div>

              <div class="mt-4 space-y-3 rounded-2xl bg-white p-4 shadow-sm">
                <label class="space-y-2">
                  <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Respuesta</span>
                  <textarea v-model="replyDraft[consultation.id]" rows="4" class="input-base resize-none" placeholder="Escribe una respuesta segura y breve..."></textarea>
                </label>
                <label class="space-y-2">
                  <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Moderador</span>
                  <input v-model="responderDraft[consultation.id]" type="text" class="input-base" placeholder="Nombre del moderador" />
                </label>
                <div class="flex flex-wrap gap-2">
                  <button type="button" class="rounded-full bg-gradient-to-r from-[#7C3AED] to-[#F97316] px-4 py-2 text-xs font-black text-white" @click="saveReply(consultation.id, consultation.session_token)">
                    Guardar respuesta
                  </button>
                  <button type="button" class="rounded-full bg-slate-100 px-4 py-2 text-xs font-bold text-slate-600" @click="markConsultationClosed(consultation.id)">
                    Cerrar
                  </button>
                </div>
              </div>
            </article>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
import { apiUrl } from '@/utils/api';
import {
  type AdolescentConsultation,
  type HealthCenter,
  type PanicAlert,
  type PublicSectorLevel,
  toNumber,
} from '../client/public-sector';

type CenterForm = {
  nombre: string;
  nivel: PublicSectorLevel;
  direccion: string;
  ciudad: string;
  telefono: string;
  telefono_emergencia: string;
  horario: string;
  ambulancia_disponible: boolean;
  latitude: string;
  longitude: string;
};

const centers = ref<HealthCenter[]>([]);
const alerts = ref<PanicAlert[]>([]);
const consultations = ref<AdolescentConsultation[]>([]);
const editingCenterId = ref<number | null>(null);
const replyDraft = reactive<Record<number, string>>({});
const responderDraft = reactive<Record<number, string>>({});

const centerForm = reactive<CenterForm>({
  nombre: '',
  nivel: 'I',
  direccion: '',
  ciudad: '',
  telefono: '',
  telefono_emergencia: '',
  horario: '',
  ambulancia_disponible: false,
  latitude: '-16.500000',
  longitude: '-68.150000',
});

const alertStatuses = [
  { value: 'open', label: 'Abierta' },
  { value: 'acknowledged', label: 'Reconocida' },
  { value: 'closed', label: 'Cerrada' },
] as const;

function resetCenterForm(): void {
  editingCenterId.value = null;
  centerForm.nombre = '';
  centerForm.nivel = 'I';
  centerForm.direccion = '';
  centerForm.ciudad = '';
  centerForm.telefono = '';
  centerForm.telefono_emergencia = '';
  centerForm.horario = '';
  centerForm.ambulancia_disponible = false;
  centerForm.latitude = '-16.500000';
  centerForm.longitude = '-68.150000';
}

function populateCenterForm(center: HealthCenter): void {
  editingCenterId.value = center.id;
  centerForm.nombre = center.nombre;
  centerForm.nivel = center.nivel;
  centerForm.direccion = center.direccion;
  centerForm.ciudad = center.ciudad;
  centerForm.telefono = center.telefono;
  centerForm.telefono_emergencia = center.telefono_emergencia;
  centerForm.horario = center.horario;
  centerForm.ambulancia_disponible = center.ambulancia_disponible;
  centerForm.latitude = String(center.latitude);
  centerForm.longitude = String(center.longitude);
}

function topicLabel(topic: AdolescentConsultation['topic']): string {
  if (topic === 'contracepcion') return 'Anticoncepción';
  if (topic === 'prevencion') return 'Prevención';
  if (topic === 'ciclo') return 'Ciclo menstrual';
  return 'Otra consulta';
}

function statusClass(status: string): string {
  if (status === 'open') return 'bg-rose-100 text-rose-700';
  if (status === 'acknowledged') return 'bg-orange-100 text-orange-700';
  return 'bg-emerald-100 text-emerald-700';
}

function toLabel(latitude: number | string, longitude: number | string): string {
  return `${toNumber(latitude).toFixed(4)}, ${toNumber(longitude).toFixed(4)}`;
}

async function loadAll(): Promise<void> {
  const [centersResponse, alertsResponse, consultationsResponse] = await Promise.all([
    fetch(apiUrl('/health-centers/')),
    fetch(apiUrl('/panic-alerts/')),
    fetch(apiUrl('/adolescent-consultations/')),
  ]);

  centers.value = centersResponse.ok ? ((await centersResponse.json()) as HealthCenter[]) : [];
  alerts.value = alertsResponse.ok ? ((await alertsResponse.json()) as PanicAlert[]) : [];
  consultations.value = consultationsResponse.ok ? ((await consultationsResponse.json()) as AdolescentConsultation[]) : [];
}

async function saveCenter(): Promise<void> {
  const payload = {
    nombre: centerForm.nombre,
    nivel: centerForm.nivel,
    direccion: centerForm.direccion,
    ciudad: centerForm.ciudad,
    telefono: centerForm.telefono,
    telefono_emergencia: centerForm.telefono_emergencia,
    horario: centerForm.horario,
    ambulancia_disponible: centerForm.ambulancia_disponible,
    latitude: Number.parseFloat(centerForm.latitude),
    longitude: Number.parseFloat(centerForm.longitude),
  };

  const request = editingCenterId.value
    ? fetch(apiUrl(`/health-centers/${editingCenterId.value}/`), {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })
    : fetch(apiUrl('/health-centers/'), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

  const response = await request;
  if (response.ok) {
    await loadAll();
    resetCenterForm();
  }
}

async function updateAlertStatus(alertId: number, status: 'open' | 'acknowledged' | 'closed'): Promise<void> {
  await fetch(apiUrl(`/panic-alerts/${alertId}/`), {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status }),
  });
  await loadAll();
}

async function saveReply(consultationId: number, sessionToken: string): Promise<void> {
  await fetch(apiUrl(`/adolescent-consultations/${consultationId}/`), {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      answer: replyDraft[consultationId] ?? '',
      responder_name: responderDraft[consultationId] ?? '',
      status: replyDraft[consultationId] ? 'answered' : 'pending',
      session_token: sessionToken,
    }),
  });

  await loadAll();
}

async function markConsultationClosed(consultationId: number): Promise<void> {
  await fetch(apiUrl(`/adolescent-consultations/${consultationId}/`), {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status: 'closed' }),
  });

  await loadAll();
}

onMounted(async () => {
  document.title = 'Admin sector público | Mesa de Maternidad';
  await loadAll();
});
</script>

<style scoped>
.input-base {
  width: 100%;
  border-radius: 1rem;
  border: 1px solid rgb(226 232 240);
  background: rgb(248 250 252);
  padding: 0.75rem 1rem;
  color: rgb(15 23 42);
  outline: none;
  transition: all 0.2s ease;
}

.input-base:focus {
  border-color: rgb(20 184 166);
  box-shadow: 0 0 0 4px rgba(20, 184, 166, 0.12);
}
</style>
