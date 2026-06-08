<template>
  <div>
    <div class="admin-page-header">
      <h2>Usuarios</h2>
      <div class="breadcrumb">
        <router-link to="/dashboard">Dashboard</router-link>
        <i class="pi pi-angle-right text-xs"></i>
        <span>Usuarios</span>
      </div>
    </div>

    <!-- Stats -->
    <div class="grid grid-cols-1 gap-4 sm:grid-cols-3 mb-6">
      <div class="admin-stat-card" style="--card-color:#10b981;--card-color-end:#059669;">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-500">Total Usuarios</p>
            <p class="mt-1 text-2xl font-bold text-gray-900">156</p>
          </div>
          <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-green-50">
            <i class="pi pi-users text-lg text-green-600"></i>
          </div>
        </div>
      </div>
      <div class="admin-stat-card" style="--card-color:#3b82f6;--card-color-end:#2563eb;">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-500">Activos Hoy</p>
            <p class="mt-1 text-2xl font-bold text-gray-900">23</p>
          </div>
          <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-50">
            <i class="pi pi-user text-lg text-blue-600"></i>
          </div>
        </div>
      </div>
      <div class="admin-stat-card" style="--card-color:#F97316;--card-color-end:#EA580C;">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-500">Nuevos (Mes)</p>
            <p class="mt-1 text-2xl font-bold text-gray-900">12</p>
          </div>
          <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-orange-50">
            <i class="pi pi-user-plus text-lg text-orange-600"></i>
          </div>
        </div>
      </div>
    </div>

    <div class="admin-table-container">
      <div class="admin-table-header">
        <h3>Lista de Usuarios</h3>
        <button class="admin-btn-primary">
          <i class="pi pi-plus"></i>
          Agregar Usuario
        </button>
      </div>

      <div class="overflow-x-auto">
        <table class="admin-table">
          <thead>
            <tr>
              <th>Usuario</th>
              <th>Email</th>
              <th>Rol</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="u in users" :key="u.id">
              <td>
                <div class="flex items-center gap-3">
                  <div
                    class="flex h-9 w-9 items-center justify-center rounded-full text-xs font-bold text-white"
                    :style="{ background: u.avatarBg }"
                  >
                    {{ u.initials }}
                  </div>
                  <span class="font-medium text-gray-900">{{ u.name }}</span>
                </div>
              </td>
              <td>{{ u.email }}</td>
              <td>
                <span
                  class="inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold"
                  :style="{ background: u.roleBg, color: u.roleColor }"
                >
                  {{ u.role }}
                </span>
              </td>
              <td>
                <span class="status-badge" :class="u.statusClass">{{ u.status }}</span>
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
const users = [
  { id: 1, name: 'María García', initials: 'MG', email: 'maria@mnmns.org', role: 'Admin', roleBg: '#fff7ed', roleColor: '#F97316', avatarBg: 'linear-gradient(135deg, #F97316, #991a73)', status: 'Activo', statusClass: 'status-active' },
  { id: 2, name: 'Carlos López', initials: 'CL', email: 'carlos@mnmns.org', role: 'Moderador', roleBg: '#f5f3ff', roleColor: '#8b5cf6', avatarBg: 'linear-gradient(135deg, #8b5cf6, #6366f1)', status: 'Activo', statusClass: 'status-active' },
  { id: 3, name: 'Ana Quispe', initials: 'AQ', email: 'ana@mnmns.org', role: 'Usuario', roleBg: '#eff6ff', roleColor: '#3b82f6', avatarBg: 'linear-gradient(135deg, #3b82f6, #2563eb)', status: 'Activo', statusClass: 'status-active' },
  { id: 4, name: 'Pedro Mamani', initials: 'PM', email: 'pedro@mnmns.org', role: 'Usuario', roleBg: '#eff6ff', roleColor: '#3b82f6', avatarBg: 'linear-gradient(135deg, #10b981, #059669)', status: 'Inactivo', statusClass: 'status-inactive' },
];
</script>
