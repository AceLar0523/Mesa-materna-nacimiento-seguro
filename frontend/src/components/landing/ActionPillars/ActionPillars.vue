<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16">
      <h2 class="text-sm font-bold text-[#F97316] uppercase tracking-[0.2em] mb-3">Nuestra Misión</h2>
      <p class="text-3xl md:text-4xl font-extrabold text-gray-900">¿Cómo transformamos la maternidad?</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div v-for="(pillar, i) in pillars" :key="i" 
           class="bg-white p-10 rounded-[2rem] border border-gray-100 shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-500 group">
        <div class="w-16 h-16 bg-orange-50 text-[#F97316] rounded-2xl flex items-center justify-center mb-6 group-hover:bg-[#F97316] group-hover:text-white transition-colors duration-500">
          <i :class="['pi text-2xl', pillar.icon]"></i>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-4">{{ pillar.title }}</h3>
        <p class="text-gray-500 leading-relaxed">{{ pillar.desc }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
const pillars = [
  { icon: 'pi-box', title: 'Equipamiento Crítico', desc: 'Dotamos a centros de salud rurales con kits de parto limpio y equipos de reanimación neonatal.' },
  { icon: 'pi-home', title: 'Casas Maternas', desc: 'Espacios de acogida para mujeres de comunidades alejadas, garantizando cercanía al hospital antes del parto.' },
  { icon: 'pi-users', title: 'Enfoque Intercultural', desc: 'Articulamos el saber de las parteras tradicionales con la medicina académica bajo la política SAFCI.' }
];
</script>