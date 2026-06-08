<template>
  <div class="admin-layout">
    <AdminSidebar :is-open="isSidebarOpen" @close="isSidebarOpen = false" />

    <div class="admin-main">
      <AdminTopbar @toggle-sidebar="isSidebarOpen = !isSidebarOpen" />

      <main class="admin-content">
        <router-view v-slot="{ Component }">
          <transition name="admin-page" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuth } from '@/composables/useAuth';
import AdminSidebar from '@/components/navs/AdminSidebar.vue';
import AdminTopbar from '@/components/navs/AdminTopbar.vue';

const router = useRouter();
const { isAuthenticated, initAuth } = useAuth();
const isSidebarOpen = ref(false);

onMounted(() => {
  initAuth();
  if (!isAuthenticated.value) {
    router.push('/login');
  }
});
</script>

<style scoped>
.admin-page-enter-active,
.admin-page-leave-active {
  transition: all 0.25s ease;
}

.admin-page-enter-from {
  opacity: 0;
  transform: translateY(8px);
}

.admin-page-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>
