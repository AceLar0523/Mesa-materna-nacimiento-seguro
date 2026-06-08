<template>
  <div>
    <div class="admin-page-header">
      <h2>Publicaciones</h2>
      <div class="breadcrumb">
        <router-link to="/dashboard">Dashboard</router-link>
        <i class="pi pi-angle-right text-xs"></i>
        <span>Publicaciones</span>
      </div>
    </div>

    <div class="admin-table-container">
      <div class="admin-table-header">
        <h3>Documentos y Recursos</h3>
        <button class="admin-btn-primary">
          <i class="pi pi-plus"></i>
          Nueva Publicación
        </button>
      </div>

      <div class="overflow-x-auto">
        <table class="admin-table">
          <thead>
            <tr>
              <th>Título</th>
              <th>Tipo</th>
              <th>Descargas</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="pub in publicaciones" :key="pub.id">
              <td class="font-medium text-gray-900">
                <div class="flex items-center gap-2">
                  <i class="pi pi-file-pdf text-red-500"></i>
                  {{ pub.title }}
                </div>
              </td>
              <td>{{ pub.type }}</td>
              <td>{{ pub.downloads }}</td>
              <td>
                <span class="status-badge" :class="pub.statusClass">{{ pub.status }}</span>
              </td>
              <td>
                <div class="flex gap-2">
                  <button class="admin-topbar-icon-btn" style="width:32px;height:32px;" title="Editar">
                    <i class="pi pi-pencil" style="font-size:0.75rem;"></i>
                  </button>
                  <button class="admin-topbar-icon-btn" style="width:32px;height:32px;" title="Descargar">
                    <i class="pi pi-download" style="font-size:0.75rem;"></i>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const publicaciones = [
  { id: 1, title: 'Guía de Atención Prenatal 2026', type: 'PDF', downloads: 342, status: 'Publicado', statusClass: 'status-active' },
  { id: 2, title: 'Informe Anual MNMNS 2025', type: 'PDF', downloads: 215, status: 'Publicado', statusClass: 'status-active' },
  { id: 3, title: 'Manual de Partería Comunitaria', type: 'PDF', downloads: 128, status: 'Publicado', statusClass: 'status-active' },
  { id: 4, title: 'Protocolo de Emergencias Obstétricas', type: 'PDF', downloads: 89, status: 'Borrador', statusClass: 'status-draft' },
];
</script>
