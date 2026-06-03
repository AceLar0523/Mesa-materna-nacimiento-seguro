<template>
  <div>
    <DisplayHeader v-if="!isSidebarPage" :activeItem="activeItem" />
    <Toast position="top-right" />

    <router-view />
    <ChatbotWidget />
  </div>
</template>

<script setup lang="ts">
import DisplayHeader from '@/components/landing/DisplayHeader/DisplayHeader.vue';
import ChatbotWidget from '@/components/common/ChatbotWidget.vue';
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const isSidebarPage = computed(() => {
  return Boolean(route.meta.hideHeader);
});

const activeItem = computed(() => {
  if (route.path === '/') return 'home';
  return null;
});
</script>
