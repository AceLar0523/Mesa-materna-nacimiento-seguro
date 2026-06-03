<template>
  <div class="relative pt-32 pb-20 sm:pt-48 sm:pb-32 overflow-hidden flex flex-col items-center justify-center min-h-[80vh]">
    
    <div class="absolute inset-0 z-0 opacity-30 pointer-events-none">
       <PlasmaWaveV2 :yOffset="0" :xOffset="40" :rotationDeg="-45" />
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      
      <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-orange-50/80 backdrop-blur-sm text-[#F97316] text-sm font-semibold mb-8 border border-[#991a73]/15 shadow-sm">
        <span class="relative flex h-3 w-3">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#991a73] opacity-60"></span>
          <span class="relative inline-flex rounded-full h-3 w-3 bg-[#991a73]"></span>
        </span>
        Trabajando por la niñez en Bolivia
      </div>

      <h1 class="text-5xl md:text-7xl font-extrabold tracking-tight mb-6 text-gray-900 drop-shadow-sm">
        Mesa de Maternidad y <br class="hidden md:block" />
        <span class="text-[#F97316]">Nacimiento Seguros</span>
      </h1>
      
      <p class="mt-4 max-w-2xl mx-auto text-xl text-gray-700 font-medium mb-10 leading-relaxed drop-shadow-sm">
        Garantizamos que cada madre y bebé reciban la atención, el respeto y el equipamiento médico que merecen durante el embarazo y el parto.
      </p>  
      
      <div class="flex flex-col sm:flex-row justify-center gap-4">
        <router-link to="/conocenos" class="px-8 py-4 rounded-full bg-[#F97316] text-white font-bold text-lg hover:bg-[#EA580C] transition-all shadow-lg hover:shadow-xl hover:-translate-y-1">
          Conoce nuestro impacto
        </router-link>
        <router-link to="/datos" class="px-8 py-4 rounded-full bg-white/90 backdrop-blur-sm text-[#991a73] font-bold text-lg border-2 border-[#991a73] hover:bg-gray-50 transition-all shadow-sm">
          Ver Datos Oficiales
        </router-link>
      </div>
      
    </div>
  </div>
</template>

<script setup lang="ts">
// Importamos la animación original del template
import PlasmaWaveV2 from '../PlasmaWave/PlasmaWaveV2.vue';
</script>