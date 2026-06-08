<template>
  <!-- Mobile Overlay -->
  <div
    class="admin-sidebar-overlay"
    :class="{ visible: isOpen }"
    @click="$emit('close')"
  ></div>

  <aside class="admin-sidebar" :class="{ 'sidebar-open': isOpen }">
    <!-- Logo -->
    <div class="admin-sidebar-logo">
      <img src="/img/logo1.jpg" alt="MNMNS Bolivia" />
      <div class="admin-sidebar-logo-text">
        <span class="logo-title">Mesa de Maternidad</span>
        <span class="logo-subtitle">Panel de Administración</span>
      </div>
    </div>

    <!-- Navigation -->
    <nav class="admin-sidebar-nav">
      <!-- Principal -->
      <div class="admin-nav-section">
        <p class="admin-nav-section-title">Principal</p>
        <router-link
          v-for="item in mainNav"
          :key="item.to"
          :to="item.to"
          class="admin-nav-item"
          :class="{ active: isActive(item.to) }"
          @click="$emit('close')"
        >
          <i :class="item.icon"></i>
          <span>{{ item.label }}</span>
          <span v-if="item.badge" class="nav-badge">{{ item.badge }}</span>
        </router-link>
      </div>

      <!-- Contenido -->
      <div class="admin-nav-section">
        <p class="admin-nav-section-title">Gestión de Contenido</p>
        <router-link
          v-for="item in contentNav"
          :key="item.to"
          :to="item.to"
          class="admin-nav-item"
          :class="{ active: isActive(item.to) }"
          @click="$emit('close')"
        >
          <i :class="item.icon"></i>
          <span>{{ item.label }}</span>
          <span v-if="item.badge" class="nav-badge">{{ item.badge }}</span>
        </router-link>
      </div>

      <!-- Sistema -->
      <div class="admin-nav-section">
        <p class="admin-nav-section-title">Sistema</p>
        <router-link
          v-for="item in systemNav"
          :key="item.to"
          :to="item.to"
          class="admin-nav-item"
          :class="{ active: isActive(item.to) }"
          @click="$emit('close')"
        >
          <i :class="item.icon"></i>
          <span>{{ item.label }}</span>
          <span v-if="item.badge" class="nav-badge">{{ item.badge }}</span>
        </router-link>
      </div>
    </nav>

    <!-- User Section -->
    <div class="admin-sidebar-user">
      <div class="admin-user-avatar">
        {{ userInitials }}
      </div>
      <div class="admin-user-info">
        <div class="admin-user-name">{{ user?.fullName || 'Usuario' }}</div>
        <div class="admin-user-role">{{ roleLabel }}</div>
      </div>
      <button class="admin-logout-btn" @click="handleLogout" title="Cerrar sesión">
        <i class="pi pi-sign-out" style="font-size: 0.85rem;"></i>
      </button>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuth } from '@/composables/useAuth';

defineProps<{
  isOpen: boolean;
}>();

defineEmits(['close']);

const route = useRoute();
const router = useRouter();
const { user, logout } = useAuth();

const mainNav = [
  { label: 'Dashboard', icon: 'pi pi-home', to: '/dashboard', badge: null },
];

const contentNav = [
  { label: 'Blog', icon: 'pi pi-file-edit', to: '/dashboard/blog', badge: '24' },
  { label: 'Noticias', icon: 'pi pi-megaphone', to: '/dashboard/noticias', badge: '8' },
  { label: 'Publicaciones', icon: 'pi pi-book', to: '/dashboard/publicaciones', badge: null },
  { label: 'Multimedia', icon: 'pi pi-images', to: '/dashboard/multimedia', badge: null },
  { label: 'Instituciones', icon: 'pi pi-building', to: '/dashboard/instituciones', badge: null },
];

const systemNav = [
  { label: 'Usuarios', icon: 'pi pi-users', to: '/dashboard/usuarios', badge: null },
  { label: 'Mensajes', icon: 'pi pi-envelope', to: '/dashboard/mensajes', badge: '3' },
  { label: 'Configuración', icon: 'pi pi-cog', to: '/dashboard/configuracion', badge: null },
];

const isActive = (path: string) => {
  if (path === '/dashboard') {
    return route.path === '/dashboard';
  }
  return route.path.startsWith(path);
};

const userInitials = computed(() => {
  if (!user.value?.fullName) return 'U';
  const parts = user.value.fullName.split(' ');
  return parts.map(p => p[0]).slice(0, 2).join('').toUpperCase();
});

const roleLabel = computed(() => {
  const roles: Record<string, string> = {
    admin: 'Administrador',
    moderator: 'Moderador',
    user: 'Usuario',
  };
  return roles[user.value?.role || 'user'] || 'Usuario';
});

const handleLogout = () => {
  logout();
  router.push('/');
};
</script>
