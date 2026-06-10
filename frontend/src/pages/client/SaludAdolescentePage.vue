<template>
  <div class="min-h-screen overflow-hidden bg-[radial-gradient(circle_at_top,_rgba(124,58,237,0.16),_transparent_30%),linear-gradient(180deg,#f8f7ff_0%,#ffffff_50%,#fff7ed_100%)] pt-20 text-slate-900">
    <PageHero
      kicker="Sector público"
      title="Espacio de salud sexual adolescente"
      subtitle="Consulta de forma anónima, conserva el historial en tu navegador y revisa si ya existe una respuesta segura del equipo moderador."
      backgroundImage="/img/fondo14.avif"
    />

    <section class="mx-auto grid max-w-7xl gap-8 px-4 py-12 sm:px-6 lg:grid-cols-[0.95fr_1.05fr] lg:px-8">
      <div class="space-y-6">
        <div class="rounded-[2rem] border border-violet-100 bg-white/90 p-6 shadow-[0_25px_80px_-38px_rgba(124,58,237,0.45)] backdrop-blur">
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.3em] text-violet-600">Anónimo por diseño</p>
              <h2 class="mt-2 text-2xl font-black text-slate-900">Consulta sin nombre, correo ni teléfono</h2>
            </div>
            <div class="rounded-2xl bg-violet-50 px-4 py-2 text-sm font-semibold text-violet-700">
              Código guardado: {{ sessionTokenPreview }}
            </div>
          </div>

          <div class="mt-6 flex flex-wrap gap-2">
            <button
              v-for="topic in topicChips"
              :key="topic.value"
              type="button"
              class="rounded-full px-4 py-2 text-sm font-semibold transition"
              :class="selectedTopic === topic.value ? 'bg-slate-950 text-white' : 'bg-slate-100 text-slate-600 hover:bg-violet-50 hover:text-violet-700'"
              @click="selectedTopic = topic.value"
            >
              {{ topic.label }}
            </button>
          </div>

          <form class="mt-6 space-y-4" @submit.prevent="sendQuestion">
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Tema</span>
              <select
                v-model="selectedTopic"
                class="w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none transition focus:border-violet-500 focus:ring-4 focus:ring-violet-100"
              >
                <option value="contracepcion">Anticoncepción</option>
                <option value="prevencion">Prevención</option>
                <option value="ciclo">Ciclo menstrual</option>
                <option value="otro">Otra consulta</option>
              </select>
            </label>

            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Tu duda</span>
              <textarea
                v-model="question"
                rows="6"
                class="w-full rounded-[1.5rem] border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-violet-500 focus:ring-4 focus:ring-violet-100"
                placeholder="Escribe tu consulta de forma clara. Por ejemplo: '¿Qué método anticonceptivo me recomiendan si aún no tengo relaciones regulares?'"
              ></textarea>
            </label>

            <div class="flex flex-wrap gap-3">
              <button
                type="submit"
                class="rounded-full bg-gradient-to-r from-[#7C3AED] via-[#F97316] to-[#FB7185] px-6 py-3 text-sm font-black text-white shadow-xl shadow-violet-200 transition hover:-translate-y-0.5 disabled:cursor-not-allowed disabled:opacity-60"
                :disabled="sending"
              >
                {{ sending ? 'Enviando...' : 'Enviar consulta anónima' }}
              </button>
              <button
                type="button"
                class="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 transition hover:border-violet-200 hover:text-violet-700"
                @click="refreshConsultations"
              >
                Verificar respuestas
              </button>
            </div>
          </form>

          <p class="mt-4 text-sm text-slate-500">{{ statusMessage }}</p>
        </div>

        <div class="grid gap-4 md:grid-cols-2">
          <article class="rounded-[1.75rem] border border-violet-100 bg-white p-5 shadow-sm">
            <p class="text-xs font-bold uppercase tracking-[0.25em] text-violet-600">Acceso guardado</p>
            <h3 class="mt-2 text-xl font-black text-slate-900">{{ sessionTokenPreview }}</h3>
            <p class="mt-2 text-sm text-slate-600">Puedes volver días después y seguir viendo tus respuestas guardadas en este navegador.</p>
          </article>
          <article class="rounded-[1.75rem] border border-orange-100 bg-gradient-to-br from-orange-50 to-white p-5 shadow-sm">
            <p class="text-xs font-bold uppercase tracking-[0.25em] text-orange-500">Estado</p>
            <h3 class="mt-2 text-xl font-black text-slate-900">{{ consultations.length }} conversaciones</h3>
            <p class="mt-2 text-sm text-slate-600">Las respuestas quedan asociadas a este navegador para que puedas retomarlas luego.</p>
          </article>
        </div>
      </div>

      <aside class="space-y-6 lg:sticky lg:top-28 lg:self-start">
        <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-lg">
          <div class="flex items-center justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.3em] text-slate-500">Bandeja local</p>
              <h3 class="mt-2 text-2xl font-black text-slate-900">Tus consultas guardadas</h3>
            </div>
              <span class="rounded-full bg-violet-50 px-3 py-1 text-xs font-bold text-violet-700">Anónimo</span>
          </div>

          <div class="mt-5 space-y-4">
            <template v-for="consultation in consultations" :key="consultation?.id">
              <article
                v-if="consultation"
                class="rounded-[1.5rem] border p-4 transition hover:-translate-y-0.5"
                :class="consultation.status === 'answered' ? 'border-emerald-100 bg-emerald-50/60' : 'border-slate-100 bg-slate-50'"
              >
                <div class="flex flex-wrap items-start justify-between gap-3">
                  <div>
                    <p class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">{{ topicLabel(consultation.topic) }}</p>
                    <h4 class="mt-1 font-black text-slate-900">{{ consultation.question }}</h4>
                  </div>
                  <span class="rounded-full px-3 py-1 text-xs font-bold" :class="statusClass(consultation.status)">{{ statusLabel(consultation.status) }}</span>
                </div>

                <div class="mt-4 rounded-2xl bg-white p-4 text-sm text-slate-700 shadow-sm">
                  <p class="text-xs font-bold uppercase tracking-[0.25em] text-slate-400">Respuesta</p>
                  <p class="mt-2 whitespace-pre-line">{{ consultation.answer || 'Todavía no hay respuesta del moderador.' }}</p>
                  <p v-if="consultation.responder_name" class="mt-2 text-xs text-slate-500">Atendió: {{ consultation.responder_name }}</p>
                </div>
              </article>
            </template>

            <p v-if="consultations.length === 0" class="rounded-[1.5rem] border border-dashed border-slate-200 p-4 text-sm text-slate-500">
              Aún no tienes consultas enviadas desde este navegador.
            </p>
          </div>
        </div>

        <div class="rounded-[2rem] border border-violet-100 bg-[radial-gradient(circle_at_top,_rgba(124,58,237,0.14),_transparent_34%),linear-gradient(180deg,#ffffff, #f8f7ff)] p-6 shadow-lg">
          <p class="text-xs font-bold uppercase tracking-[0.35em] text-violet-600">Guía rápida</p>
          <ul class="mt-4 space-y-3 text-sm text-slate-600">
            <li class="flex gap-3"><i class="pi pi-check-circle mt-1 text-violet-600"></i> No escribas nombres, correos ni teléfonos.</li>
            <li class="flex gap-3"><i class="pi pi-check-circle mt-1 text-violet-600"></i> Este espacio queda guardado en tu navegador.</li>
            <li class="flex gap-3"><i class="pi pi-check-circle mt-1 text-violet-600"></i> Puedes volver luego y verificar si ya hay respuesta.</li>
          </ul>
        </div>
      </aside>
    </section>

    <Footer class="mt-10" />
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue';
import Footer from '@/components/landing/Footer/Footer.vue';
import PageHero from '@/components/common/PageHero.vue';
import { apiUrl } from '@/utils/api';
import { ensureSessionToken, toApiList, type AdolescentConsultation, PUBLIC_SECTOR_TOKEN_KEY } from './public-sector';

