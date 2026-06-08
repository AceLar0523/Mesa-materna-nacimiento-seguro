<template>
  <div class="min-h-screen overflow-hidden bg-[radial-gradient(circle_at_top,_rgba(239,68,68,0.18),_transparent_30%),linear-gradient(180deg,#fff7ed_0%,#ffffff_50%,#fff1f2_100%)] pt-20 text-slate-900">
    <PageHero
      kicker="Sector público"
      title="Señales de alarma y botón de pánico"
      subtitle="Identifica síntomas críticos, marca tu ubicación y envía una alerta anónima al backend con un solo gesto."
      backgroundImage="/img/fondo14.avif"
    />

    <section class="mx-auto grid max-w-7xl gap-8 px-4 py-12 sm:px-6 lg:grid-cols-[1fr_0.95fr] lg:px-8">
      <div class="space-y-6">
        <div class="rounded-[2rem] border border-rose-100 bg-white/90 p-6 shadow-[0_25px_80px_-38px_rgba(244,63,94,0.5)] backdrop-blur">
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.3em] text-rose-500">Alerta prioritaria</p>
              <h2 class="mt-2 text-2xl font-black text-slate-900">Botón de pánico anónimo</h2>
            </div>
            <div class="rounded-2xl bg-rose-50 px-4 py-2 text-sm font-semibold text-rose-600">
              Token local activo: {{ sessionTokenPreview }}
            </div>
          </div>

          <div class="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
            <button
              v-for="symptom in symptoms"
              :key="symptom.key"
              type="button"
              class="group rounded-[1.5rem] border p-4 text-left transition hover:-translate-y-1 hover:shadow-xl"
              :class="selectedSymptom === symptom.key ? 'border-rose-300 bg-rose-50' : 'border-slate-200 bg-white'"
              @click="selectedSymptom = symptom.key"
            >
              <div class="flex h-11 w-11 items-center justify-center rounded-2xl bg-white text-xl shadow-sm" :class="symptom.accent">
                <i :class="symptom.icon"></i>
              </div>
              <h3 class="mt-3 text-base font-black text-slate-900">{{ symptom.label }}</h3>
              <p class="mt-2 text-sm text-slate-600">{{ symptom.description }}</p>
            </button>
          </div>

          <div class="mt-6 grid gap-4 md:grid-cols-2">
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Latitud</span>
              <input
                v-model="manualLatitude"
                type="number"
                step="0.000001"
                class="w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none transition focus:border-rose-500 focus:ring-4 focus:ring-rose-100"
              />
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Longitud</span>
              <input
                v-model="manualLongitude"
                type="number"
                step="0.000001"
                class="w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none transition focus:border-rose-500 focus:ring-4 focus:ring-rose-100"
              />
            </label>
          </div>

          <div class="mt-6 flex flex-wrap gap-3">
            <button
              type="button"
              class="rounded-full bg-gradient-to-r from-[#991B1B] via-[#F97316] to-[#FB7185] px-6 py-4 text-sm font-black text-white shadow-xl shadow-rose-200 transition hover:-translate-y-0.5 disabled:cursor-not-allowed disabled:opacity-60"
              :disabled="submitting"
              @click="sendAlert"
            >
              {{ submitting ? 'Enviando...' : 'Activar alerta crítica' }}
            </button>
            <button
              type="button"
              class="rounded-full border border-slate-200 bg-white px-5 py-4 text-sm font-semibold text-slate-700 transition hover:border-rose-200 hover:text-rose-600"
              @click="requestCurrentLocation"
            >
              Detectar ubicación
            </button>
          </div>

          <p class="mt-4 text-sm text-slate-500">{{ statusMessage }}</p>
        </div>

        <div class="grid gap-4 md:grid-cols-2">
          <article class="rounded-[1.75rem] border border-rose-100 bg-white p-5 shadow-sm">
            <p class="text-xs font-bold uppercase tracking-[0.25em] text-rose-500">Ubicación actual</p>
            <h3 class="mt-2 text-xl font-black text-slate-900">{{ locationLabel }}</h3>
            <p class="mt-2 text-sm text-slate-600">La coordenada se envía junto con la marca de tiempo al endpoint de alertas.</p>
          </article>
          <article class="rounded-[1.75rem] border border-orange-100 bg-gradient-to-br from-orange-50 to-white p-5 shadow-sm">
            <p class="text-xs font-bold uppercase tracking-[0.25em] text-orange-500">Respuesta rápida</p>
            <h3 class="mt-2 text-xl font-black text-slate-900">{{ lastAlertSummary }}</h3>
            <p class="mt-2 text-sm text-slate-600">Historial anónimo persistido por session_token.</p>
          </article>
        </div>
      </div>

      <aside class="space-y-6 lg:sticky lg:top-28 lg:self-start">
        <div class="rounded-[2rem] border border-slate-900 bg-slate-950 p-6 text-white shadow-[0_35px_90px_-40px_rgba(15,23,42,0.95)]">
          <div class="relative overflow-hidden rounded-[1.5rem] border border-white/10 bg-[radial-gradient(circle_at_top,_rgba(239,68,68,0.24),_transparent_36%),linear-gradient(180deg,rgba(15,23,42,0.96),rgba(88,28,28,0.98))] p-6">
            <div class="absolute -right-8 -top-8 h-32 w-32 rounded-full bg-rose-500/20 blur-3xl"></div>
            <div class="absolute -left-10 bottom-0 h-40 w-40 rounded-full bg-orange-400/20 blur-3xl"></div>
            <div class="relative flex flex-col items-center text-center">
              <div class="pulse-ring relative flex h-44 w-44 items-center justify-center rounded-full border border-white/15 bg-white/5">
                <div class="flex h-32 w-32 items-center justify-center rounded-full bg-gradient-to-br from-[#991B1B] via-[#F97316] to-[#FB7185] shadow-[0_0_0_20px_rgba(249,115,22,0.18)]">
                  <button
                    class="flex h-24 w-24 items-center justify-center rounded-full border border-white/30 bg-white text-rose-600 shadow-2xl transition hover:scale-105"
                    type="button"
                    :disabled="submitting"
                    @click="sendAlert"
                  >
                    <i class="pi pi-bell text-4xl"></i>
                  </button>
                </div>
              </div>
              <h2 class="mt-5 text-2xl font-black">Botón de pánico</h2>
              <p class="mt-2 max-w-sm text-sm leading-6 text-rose-100">
                Al presionarlo, se dispara una petición POST anónima hacia el backend con tus coordenadas y el síntoma seleccionado.
              </p>
            </div>
          </div>
        </div>

        <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-lg">
          <div class="flex items-center justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.3em] text-slate-500">Alertas recientes</p>
              <h3 class="mt-2 text-2xl font-black text-slate-900">{{ alerts.length }} registros</h3>
            </div>
            <span class="rounded-full bg-rose-50 px-3 py-1 text-xs font-bold text-rose-600">Anónimo</span>
          </div>

          <div class="mt-5 space-y-3">
            <article
              v-for="alert in alerts"
              :key="alert.id"
              class="rounded-2xl border border-slate-100 bg-slate-50 p-4"
            >
              <div class="flex items-center justify-between gap-3">
                <p class="font-bold text-slate-900">{{ alert.symptom || 'Alerta sin síntoma' }}</p>
                <span class="rounded-full px-3 py-1 text-xs font-bold" :class="alertBadgeClass(alert.status)">{{ alert.status }}</span>
              </div>
              <p class="mt-2 text-sm text-slate-600">{{ formatAlertDate(alert.created_at) }}</p>
              <p class="mt-1 text-xs text-slate-500">{{ toPointLabel(alert.latitude, alert.longitude) }}</p>
            </article>
            <p v-if="alerts.length === 0" class="rounded-2xl border border-dashed border-slate-200 p-4 text-sm text-slate-500">
              No hay alertas previas para este session_token.
            </p>
          </div>
        </div>
      </aside>
    </section>

    <Footer class="mt-10" />
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import Footer from '@/components/landing/Footer/Footer.vue';
import PageHero from '@/components/common/PageHero.vue';
import { apiUrl } from '@/utils/api';
import { ensureSessionToken, type PanicAlert } from './public-sector';

