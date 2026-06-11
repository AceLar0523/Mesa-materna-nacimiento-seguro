<template>
  <div class="space-y-6 p-1">
    <main class="grid gap-6 lg:grid-cols-3">
      <router-link
        v-for="module in modules"
        :key="module.to"
        :to="module.to"
        class="group rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-md"
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
    to: '/dashboard/sector-publico/panel-operativo',
    title: 'Panel Maestro',
    badge: 'Nuevo',
    icon: 'pi pi-desktop',
    accent: 'bg-gradient-to-br from-[#1e293b] to-[#334155]',
    description: 'Vista consolidada de centros, alertas y consultas en una sola pantalla operativa.'
  },
  {
    to: '/dashboard/sector-publico/centros',
    title: 'Centros de salud',
    badge: 'Alta',
    icon: 'pi pi-map-marker',
    accent: 'bg-gradient-to-br from-[#0F766E] to-[#14B8A6]',
    description: 'Crear y actualizar hospitales, hospitales municipales y centros integrales de salud.'
  },
  {
    to: '/dashboard/sector-publico/alertas',
    title: 'Alertas de pánico',
    badge: 'Crítica',
    icon: 'pi pi-bell',
    accent: 'bg-gradient-to-br from-[#991B1B] to-[#F97316]',
    description: 'Monitorear alertas activas, reconocerlas y cerrar su ciclo operativo.'
  },
  {
    to: '/dashboard/sector-publico/consultas',
    title: 'Consultas adolescentes',
    badge: 'Moderación',
    icon: 'pi pi-comments',
    accent: 'bg-gradient-to-br from-[#7C3AED] to-[#F97316]',
    description: 'Responder consultas anónimas y marcar su estado sin exponer datos personales.'
  },
  {
    to: '/dashboard/sector-publico/near-miss',
    title: 'Registro Near-Miss',
    badge: 'Nuevo',
    icon: 'pi pi-heartbeat',
    accent: 'bg-gradient-to-br from-[#EC4899] to-[#F43F5E]',
    description: 'Gestión y análisis de casos de Morbilidad Materna Extrema bajo el enfoque de las 3 Demoras.'
  }
];

onMounted(() => {
  document.title = 'Admin sector público | Mesa de Maternidad';
});
</script>