const sessionToken = ref('');
const selectedTopic = ref<'contracepcion' | 'prevencion' | 'ciclo' | 'otro'>('contracepcion');
const question = ref('');
const sending = ref(false);
const statusMessage = ref('Escribe tu consulta con calma.');
const consultations = ref<AdolescentConsultation[]>([]);

const topicChips = [
  { value: 'contracepcion', label: 'Anticoncepción' },
  { value: 'prevencion', label: 'Prevención' },
  { value: 'ciclo', label: 'Ciclo' },
  { value: 'otro', label: 'Otra consulta' },
] as const;

const sessionTokenPreview = computed(() => (sessionToken.value ? `${sessionToken.value.slice(0, 8)}…${sessionToken.value.slice(-6)}` : 'sin acceso'));

function topicLabel(topic: AdolescentConsultation['topic']): string {
  if (!topic) return 'Consulta';
  if (topic === 'contracepcion') return 'Anticoncepción';
  if (topic === 'prevencion') return 'Prevención';
  if (topic === 'ciclo') return 'Ciclo menstrual';
  return 'Otra consulta';
}

function statusLabel(status: AdolescentConsultation['status']): string {
  if (!status) return 'Pendiente';
  if (status === 'answered') return 'Respondida';
  if (status === 'closed') return 'Cerrada';
  return 'Pendiente';
}

