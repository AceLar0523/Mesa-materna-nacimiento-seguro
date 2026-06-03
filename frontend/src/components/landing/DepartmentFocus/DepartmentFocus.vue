<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
      <div class="space-y-8">
        <h2 class="text-4xl font-extrabold text-gray-900">Presencia en toda la Red de Salud</h2>
        <p class="text-lg text-gray-600 leading-relaxed">
          Nuestra labor no se detiene en las ciudades. La Mesa de Maternidad llega a los municipios más vulnerables de Bolivia, priorizando zonas con alta tasa de mortalidad materna.
        </p>
        
        <div class="space-y-4">
          <div v-for="dept in depts" :key="dept.name" class="flex items-center gap-4 bg-white p-4 rounded-2xl shadow-sm border-l-4 border-[#F97316]">
            <span class="font-bold text-gray-800 w-24">{{ dept.name }}</span>
            <div class="flex-1 h-2 bg-gray-100 rounded-full overflow-hidden">
              <div class="h-full bg-[#F97316] rounded-full" :style="{ width: dept.perc + '%' }"></div>
            </div>
            <span class="text-xs font-bold text-[#F97316]">{{ dept.perc }}% cobertura</span>
          </div>
        </div>
      </div>

      <div class="relative">
        <div class="absolute -top-10 -right-10 w-64 h-64 bg-[#F97316]/10 rounded-full blur-3xl"></div>
        <div class="bg-white p-4 rounded-[3rem] shadow-2xl relative z-10 rotate-3 group hover:rotate-0 transition-transform duration-500">
          <img src="https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?q=80&w=800" class="rounded-[2.5rem] w-full object-cover" alt="Compromiso Institucional" />
          <div class="absolute -bottom-6 -left-6 bg-[#00833D] text-white p-6 rounded-3xl shadow-xl">
             <p class="text-2xl font-black">100%</p>
             <p class="text-xs font-bold uppercase tracking-wider">Compromiso Institucional</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Datos de cobertura por departamento (Puedes actualizar estos porcentajes luego)
const depts = [
  { name: 'Potosí', perc: 85 },
  { name: 'El Alto', perc: 92 },
  { name: 'Beni', perc: 64 },
  { name: 'Chuquisaca', perc: 78 }
];
</script>