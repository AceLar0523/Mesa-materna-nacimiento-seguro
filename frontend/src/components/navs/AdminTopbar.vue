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
};

const pageTitle = computed(() => {
  return pageMeta[route.path]?.title || 'Panel';
});

const pageDescription = computed(() => {
  return pageMeta[route.path]?.description || '';
});
</script>
