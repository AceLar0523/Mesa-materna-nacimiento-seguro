<template>
  <div>
    <!-- Welcome Card -->
    <div class="admin-welcome-card">
      <h2>¡Bienvenida, {{ user?.fullName || 'Administrador' }}! 👋</h2>
      <p>
        Este es tu panel de administración de la Mesa de Maternidad y Nacimiento Seguro.
        Aquí podrás gestionar todo el contenido, ver estadísticas y administrar el sistema.
      </p>
    </div>

    <!-- Stats Grid -->
    <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4 mb-6">
      <div
        v-for="stat in stats"
        :key="stat.label"
        class="admin-stat-card"
        :style="{ '--card-color': stat.color, '--card-color-end': stat.colorEnd }"
      >
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-500">{{ stat.label }}</p>
            <p class="mt-2 text-3xl font-bold text-gray-900">{{ stat.value }}</p>
            <p class="mt-1 text-xs font-medium" :style="{ color: stat.color }">
              <i class="pi pi-arrow-up text-xs"></i> {{ stat.change }}
            </p>
          </div>
          <div
            class="flex h-12 w-12 items-center justify-center rounded-xl"
            :style="{ background: stat.bg }"
          >
            <i :class="stat.icon" class="text-xl" :style="{ color: stat.color }"></i>
          </div>
        </div>
      </div>
    </div>

    <!-- Two Column Layout -->
    <div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
      <!-- Quick Actions -->
      <div class="lg:col-span-2">
        <div class="admin-table-container">
          <div class="admin-table-header">
            <h3>Acciones Rápidas</h3>
          </div>
          <div class="grid grid-cols-1 gap-4 p-6 sm:grid-cols-2 lg:grid-cols-3">
            <router-link
              v-for="action in quickActions"
              :key="action.to"
              :to="action.to"
              class="admin-action-card"
            >
              <i :class="action.icon" :style="{ color: action.color }"></i>
              <span>{{ action.label }}</span>
            </router-link>
          </div>
        </div>
      </div>

      <!-- Recent Activity -->
      <div>
        <div class="admin-table-container">
          <div class="admin-table-header">
            <h3>Actividad Reciente</h3>
          </div>
          <div class="p-4 space-y-3">
            <div
              v-for="(activity, idx) in recentActivity"
              :key="idx"
              class="flex items-start gap-3 rounded-xl p-3 transition-colors hover:bg-gray-50"
            >
              <div
                class="mt-0.5 flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-lg"
                :style="{ background: activity.bg }"
              >
                <i :class="activity.icon" class="text-sm" :style="{ color: activity.color }"></i>
              </div>
              <div class="min-w-0 flex-1">
                <p class="text-sm font-medium text-gray-900 truncate">{{ activity.title }}</p>
                <p class="text-xs text-gray-500">{{ activity.time }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Módulos Overview -->
    <div class="mt-6">
      <div class="admin-table-container">
        <div class="admin-table-header">
          <h3>Resumen de Módulos</h3>
        </div>
        <div class="overflow-x-auto">
          <table class="admin-table">
            <thead>
              <tr>
                <th>Módulo</th>
                <th>Registros</th>
                <th>Estado</th>
                <th>Última Actualización</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="mod in modules" :key="mod.name">
                <td class="font-medium text-gray-900">
                  <div class="flex items-center gap-2">
                    <i :class="mod.icon" class="text-sm" :style="{ color: mod.color }"></i>
                    {{ mod.name }}
                  </div>
                </td>
                <td>{{ mod.count }}</td>
                <td>
                  <span class="status-badge" :class="mod.statusClass">
                    <span class="inline-block h-1.5 w-1.5 rounded-full" :style="{ background: 'currentColor' }"></span>
                    {{ mod.status }}
                  </span>
                </td>
                <td>{{ mod.updated }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuth } from '@/composables/useAuth';

const { user } = useAuth();

const stats = [
  {
    label: 'Blog Posts',
    value: '24',
    change: '+3 este mes',
    icon: 'pi pi-file-edit',
    color: '#F97316',
    colorEnd: '#EA580C',
    bg: '#fff7ed',
  },
  {
    label: 'Mensajes',
    value: '12',
    change: '+5 nuevos',
    icon: 'pi pi-envelope',
    color: '#3b82f6',
    colorEnd: '#2563eb',
    bg: '#eff6ff',
  },
  {
    label: 'Usuarios',
    value: '156',
    change: '+12 este mes',
    icon: 'pi pi-users',
    color: '#8b5cf6',
    colorEnd: '#7c3aed',
    bg: '#f5f3ff',
  },
  {
    label: 'Visitas',
    value: '1.2k',
    change: '+18% vs mes anterior',
    icon: 'pi pi-chart-line',
    color: '#10b981',
    colorEnd: '#059669',
    bg: '#ecfdf5',
  },
];

const quickActions = [
  { label: 'Nuevo Post', icon: 'pi pi-pencil', color: '#F97316', to: '/dashboard/blog' },
  { label: 'Nueva Noticia', icon: 'pi pi-megaphone', color: '#991a73', to: '/dashboard/noticias' },
  { label: 'Subir Archivo', icon: 'pi pi-upload', color: '#3b82f6', to: '/dashboard/multimedia' },
  { label: 'Ver Mensajes', icon: 'pi pi-envelope', color: '#10b981', to: '/dashboard/mensajes' },
  { label: 'Gestionar Usuarios', icon: 'pi pi-users', color: '#8b5cf6', to: '/dashboard/usuarios' },
  { label: 'Configuración', icon: 'pi pi-cog', color: '#64748b', to: '/dashboard/configuracion' },
];

const recentActivity = [
  { title: 'Nuevo post publicado', time: 'Hace 2 horas', icon: 'pi pi-file-edit', color: '#F97316', bg: '#fff7ed' },
  { title: 'Usuario registrado', time: 'Hace 4 horas', icon: 'pi pi-user-plus', color: '#10b981', bg: '#ecfdf5' },
  { title: 'Mensaje recibido', time: 'Hace 6 horas', icon: 'pi pi-envelope', color: '#3b82f6', bg: '#eff6ff' },
  { title: 'Noticia actualizada', time: 'Ayer', icon: 'pi pi-megaphone', color: '#991a73', bg: '#fdf2f8' },
  { title: 'Institución añadida', time: 'Hace 2 días', icon: 'pi pi-building', color: '#8b5cf6', bg: '#f5f3ff' },
];

const modules = [
  { name: 'Blog', icon: 'pi pi-file-edit', color: '#F97316', count: '24 artículos', status: 'Activo', statusClass: 'status-active', updated: 'Hace 2 horas' },
  { name: 'Noticias', icon: 'pi pi-megaphone', color: '#991a73', count: '8 noticias', status: 'Activo', statusClass: 'status-active', updated: 'Ayer' },
  { name: 'Publicaciones', icon: 'pi pi-book', color: '#3b82f6', count: '15 documentos', status: 'Activo', statusClass: 'status-active', updated: 'Hace 3 días' },
  { name: 'Multimedia', icon: 'pi pi-images', color: '#10b981', count: '42 archivos', status: 'Activo', statusClass: 'status-active', updated: 'Hace 1 semana' },
  { name: 'Instituciones', icon: 'pi pi-building', color: '#8b5cf6', count: '7 instituciones', status: 'Activo', statusClass: 'status-active', updated: 'Hace 2 días' },
  { name: 'Usuarios', icon: 'pi pi-users', color: '#64748b', count: '156 usuarios', status: 'Activo', statusClass: 'status-active', updated: 'Hace 4 horas' },
];
</script>
