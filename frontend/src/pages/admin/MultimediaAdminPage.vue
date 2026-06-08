<template>
  <div>
    <div class="admin-page-header">
      <h2>Multimedia</h2>
      <div class="breadcrumb">
        <router-link to="/dashboard">Dashboard</router-link>
        <i class="pi pi-angle-right text-xs"></i>
        <span>Multimedia</span>
      </div>
    </div>

    <!-- Upload Area -->
    <div
      class="mb-6 rounded-2xl border-2 border-dashed border-gray-300 bg-white p-8 text-center transition-colors hover:border-[#F97316]"
    >
      <i class="pi pi-cloud-upload text-4xl text-gray-400 mb-3 block"></i>
      <p class="font-semibold text-gray-700 mb-1">Arrastra archivos aquí o haz clic para subir</p>
      <p class="text-sm text-gray-500">PNG, JPG, MP4, PDF hasta 50MB</p>
      <button class="admin-btn-primary mt-4">
        <i class="pi pi-upload"></i>
        Seleccionar Archivos
      </button>
    </div>

    <!-- Media Grid -->
    <div class="admin-table-container">
      <div class="admin-table-header">
        <h3>Biblioteca de Medios ({{ mediaItems.length }} archivos)</h3>
        <div class="flex gap-2">
          <button class="admin-topbar-icon-btn" title="Vista cuadrícula">
            <i class="pi pi-th-large"></i>
          </button>
          <button class="admin-topbar-icon-btn" title="Vista lista">
            <i class="pi pi-list"></i>
          </button>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-4 p-6 sm:grid-cols-3 lg:grid-cols-4">
        <div
          v-for="media in mediaItems"
          :key="media.id"
          class="group cursor-pointer overflow-hidden rounded-xl border border-gray-100 bg-gray-50 transition-all hover:shadow-lg hover:border-[#F97316]"
        >
          <div class="aspect-video flex items-center justify-center" :style="{ background: media.bg }">
            <i :class="media.icon" class="text-3xl" :style="{ color: media.color }"></i>
          </div>
          <div class="p-3">
            <p class="text-sm font-medium text-gray-900 truncate">{{ media.name }}</p>
            <p class="text-xs text-gray-500">{{ media.size }} · {{ media.date }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const mediaItems = [
  { id: 1, name: 'fondo1.jpg', size: '177 KB', date: 'Jun 2026', icon: 'pi pi-image', color: '#F97316', bg: '#fff7ed' },
  { id: 2, name: 'hero-mnmns.svg', size: '1.6 KB', date: 'Jun 2026', icon: 'pi pi-image', color: '#10b981', bg: '#ecfdf5' },
  { id: 3, name: 'video-campaña.mp4', size: '24 MB', date: 'May 2026', icon: 'pi pi-video', color: '#3b82f6', bg: '#eff6ff' },
  { id: 4, name: 'informe-2025.pdf', size: '2.3 MB', date: 'May 2026', icon: 'pi pi-file-pdf', color: '#ef4444', bg: '#fef2f2' },
  { id: 5, name: 'logo1.jpg', size: '273 KB', date: 'Abr 2026', icon: 'pi pi-image', color: '#F97316', bg: '#fff7ed' },
  { id: 6, name: 'fondo2.jpg', size: '103 KB', date: 'Abr 2026', icon: 'pi pi-image', color: '#8b5cf6', bg: '#f5f3ff' },
  { id: 7, name: 'network-map.svg', size: '899 B', date: 'Mar 2026', icon: 'pi pi-image', color: '#10b981', bg: '#ecfdf5' },
  { id: 8, name: 'presentación.pptx', size: '5.1 MB', date: 'Mar 2026', icon: 'pi pi-file', color: '#d97706', bg: '#fffbeb' },
];
</script>
