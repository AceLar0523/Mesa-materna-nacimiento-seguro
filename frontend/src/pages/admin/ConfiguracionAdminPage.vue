<template>
  <div>
    <div class="admin-page-header">
      <h2>Configuración</h2>
      <div class="breadcrumb">
        <router-link to="/dashboard">Dashboard</router-link>
        <i class="pi pi-angle-right text-xs"></i>
        <span>Configuración</span>
      </div>
    </div>

    <div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
      <!-- Settings Navigation -->
      <div>
        <div class="admin-table-container">
          <div class="p-2">
            <button
              v-for="section in sections"
              :key="section.key"
              class="flex w-full items-center gap-3 rounded-xl px-4 py-3 text-left text-sm font-medium transition-colors"
              :class="activeSection === section.key
                ? 'bg-gradient-to-r from-orange-50 to-pink-50 text-[#F97316] font-semibold'
                : 'text-gray-600 hover:bg-gray-50'
              "
              @click="activeSection = section.key"
            >
              <i :class="section.icon" class="text-base"></i>
              {{ section.label }}
            </button>
          </div>
        </div>
      </div>

      <!-- Settings Content -->
      <div class="lg:col-span-2">
        <!-- General Settings -->
        <div v-if="activeSection === 'general'" class="admin-table-container">
          <div class="admin-table-header">
            <h3>Configuración General</h3>
          </div>
          <div class="p-6 space-y-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Nombre del Sitio</label>
              <input
                type="text"
                value="Mesa de Maternidad y Nacimiento Seguro"
                class="w-full rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm text-gray-900 transition-all focus:border-[#F97316] focus:outline-none focus:ring-2 focus:ring-[#F97316]/20"
              />
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Descripción</label>
              <textarea
                rows="3"
                class="w-full rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm text-gray-900 transition-all focus:border-[#F97316] focus:outline-none focus:ring-2 focus:ring-[#F97316]/20 resize-none"
              >Plataforma de gestión de la Mesa de Maternidad y Nacimiento Seguro de Bolivia</textarea>
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Email de Contacto</label>
              <input
                type="email"
                value="contacto@mnmns.org"
                class="w-full rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm text-gray-900 transition-all focus:border-[#F97316] focus:outline-none focus:ring-2 focus:ring-[#F97316]/20"
              />
            </div>
            <button class="admin-btn-primary">
              <i class="pi pi-save"></i>
              Guardar Cambios
            </button>
          </div>
        </div>

        <!-- Appearance -->
        <div v-if="activeSection === 'appearance'" class="admin-table-container">
          <div class="admin-table-header">
            <h3>Apariencia</h3>
          </div>
          <div class="p-6 space-y-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-3">Color Principal</label>
              <div class="flex gap-3">
                <div
                  v-for="color in themeColors"
                  :key="color"
                  class="h-10 w-10 rounded-xl cursor-pointer ring-2 ring-offset-2 transition-all hover:scale-110"
                  :class="color === '#F97316' ? 'ring-[#F97316]' : 'ring-transparent'"
                  :style="{ background: color }"
                ></div>
              </div>
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Logo del Sitio</label>
              <div class="flex items-center gap-4">
                <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-white p-2 shadow ring-1 ring-gray-100">
                  <img src="/img/logo1.jpg" alt="Logo" class="h-full w-full object-contain" />
                </div>
                <button class="admin-btn-primary">
                  <i class="pi pi-upload"></i>
                  Cambiar Logo
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Security -->
        <div v-if="activeSection === 'security'" class="admin-table-container">
          <div class="admin-table-header">
            <h3>Seguridad</h3>
          </div>
          <div class="p-6 space-y-6">
            <div class="flex items-center justify-between rounded-xl border border-gray-200 p-4">
              <div>
                <p class="text-sm font-semibold text-gray-900">Autenticación de dos factores</p>
                <p class="text-xs text-gray-500">Añade una capa extra de seguridad</p>
              </div>
              <div class="relative inline-flex h-6 w-11 cursor-pointer items-center rounded-full bg-gray-300 transition-colors">
                <span class="inline-block h-4 w-4 translate-x-1 transform rounded-full bg-white transition-transform"></span>
              </div>
            </div>
            <div class="flex items-center justify-between rounded-xl border border-gray-200 p-4">
              <div>
                <p class="text-sm font-semibold text-gray-900">Notificaciones por email</p>
                <p class="text-xs text-gray-500">Recibe alertas de seguridad por email</p>
              </div>
              <div class="relative inline-flex h-6 w-11 cursor-pointer items-center rounded-full bg-[#F97316] transition-colors">
                <span class="inline-block h-4 w-4 translate-x-6 transform rounded-full bg-white transition-transform"></span>
              </div>
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Cambiar Contraseña</label>
              <input
                type="password"
                placeholder="Nueva contraseña"
                class="w-full rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm text-gray-900 placeholder-gray-400 transition-all focus:border-[#F97316] focus:outline-none focus:ring-2 focus:ring-[#F97316]/20"
              />
            </div>
            <button class="admin-btn-primary">
              <i class="pi pi-shield"></i>
              Actualizar Seguridad
            </button>
          </div>
        </div>

        <!-- Notifications -->
        <div v-if="activeSection === 'notifications'" class="admin-table-container">
          <div class="admin-table-header">
            <h3>Notificaciones</h3>
          </div>
          <div class="p-6 space-y-4">
            <div v-for="notif in notifications" :key="notif.label" class="flex items-center justify-between rounded-xl border border-gray-200 p-4">
              <div>
                <p class="text-sm font-semibold text-gray-900">{{ notif.label }}</p>
                <p class="text-xs text-gray-500">{{ notif.description }}</p>
              </div>
              <div
                class="relative inline-flex h-6 w-11 cursor-pointer items-center rounded-full transition-colors"
                :class="notif.enabled ? 'bg-[#F97316]' : 'bg-gray-300'"
              >
                <span
                  class="inline-block h-4 w-4 transform rounded-full bg-white transition-transform"
                  :class="notif.enabled ? 'translate-x-6' : 'translate-x-1'"
                ></span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const activeSection = ref('general');

const sections = [
  { key: 'general', label: 'General', icon: 'pi pi-cog' },
  { key: 'appearance', label: 'Apariencia', icon: 'pi pi-palette' },
  { key: 'security', label: 'Seguridad', icon: 'pi pi-shield' },
  { key: 'notifications', label: 'Notificaciones', icon: 'pi pi-bell' },
];

const themeColors = ['#F97316', '#991a73', '#3b82f6', '#10b981', '#8b5cf6', '#ef4444'];

const notifications = [
  { label: 'Nuevos mensajes', description: 'Recibe notificación al recibir un mensaje', enabled: true },
  { label: 'Nuevos usuarios', description: 'Notificación cuando se registra un usuario', enabled: true },
  { label: 'Actualizaciones del sistema', description: 'Alertas sobre actualizaciones disponibles', enabled: false },
  { label: 'Reportes semanales', description: 'Resumen semanal de actividad', enabled: true },
];
</script>