const sessionToken = ref('');
const selectedSymptom = ref('vision_borrosa');
const manualLatitude = ref('-16.500000');
const manualLongitude = ref('-68.150000');
const submitting = ref(false);
const statusMessage = ref('Prepara el botón antes de un evento crítico.');
const alerts = ref<PanicAlert[]>([]);
const currentLocation = ref({ latitude: -16.5, longitude: -68.15 });

const symptoms = [
  {
    key: 'edema_extremidades',
    label: 'Edema de extremidades',
    icon: 'pi pi-heart-fill',
    accent: 'text-rose-500',
    description: 'Hinchazón marcada en manos, pies o cara.'
  },
  {
    key: 'vision_borrosa',
    label: 'Visión borrosa',
    icon: 'pi pi-eye',
    accent: 'text-orange-500',
    description: 'Alteración súbita en la visión o destellos.'
  },
  {
    key: 'liquido_amniotico',
    label: 'Pérdida de líquido',
    icon: 'pi pi-tint',
    accent: 'text-teal-500',
    description: 'Salida de líquido amniótico antes del parto.'
  },
  {
    key: 'hemorragia',
    label: 'Hemorragia',
    icon: 'pi pi-exclamation-triangle',
    accent: 'text-rose-700',
    description: 'Sangrado vaginal o pérdida intensa de sangre.'
  },
];

