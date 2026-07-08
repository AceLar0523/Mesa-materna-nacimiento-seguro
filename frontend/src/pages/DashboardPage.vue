<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
    <!-- Header -->
    <header class="sticky top-0 z-40 border-b border-gray-200 bg-white/95 backdrop-blur-sm">
      <div class="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
        <div>
          <h1 class="text-2xl font-bold bg-gradient-to-r from-[#F97316] to-[#991a73] bg-clip-text text-transparent">
            {{ $t('dashboard_page.dashboard_title') }}
          </h1>
          <p class="text-sm text-gray-500">{{ $t('dashboard_page.welcome_greeting') }} {{ user?.fullName }}</p>
        </div>
        <button
          @click="handleLogout"
          class="inline-flex items-center gap-2 rounded-full bg-red-50 px-4 py-2 text-sm font-semibold text-red-600 transition-colors hover:bg-red-100"
        >
          <i class="pi pi-sign-out"></i>
          {{ $t('dashboard_page.logout_button') }}
        </button>
      </div>
    </header>

    <!-- Main Content -->
    <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
      <!-- Welcome Card -->
      <div class="mb-8 rounded-2xl border border-orange-100 bg-gradient-to-r from-[#F97316]/10 to-[#991a73]/10 p-8">
        <h2 class="mb-2 text-2xl font-bold text-gray-900">{{ $t('dashboard_page.welcome_panel_title') }}</h2>
        <p class="text-gray-600">
          {{ $t('dashboard_page.welcome_panel_description') }}
        </p>
      </div>

      <!-- Stats Grid -->
      <div class="mb-8 grid grid-cols-1 gap-4 md:grid-cols-4">
        <div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-500">{{ $t('dashboard_page.blog_posts_stat') }}</p>
              <p class="mt-2 text-3xl font-bold text-gray-900">24</p>
            </div>
            <div class="rounded-lg bg-orange-100 p-3">
              <i class="pi pi-file-edit text-2xl text-[#F97316]"></i>
            </div>
          </div>
        </div>

        <div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-500">{{ $t('dashboard_page.messages_stat') }}</p>
              <p class="mt-2 text-3xl font-bold text-gray-900">12</p>
            </div>
            <div class="rounded-lg bg-blue-100 p-3">
              <i class="pi pi-envelope text-2xl text-blue-600"></i>
            </div>
          </div>
        </div>

        <div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-500">{{ $t('dashboard_page.users_stat') }}</p>
              <p class="mt-2 text-3xl font-bold text-gray-900">156</p>
            </div>
            <div class="rounded-lg bg-purple-100 p-3">
              <i class="pi pi-users text-2xl text-purple-600"></i>
            </div>
          </div>
        </div>

        <div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-500">{{ $t('dashboard_page.visits_stat') }}</p>
              <p class="mt-2 text-3xl font-bold text-gray-900">1.2k</p>
            </div>
            <div class="rounded-lg bg-green-100 p-3">
              <i class="pi pi-chart-line text-2xl text-green-600"></i>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Actions -->
      <div class="rounded-2xl border border-gray-200 bg-white p-8">
        <h3 class="mb-6 text-lg font-bold text-gray-900">{{ $t('dashboard_page.quick_actions_title') }}</h3>
        <div class="grid grid-cols-1 gap-4 md:grid-cols-3">
          <router-link
            to="/"
            class="rounded-xl border-2 border-[#F97316] bg-orange-50 p-6 text-center transition-all hover:shadow-lg"
          >
            <i class="pi pi-pencil mb-3 block text-3xl text-[#F97316]"></i>
            <span class="font-semibold text-gray-900">{{ $t('dashboard_page.create_post_action') }}</span>
          </router-link>

          <router-link
            to="/"
            class="rounded-xl border-2 border-[#991a73] bg-pink-50 p-6 text-center transition-all hover:shadow-lg"
          >
            <i class="pi pi-file mb-3 block text-3xl text-[#991a73]"></i>
            <span class="font-semibold text-gray-900">{{ $t('dashboard_page.view_blog_action') }}</span>
          </router-link>

          <router-link
            to="/"
            class="rounded-xl border-2 border-blue-500 bg-blue-50 p-6 text-center transition-all hover:shadow-lg"
          >
            <i class="pi pi-envelope mb-3 block text-3xl text-blue-500"></i>
            <span class="font-semibold text-gray-900">{{ $t('dashboard_page.messages_action') }}</span>
          </router-link>
        </div>
      </div>

      <!-- Info -->
      <div class="mt-8 rounded-xl border-2 border-dashed border-gray-300 bg-gray-50 p-6 text-center">
        <i class="pi pi-info-circle mb-3 block text-2xl text-[#F97316]"></i>
        <p class="font-semibold text-gray-900">{{ $t('dashboard_page.dashboard_in_progress_title') }}</p>
        <p class="mt-2 text-sm text-gray-600">
          {{ $t('dashboard_page.dashboard_in_progress_description') }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuth } from '@/composables/useAuth';

const router = useRouter();
const { user, logout, isAuthenticated } = useAuth();

// Proteger la ruta - redirigir si no está autenticado
onMounted(() => {
  if (!isAuthenticated.value) {
    router.push('/login');
  }
});

const handleLogout = () => {
  logout();
  router.push('/');
};
</script>