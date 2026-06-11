<template>
  <header class="admin-topbar">
    <div class="admin-topbar-left">
      <button class="admin-hamburger" @click="$emit('toggle-sidebar')">
        <i class="pi pi-bars"></i>
      </button>

      <div class="admin-topbar-title">
        <h1>{{ pageTitle }}</h1>
        <p>{{ pageDescription }}</p>
      </div>
    </div>

    <div class="admin-topbar-right">
      <div class="hidden md:flex items-center gap-2 mr-4">
        <router-link to="/dashboard/sector-publico/panel-operativo" class="text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-lg bg-teal-50 text-teal-700 hover:bg-teal-100 transition-colors">
          Panel Maestro
        </router-link>
        <router-link to="/dashboard/sector-publico/alertas" class="text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-lg bg-rose-50 text-rose-700 hover:bg-rose-100 transition-colors">
          Alertas
        </router-link>
      </div>

      <div class="admin-topbar-search">
        <i class="pi pi-search"></i>
        <input type="text" placeholder="Buscar..." />
      </div>

      <button class="admin-topbar-icon-btn" title="Notificaciones">
        <i class="pi pi-bell"></i>
        <span class="notif-dot"></span>
      </button>
    </div>
  </header>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';

defineEmits(['toggle-sidebar']);

const route = useRoute();

const pageMeta: Record<string, { title: string; description: string }> = {
  '/dashboard': { title: 'Dashboard', description: 'Resumen general del sistema' },
  '/dashboard/blog': { title: 'Blog', description: 'Gestión de artículos y posts' },
  '/dashboard/noticias': { title: 'Noticias', description: 'Gestión de noticias y actualizaciones' },
  '/dashboard/publicaciones': { title: 'Publicaciones', description: 'Documentos y recursos descargables' },
  '/dashboard/multimedia': { title: 'Multimedia', description: 'Fotos, videos y recursos visuales' },
  '/dashboard/instituciones': { title: 'Instituciones', description: 'Gestión de instituciones aliadas' },
  '/dashboard/usuarios': { title: 'Usuarios', description: 'Gestión de usuarios del sistema' },
  '/dashboard/mensajes': { title: 'Mensajes', description: 'Bandeja de mensajes y contacto' },
  '/dashboard/configuracion': { title: 'Configuración', description: 'Ajustes generales del sistema' },
  '/dashboard/sector-publico': { title: 'Sector Público', description: 'Administración de servicios ciudadanos' },
  '/dashboard/sector-publico/centros': { title: 'Centros de Salud', description: 'Gestión de establecimientos médicos' },
  '/dashboard/sector-publico/alertas': { title: 'Alertas de Pánico', description: 'Monitoreo de señales de emergencia' },
  '/dashboard/sector-publico/consultas': { title: 'Consultas Jóvenes', description: 'Moderación de dudas anónimas' },
  '/dashboard/sector-publico/near-miss': { title: 'Registro Near-Miss', description: 'Morbilidad Materna Extrema' },
};

const pageTitle = computed(() => {
  return pageMeta[route.path]?.title || 'Panel';
});

const pageDescription = computed(() => {
  return pageMeta[route.path]?.description || '';
});
</script>
