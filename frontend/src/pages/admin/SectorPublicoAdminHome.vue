<template>
  <div class="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(15,118,110,0.16),_transparent_28%),linear-gradient(180deg,#0f172a_0%,#ffffff_54%,#fff7ed_100%)] pt-16 text-slate-900">
    <header class="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
      <div class="rounded-[2rem] border border-white/20 bg-slate-950 p-8 text-white shadow-[0_30px_90px_-40px_rgba(15,23,42,0.95)]">
        <p class="text-xs font-bold uppercase tracking-[0.35em] text-teal-200">Admin público</p>
        <h1 class="mt-3 text-3xl font-black md:text-5xl">Administración del sector público</h1>
        <p class="mt-4 max-w-3xl text-sm leading-6 text-slate-300 md:text-base">
          Cada módulo con operación administrativa propia. Entra directo al que necesites sin mezclar flujos en una sola vista.
        </p>
      </div>
    </header>

    <main class="mx-auto grid max-w-7xl gap-6 px-4 pb-12 sm:px-6 lg:grid-cols-3 lg:px-8">
      <router-link
        v-for="module in modules"
        :key="module.to"
        :to="module.to"
        class="group rounded-[2rem] border border-slate-200 bg-white p-6 shadow-lg transition hover:-translate-y-1 hover:shadow-xl"
      >
        <div class="flex items-center justify-between gap-4">
          <div class="flex h-14 w-14 items-center justify-center rounded-2xl text-white shadow-sm" :class="module.accent">
            <i :class="module.icon" class="text-2xl"></i>
          </div>
          <span class="rounded-full bg-slate-100 px-3 py-1 text-xs font-bold text-slate-500">{{ module.badge }}</span>
        </div>
        <h2 class="mt-5 text-2xl font-black text-slate-900">{{ module.title }}</h2>
        <p class="mt-3 text-sm leading-6 text-slate-600">{{ module.description }}</p>
        <div class="mt-6 flex items-center gap-2 text-sm font-bold text-[#0F766E]">
          Entrar
          <i class="pi pi-arrow-right transition group-hover:translate-x-1"></i>
        </div>
      </router-link>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';

const modules = [
  {
    to: '/admin/sector-publico/centros',
    title: 'Centros de salud',
    badge: 'Alta',
    icon: 'pi pi-map-marker',
    accent: 'bg-gradient-to-br from-[#0F766E] to-[#14B8A6]',
    description: 'Crear y actualizar hospitales, hospitales municipales y centros integrales de salud.'
  },
  {
    to: '/admin/sector-publico/alertas',
    title: 'Alertas de pánico',
    badge: 'Crítica',
    icon: 'pi pi-bell',
    accent: 'bg-gradient-to-br from-[#991B1B] to-[#F97316]',
    description: 'Monitorear alertas activas, reconocerlas y cerrar su ciclo operativo.'
  },
  {
    to: '/admin/sector-publico/consultas',
    title: 'Consultas adolescentes',
    badge: 'Moderación',
    icon: 'pi pi-comments',
    accent: 'bg-gradient-to-br from-[#7C3AED] to-[#F97316]',
    description: 'Responder consultas anónimas y marcar su estado sin exponer datos personales.'
  }
];

onMounted(() => {
  document.title = 'Admin sector público | Mesa de Maternidad';
});
</script>
