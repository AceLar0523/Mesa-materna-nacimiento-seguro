<template>
  <div>
    <div class="admin-page-header">
      <h2>Noticias</h2>
      <div class="breadcrumb">
        <router-link to="/dashboard">Dashboard</router-link>
        <i class="pi pi-angle-right text-xs"></i>
        <span>Noticias</span>
      </div>
    </div>

    <div class="admin-table-container">
      <div class="admin-table-header">
        <h3>Gestión de Noticias</h3>
        <button class="admin-btn-primary">
          <i class="pi pi-plus"></i>
          Nueva Noticia
        </button>
      </div>

      <div class="overflow-x-auto">
        <table class="admin-table">
          <thead>
            <tr>
              <th>Titular</th>
              <th>Fuente</th>
              <th>Estado</th>
              <th>Fecha</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in noticias" :key="item.id">
              <td class="font-medium text-gray-900">{{ item.title }}</td>
              <td>{{ item.source }}</td>
              <td>
                <span class="status-badge" :class="item.statusClass">{{ item.status }}</span>
              </td>
              <td>{{ item.date }}</td>
              <td>
                <div class="flex gap-2">
                  <button class="admin-topbar-icon-btn" style="width:32px;height:32px;" title="Editar">
                    <i class="pi pi-pencil" style="font-size:0.75rem;"></i>
                  </button>
                  <button class="admin-topbar-icon-btn" style="width:32px;height:32px;" title="Eliminar">
                    <i class="pi pi-trash" style="font-size:0.75rem;"></i>
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
const noticias = [
  { id: 1, title: 'Bolivia refuerza políticas de salud materna', source: 'Ministerio de Salud', status: 'Publicado', statusClass: 'status-active', date: '06 Jun 2026' },
  { id: 2, title: 'Nuevo centro de atención prenatal en La Paz', source: 'MNMNS', status: 'Publicado', statusClass: 'status-active', date: '04 Jun 2026' },
  { id: 3, title: 'Campaña de vacunación prenatal 2026', source: 'OMS Bolivia', status: 'Borrador', statusClass: 'status-draft', date: '02 Jun 2026' },
  { id: 4, title: 'Resultados del programa de parteras comunitarias', source: 'MNMNS', status: 'Publicado', statusClass: 'status-active', date: '30 May 2026' },
];
</script>
