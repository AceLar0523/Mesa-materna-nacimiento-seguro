<template>
  <div>
    <DisplayHeader v-if="!isAdminPage" :activeItem="activeItem" />
    <Toast position="top-right" />

    <router-view />
    <ChatbotWidget v-if="!isAdminPage" />
  </div>
</template>

<script setup lang="ts">
import DisplayHeader from '@/components/landing/DisplayHeader/DisplayHeader.vue';
import ChatbotWidget from '@/components/common/ChatbotWidget.vue';
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const isAdminPage = computed(() => {
  // Check both direct meta and parent route meta for nested routes
  return route.matched.some(record => record.meta.hideHeader);
});

const activeItem = computed(() => {
  if (route.path === '/') return 'home';
  return null;
});
</script>

