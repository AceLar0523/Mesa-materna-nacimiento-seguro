<template>
  <div>
    <div class="admin-page-header">
      <h2>Instituciones</h2>
      <div class="breadcrumb">
        <router-link to="/dashboard">Dashboard</router-link>
        <i class="pi pi-angle-right text-xs"></i>
        <span>Instituciones</span>
      </div>
    </div>

    <div class="admin-table-container">
      <div class="admin-table-header">
        <h3>Instituciones Aliadas</h3>
        <button class="admin-btn-primary">
          <i class="pi pi-plus"></i>
          Nueva Institución
        </button>
      </div>

      <div class="overflow-x-auto">
        <table class="admin-table">
          <thead>
            <tr>
              <th>Institución</th>
              <th>Tipo</th>
              <th>Departamento</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="inst in instituciones" :key="inst.id">
              <td class="font-medium text-gray-900">
                <div class="flex items-center gap-3">
                  <div class="flex h-9 w-9 items-center justify-center rounded-lg" :style="{ background: inst.bg }">
                    <i class="pi pi-building text-sm" :style="{ color: inst.color }"></i>
                  </div>
                  {{ inst.name }}
                </div>
              </td>
              <td>{{ inst.type }}</td>
              <td>{{ inst.department }}</td>
              <td>
                <span class="status-badge" :class="inst.statusClass">{{ inst.status }}</span>
              </td>
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
const instituciones = [
  { id: 1, name: 'Hospital de la Mujer', type: 'Hospital', department: 'La Paz', status: 'Activo', statusClass: 'status-active', color: '#F97316', bg: '#fff7ed' },
  { id: 2, name: 'Centro de Salud Villa Dolores', type: 'Centro de Salud', department: 'El Alto', status: 'Activo', statusClass: 'status-active', color: '#3b82f6', bg: '#eff6ff' },
  { id: 3, name: 'Maternidad Percy Boland', type: 'Maternidad', department: 'Santa Cruz', status: 'Activo', statusClass: 'status-active', color: '#991a73', bg: '#fdf2f8' },
  { id: 4, name: 'Hospital Gineco-Obstétrico', type: 'Hospital', department: 'Cochabamba', status: 'Activo', statusClass: 'status-active', color: '#10b981', bg: '#ecfdf5' },
  { id: 5, name: 'Centro Comunitario Warmi', type: 'ONG', department: 'Potosí', status: 'Inactivo', statusClass: 'status-inactive', color: '#8b5cf6', bg: '#f5f3ff' },
];
</script>