const sessionTokenPreview = computed(() => (sessionToken.value ? `${sessionToken.value.slice(0, 8)}…${sessionToken.value.slice(-6)}` : 'sin token'));
const locationLabel = computed(() => `${currentLocation.value.latitude.toFixed(4)}, ${currentLocation.value.longitude.toFixed(4)}`);
const lastAlertSummary = computed(() => alerts.value[0]?.symptom || 'Esperando primera alerta');

function requestCurrentLocation(): void {
  if (!navigator.geolocation) {
    statusMessage.value = 'Tu navegador no soporta geolocalización. Usa las coordenadas manuales.';
    return;
  }

  navigator.geolocation.getCurrentPosition(
    (position) => {
      currentLocation.value = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude,
      };
      manualLatitude.value = position.coords.latitude.toFixed(6);
      manualLongitude.value = position.coords.longitude.toFixed(6);
      statusMessage.value = 'Ubicación obtenida correctamente.';
    },
    () => {
      statusMessage.value = 'No se pudo detectar GPS. Mantén las coordenadas manuales.';
    },
    { enableHighAccuracy: true, timeout: 12000, maximumAge: 120000 }
  );
}

function applyManualPosition(): void {
  const latitude = Number.parseFloat(manualLatitude.value);
  const longitude = Number.parseFloat(manualLongitude.value);

  if (Number.isNaN(latitude) || Number.isNaN(longitude)) {
    statusMessage.value = 'Coordenadas inválidas.';
    return;
  }

  currentLocation.value = { latitude, longitude };
}

function toPointLabel(latitude: number | string, longitude: number | string): string {
  const lat = typeof latitude === 'number' ? latitude : Number.parseFloat(latitude);
  const lng = typeof longitude === 'number' ? longitude : Number.parseFloat(longitude);
  return `${lat.toFixed(4)}, ${lng.toFixed(4)}`;
}

function alertBadgeClass(status: string): string {
  if (status === 'open') {
    return 'bg-rose-100 text-rose-700';
  }
  if (status === 'acknowledged') {
    return 'bg-orange-100 text-orange-700';
  }
  return 'bg-emerald-100 text-emerald-700';
}

function formatAlertDate(value: string): string {
  return new Date(value).toLocaleString('es-BO', {
    day: '2-digit',
    month: 'short',
    hour: '2-digit',
    minute: '2-digit',
  });
}

async function loadAlerts(): Promise<void> {
  try {
    const response = await fetch(apiUrl(`/panic-alerts/?session_token=${sessionToken.value}`));
    if (!response.ok) {
      throw new Error('No se pudieron cargar las alertas.');
    }

    alerts.value = (await response.json()) as PanicAlert[];
  } catch {
    alerts.value = [];
  }
}

async function sendAlert(): Promise<void> {
  submitting.value = true;

  try {
    applyManualPosition();
    const symptomLabel = symptoms.find((symptom) => symptom.key === selectedSymptom.value)?.label ?? selectedSymptom.value;

    const response = await fetch(apiUrl('/panic-alerts/'), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        session_token: sessionToken.value,
        symptom: symptomLabel,
        latitude: currentLocation.value.latitude,
        longitude: currentLocation.value.longitude,
        status: 'open',
        note: 'Alerta iniciada desde el botón de pánico del sector público.',
      }),
    });

    if (!response.ok) {
      throw new Error('No fue posible enviar la alerta.');
    }

    statusMessage.value = 'Alerta enviada y almacenada correctamente.';
    if ('vibrate' in navigator) {
      navigator.vibrate?.([120, 60, 120]);
    }

    await loadAlerts();
  } catch (error) {
    statusMessage.value = error instanceof Error ? error.message : 'Error inesperado al enviar la alerta.';
  } finally {
    submitting.value = false;
  }
}

onMounted(async () => {
  document.title = 'Señales de alarma | Mesa de Maternidad';
  sessionToken.value = ensureSessionToken();
  requestCurrentLocation();
  await loadAlerts();
});
</script>

<style scoped>
.pulse-ring::before,
.pulse-ring::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 9999px;
  border: 1px solid rgba(255, 255, 255, 0.14);
  animation: pulse 2.8s linear infinite;
}

.pulse-ring::after {
  animation-delay: 1.4s;
}

@keyframes pulse {
  0% {
    transform: scale(0.95);
    opacity: 0.9;
  }
  100% {
    transform: scale(1.25);
    opacity: 0;
  }
}
</style>
