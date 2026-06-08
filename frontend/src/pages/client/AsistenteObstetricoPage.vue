<template>
  <div class="min-h-screen overflow-hidden bg-[radial-gradient(circle_at_top,_rgba(249,115,22,0.14),_transparent_35%),linear-gradient(180deg,#fff7ed_0%,#ffffff_52%,#fff1f4_100%)] pt-20 text-slate-900">
    <PageHero
      kicker="Sector público"
      title="Asistente obstétrico basado en FUM"
      subtitle="Calcula la edad gestacional, estima la fecha probable de parto y muestra el cronograma de cinco controles prenatales mínimos sin guardar datos sensibles en el servidor."
      backgroundImage="/img/fondo14.avif"
    />

    <section class="mx-auto grid max-w-7xl gap-8 px-4 py-12 sm:px-6 lg:grid-cols-[1.1fr_0.9fr] lg:px-8">
      <div class="space-y-6">
        <div class="rounded-[2rem] border border-orange-100 bg-white/85 p-6 shadow-[0_20px_80px_-35px_rgba(249,115,22,0.45)] backdrop-blur">
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.3em] text-[#F97316]">Persistencia local</p>
              <h2 class="mt-2 text-2xl font-black text-slate-900">Perfil obstétrico en tu dispositivo</h2>
            </div>
            <div class="rounded-2xl bg-orange-50 px-4 py-2 text-sm font-semibold text-[#EA580C]">
              {{ isSaved ? 'Guardado en localStorage' : 'Sin datos guardados' }}
            </div>
          </div>

          <div class="mt-6 grid gap-4 md:grid-cols-3">
            <article class="rounded-3xl border border-orange-100 bg-gradient-to-br from-orange-50 to-white p-4">
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-orange-500">Edad gestacional</p>
              <p class="mt-3 text-4xl font-black text-slate-900">{{ gestationalWeeks }}<span class="text-xl text-slate-500"> sem</span></p>
              <p class="mt-1 text-sm text-slate-600">{{ gestationalDays }} días estimados</p>
            </article>
            <article class="rounded-3xl border border-rose-100 bg-gradient-to-br from-rose-50 to-white p-4">
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-rose-500">Fecha probable de parto</p>
              <p class="mt-3 text-2xl font-black text-slate-900">{{ dueDateLabel }}</p>
              <p class="mt-1 text-sm text-slate-600">Calculada con {{ calculationMethodLabel }}</p>
            </article>
            <article class="rounded-3xl border border-emerald-100 bg-gradient-to-br from-emerald-50 to-white p-4">
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-emerald-500">Próximo control</p>
              <p class="mt-3 text-2xl font-black text-slate-900">{{ nextControl?.title ?? 'Completar FUM' }}</p>
              <p class="mt-1 text-sm text-slate-600">{{ nextControl?.window ?? 'Se completa automáticamente' }}</p>
            </article>
          </div>

          <form class="mt-8 grid gap-4 md:grid-cols-[1.2fr_0.8fr]" @submit.prevent>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Fecha de última menstruación</span>
              <input
                v-model="fum"
                type="date"
                class="w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none transition focus:border-[#F97316] focus:ring-4 focus:ring-orange-100"
              />
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Método de cálculo</span>
              <select
                v-model="calculationMethod"
                class="w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none transition focus:border-[#F97316] focus:ring-4 focus:ring-orange-100"
              >
                <option value="naegele">Regla de Naegele</option>
                <option value="wahl">Regla de Wahl</option>
              </select>
            </label>
          </form>

          <div class="mt-6 flex flex-wrap gap-3">
            <button
              type="button"
              class="rounded-full bg-gradient-to-r from-[#F97316] to-[#FB7185] px-5 py-3 text-sm font-bold text-white shadow-lg shadow-orange-200 transition hover:-translate-y-0.5"
              @click="saveProfile"
            >
              Guardar solo en este dispositivo
            </button>
            <button
              type="button"
              class="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 transition hover:border-orange-200 hover:text-[#EA580C]"
              @click="resetProfile"
            >
              Limpiar perfil local
            </button>
          </div>
        </div>

        <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-5">
          <article
            v-for="control in controlPlan"
            :key="control.id"
            class="group relative overflow-hidden rounded-[1.75rem] border p-4 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl"
            :class="control.active ? 'border-orange-200 bg-white' : 'border-slate-200 bg-white/80'"
          >
            <div class="absolute inset-x-0 top-0 h-1 bg-gradient-to-r from-[#F97316] via-[#FB7185] to-[#7C3AED]"></div>
            <p class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Control {{ control.id }}</p>
            <h3 class="mt-3 text-lg font-black text-slate-900">{{ control.title }}</h3>
            <p class="mt-2 text-sm text-slate-600">{{ control.description }}</p>
            <div class="mt-4 rounded-2xl bg-slate-50 px-3 py-2 text-xs font-semibold text-slate-500">
              {{ control.window }}
            </div>
            <div
              class="mt-4 inline-flex rounded-full px-3 py-1 text-xs font-bold"
              :class="control.active ? 'bg-orange-100 text-[#EA580C]' : 'bg-slate-100 text-slate-500'"
            >
              {{ control.active ? 'Control vigente' : 'Próximo' }}
            </div>
          </article>
        </div>
      </div>

      <aside class="space-y-6 lg:sticky lg:top-28 lg:self-start">
        <div class="rounded-[2rem] border border-white/70 bg-slate-950 p-6 text-white shadow-[0_30px_80px_-35px_rgba(15,23,42,0.85)]">
          <p class="text-xs font-bold uppercase tracking-[0.35em] text-orange-200">Cronograma dinámico</p>
          <h2 class="mt-3 text-2xl font-black">Ventanas recomendadas de control prenatal</h2>
          <div class="mt-6 space-y-4">
            <div
              v-for="item in timeline"
              :key="item.id"
              class="flex items-start gap-4 rounded-2xl border border-white/10 bg-white/5 p-4"
            >
              <div class="mt-1 flex h-10 w-10 items-center justify-center rounded-2xl bg-gradient-to-br from-[#F97316] to-[#FB7185] text-sm font-black">
                {{ item.id }}
              </div>
              <div class="flex-1">
                <div class="flex items-center justify-between gap-3">
                  <p class="font-bold">{{ item.title }}</p>
                  <span class="text-xs text-orange-200">{{ item.window }}</span>
                </div>
                <p class="mt-1 text-sm text-slate-300">{{ item.description }}</p>
              </div>
            </div>
          </div>
        </div>

        <div class="rounded-[2rem] border border-orange-100 bg-white p-6 shadow-lg">
          <div class="flex items-center gap-3">
            <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-orange-50 text-[#F97316]">
              <i class="pi pi-shield text-xl"></i>
            </div>
            <div>
              <h3 class="font-black text-slate-900">Privacidad reforzada</h3>
              <p class="text-sm text-slate-500">Los datos obstétricos se quedan en tu navegador.</p>
            </div>
          </div>
          <p class="mt-4 text-sm leading-6 text-slate-600">
            Este asistente no guarda historial clínico en el servidor. Solo conserva la FUM y el método de cálculo de forma local para reabrir el cronograma cuando vuelvas.
          </p>
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

const STORAGE_KEY = 'mesa-public-sector-obstetric-profile';

const fum = ref('');
const calculationMethod = ref<'naegele' | 'wahl'>('naegele');
const isSaved = ref(false);

const timeline = [
  {
    id: 1,
    title: 'Primer control',
    window: '8 - 12 semanas',
    description: 'Captación temprana, laboratorio base y confirmación del plan de seguimiento.'
  },
  {
    id: 2,
    title: 'Segundo control',
    window: '16 - 20 semanas',
    description: 'Seguimiento de crecimiento, nutrición y alertas maternas tempranas.'
  },
  {
    id: 3,
    title: 'Tercer control',
    window: '24 - 28 semanas',
    description: 'Tamizaje intermedio, revisión de signos de alarma y educación perinatal.'
  },
  {
    id: 4,
    title: 'Cuarto control',
    window: '30 - 34 semanas',
    description: 'Acompañamiento del tercer trimestre y preparación para el parto.'
  },
  {
    id: 5,
    title: 'Quinto control',
    window: '36 - 40 semanas',
    description: 'Plan final de nacimiento seguro, ruta de emergencia y red de apoyo.'
  }
];

const parsedFum = computed(() => {
  if (!fum.value) {
    return null;
  }

  const value = new Date(`${fum.value}T00:00:00`);
  return Number.isNaN(value.getTime()) ? null : value;
});

const referenceDays = computed(() => (calculationMethod.value === 'wahl' ? 285 : 280));

const today = new Date();

const gestationalDays = computed(() => {
  if (!parsedFum.value) {
    return 0;
  }

  const elapsed = Math.max(0, Math.floor((today.getTime() - parsedFum.value.getTime()) / 86400000));
  return elapsed;
});

const gestationalWeeks = computed(() => Math.floor(gestationalDays.value / 7));

const dueDate = computed(() => {
  if (!parsedFum.value) {
    return null;
  }

  const date = new Date(parsedFum.value.getTime());
  date.setDate(date.getDate() + referenceDays.value);
  return date;
});

const dueDateLabel = computed(() => {
  if (!dueDate.value) {
    return 'Agrega tu FUM';
  }

  return dueDate.value.toLocaleDateString('es-BO', {
    day: '2-digit',
    month: 'short',
    year: 'numeric'
  });
});

const calculationMethodLabel = computed(() => (calculationMethod.value === 'wahl' ? 'la regla de Wahl' : 'la regla de Naegele'));

const controlPlan = computed(() => {
  const activeWeeks = gestationalWeeks.value;

  return [
    {
      id: 1,
      title: 'Captación temprana',
      window: '8 - 12 semanas',
      description: 'Confirmación del embarazo, perfil inicial y plan de autocuidado.',
      active: activeWeeks >= 8 && activeWeeks <= 12
    },
    {
      id: 2,
      title: 'Seguimiento intermedio',
      window: '16 - 20 semanas',
      description: 'Evaluación del crecimiento fetal y estado general materno.',
      active: activeWeeks >= 16 && activeWeeks <= 20
    },
    {
      id: 3,
      title: 'Tamizaje y educación',
      window: '24 - 28 semanas',
      description: 'Reforzar alimentación, ejercicios y signos de alarma.',
      active: activeWeeks >= 24 && activeWeeks <= 28
    },
    {
      id: 4,
      title: 'Preparación del parto',
      window: '30 - 34 semanas',
      description: 'Plan familiar, ruta de referencia y control del tercer trimestre.',
      active: activeWeeks >= 30 && activeWeeks <= 34
    },
    {
      id: 5,
      title: 'Cierre obstétrico',
      window: '36 - 40 semanas',
      description: 'Plan de nacimiento, acompañamiento y urgencias.',
      active: activeWeeks >= 36 && activeWeeks <= 40
    }
  ];
});

const nextControl = computed(() => controlPlan.value.find((control) => control.active) ?? controlPlan.value.find((control) => gestationalWeeks.value < Number.parseInt(control.window, 10)) ?? null);

const saveProfile = () => {
  if (typeof window === 'undefined') {
    return;
  }

  window.localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify({
      fum: fum.value,
      calculationMethod: calculationMethod.value
    })
  );
  isSaved.value = true;
};

const resetProfile = () => {
  fum.value = '';
  calculationMethod.value = 'naegele';
  isSaved.value = false;

  if (typeof window !== 'undefined') {
    window.localStorage.removeItem(STORAGE_KEY);
  }
};

watch([fum, calculationMethod], () => {
  if (fum.value) {
    saveProfile();
  }
});

onMounted(() => {
  document.title = 'Asistente obstétrico | Mesa de Maternidad';

  if (typeof window === 'undefined') {
    return;
  }

  const saved = window.localStorage.getItem(STORAGE_KEY);
  if (saved) {
    try {
      const parsed = JSON.parse(saved) as { fum?: string; calculationMethod?: 'naegele' | 'wahl' };
      fum.value = parsed.fum ?? '';
      calculationMethod.value = parsed.calculationMethod ?? 'naegele';
      isSaved.value = true;
    } catch {
      window.localStorage.removeItem(STORAGE_KEY);
    }
  }
});
</script>
