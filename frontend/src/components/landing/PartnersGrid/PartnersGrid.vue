<template>
  <section class="py-16 bg-white border-t border-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <h2 class="text-sm font-bold text-gray-400 uppercase tracking-widest mb-8">
        Instituciones que hacen esto posible
      </h2>
      
      <div class="flex flex-wrap justify-center items-center gap-12 opacity-60 grayscale hover:grayscale-0 transition-all duration-500">
        <div v-for="i in 5" :key="i" class="w-32 h-16 bg-gray-100 rounded flex items-center justify-center">
          <span class="text-gray-400 font-medium text-sm">Logo Aliado {{ i }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>