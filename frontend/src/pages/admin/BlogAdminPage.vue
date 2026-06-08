<template>
  <div>
    <div class="admin-page-header">
      <h2>Blog</h2>
      <div class="breadcrumb">
        <router-link to="/dashboard">Dashboard</router-link>
        <i class="pi pi-angle-right text-xs"></i>
        <span>Blog</span>
      </div>
    </div>

    <div class="admin-table-container">
      <div class="admin-table-header">
        <h3>Artículos del Blog</h3>
        <button class="admin-btn-primary">
          <i class="pi pi-plus"></i>
          Nuevo Post
        </button>
      </div>

      <div class="overflow-x-auto">
        <table class="admin-table">
          <thead>
            <tr>
              <th>Título</th>
              <th>Categoría</th>
              <th>Estado</th>
              <th>Fecha</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="post in posts" :key="post.id">
              <td class="font-medium text-gray-900">{{ post.title }}</td>
              <td>{{ post.category }}</td>
              <td>
                <span class="status-badge" :class="post.statusClass">
                  {{ post.status }}
                </span>
              </td>
              <td>{{ post.date }}</td>
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
const posts = [
  { id: 1, title: 'La importancia del control prenatal', category: 'Salud Materna', status: 'Publicado', statusClass: 'status-active', date: '05 Jun 2026' },
  { id: 2, title: 'Lactancia materna: Guía completa', category: 'Nutrición', status: 'Publicado', statusClass: 'status-active', date: '03 Jun 2026' },
  { id: 3, title: 'Derechos de la mujer embarazada', category: 'Derechos', status: 'Borrador', statusClass: 'status-draft', date: '01 Jun 2026' },
  { id: 4, title: 'Signos de alarma durante el embarazo', category: 'Salud Materna', status: 'Publicado', statusClass: 'status-active', date: '28 May 2026' },
  { id: 5, title: 'Nutrición en el embarazo', category: 'Nutrición', status: 'Borrador', statusClass: 'status-draft', date: '25 May 2026' },
];
</script>
