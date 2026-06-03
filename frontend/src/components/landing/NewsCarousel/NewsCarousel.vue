<template>
  <section class="py-20 bg-[#F9FAFB]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-end mb-12">
        <div>
          <h2 class="text-3xl font-bold text-gray-800 mb-2">Últimas Noticias</h2>
          <p class="text-gray-600">Avances y testimonios desde el terreno.</p>
        </div>
        <router-link to="/noticias" class="text-[#F97316] hover:text-[#EA580C] font-medium transition-colors hidden sm:block">
          Ver todas las noticias &rarr;
        </router-link>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <article v-for="n in 3" :key="n" class="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-lg transition-all duration-300">
          <div class="h-48 bg-gray-200 w-full object-cover">
            <div class="w-full h-full flex items-center justify-center text-gray-400 bg-orange-50">
               <i class="pi pi-image text-3xl"></i>
            </div>
          </div>
          <div class="p-6">
            <span class="text-xs font-bold text-[#F97316] uppercase tracking-wider">Campaña</span>
            <h3 class="text-xl font-bold text-gray-800 mt-2 mb-3">Nueva sala de atención neonatal inaugurada en El Alto</h3>
            <p class="text-gray-600 text-sm mb-4 line-clamp-3">
              Gracias al esfuerzo conjunto de la Mesa de Maternidad, logramos equipar una nueva sala que beneficiará a cientos de familias...
            </p>
            <router-link to="/noticias" class="text-[#F97316] font-medium text-sm hover:underline">Leer más</router-link>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>