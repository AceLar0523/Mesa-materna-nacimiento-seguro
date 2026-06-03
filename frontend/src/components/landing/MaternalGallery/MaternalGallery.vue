<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
      <div class="max-w-xl text-left">
        <h2 class="text-3xl md:text-4xl font-extrabold text-gray-900 mb-4">El impacto de la MNMNS en el terreno</h2>
        <p class="text-gray-500">Cada fotografía representa una vida salvada y una familia fortalecida en los rincones más profundos de Bolivia.</p>
      </div>
      <router-link to="/blog" class="px-6 py-3 border-2 border-[#F97316] text-[#F97316] font-bold rounded-full hover:bg-[#F97316] hover:text-white transition-all">
        Ver todas las historias
      </router-link>
    </div>

    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 h-[600px]">
      <div class="col-span-2 row-span-2 relative group overflow-hidden rounded-[2.5rem] shadow-lg">
        <img src="https://images.unsplash.com/photo-1584515933487-779824d29309?q=80&w=800" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-8">
          <p class="text-white font-bold">Capacitación médica en el Altiplano</p>
        </div>
      </div>
      <div class="col-span-2 row-span-1 relative group overflow-hidden rounded-[2.5rem] shadow-lg">
        <img src="https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=800" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
      </div>
      <div class="col-span-1 row-span-1 relative group overflow-hidden rounded-[2.5rem] shadow-lg">
        <img src="https://images.unsplash.com/photo-1579154235602-33d5fbf7303f?q=80&w=500" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
      </div>
      <div class="col-span-1 row-span-1 relative group overflow-hidden rounded-[2.5rem] shadow-lg bg-[#F97316] flex flex-col items-center justify-center text-white p-4 text-center">
        <i class="pi pi-heart-fill text-3xl mb-3"></i>
        <p class="font-bold text-sm">Más de 500 kits entregados este mes</p>
      </div>
    </div>
  </div>
</template>