function statusClass(status: AdolescentConsultation['status']): string {
  if (status === 'answered') return 'bg-emerald-100 text-emerald-700';
  if (status === 'closed') return 'bg-slate-100 text-slate-600';
  return 'bg-violet-100 text-violet-700';
}

async function refreshConsultations(): Promise<void> {
  try {
    const response = await fetch(apiUrl(`/adolescent-consultations/?session_token=${sessionToken.value}`), {
      cache: 'no-store',
    });
    if (!response.ok) {
      throw new Error('No se pudieron cargar las consultas.');
    }

    const payload = (await response.json()) as unknown;
    consultations.value = toApiList<AdolescentConsultation>(payload);
  } catch {
    consultations.value = [];
  }
}

async function sendQuestion(): Promise<void> {
  if (!question.value.trim()) {
    statusMessage.value = 'Escribe una consulta antes de enviarla.';
    return;
  }

  sending.value = true;

  try {
    const response = await fetch(apiUrl('/adolescent-consultations/'), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        session_token: sessionToken.value,
        topic: selectedTopic.value,
        question: question.value.trim(),
        status: 'pending',
        answer: '',
        responder_name: '',
      }),
    });

    if (!response.ok) {
      throw new Error('No fue posible registrar la consulta.');
    }

    question.value = '';
    statusMessage.value = 'Consulta enviada. Puedes volver luego para revisar respuestas.';
    await refreshConsultations();
  } catch (error) {
    statusMessage.value = error instanceof Error ? error.message : 'Error inesperado al enviar la consulta.';
  } finally {
    sending.value = false;
  }
}

onMounted(async () => {
  document.title = 'Salud adolescente | Mesa de Maternidad';
  sessionToken.value = ensureSessionToken();
  await refreshConsultations();

  if (typeof window !== 'undefined') {
    const draft = window.localStorage.getItem(`${PUBLIC_SECTOR_TOKEN_KEY}:adolescent-draft`);
    if (draft) {
      question.value = draft;
    }
  }
});

watch(question, (value) => {
  if (typeof window === 'undefined') {
    return;
  }

  window.localStorage.setItem(`${PUBLIC_SECTOR_TOKEN_KEY}:adolescent-draft`, value);
});
</script>
