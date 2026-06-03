<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <PageHero
      kicker="Comunidad"
      title="Publicaciones"
      subtitle="Repositorio de documentos para consulta tecnica y ciudadana."
      backgroundImage="/img/fondo11.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
        <article v-for="item in items" :key="item.title" class="rounded-2xl border border-gray-100 bg-white p-6 shadow-sm transition-all hover:-translate-y-1 hover:shadow-lg">
          <img :src="item.image" :alt="item.title" class="h-36 w-full rounded-xl object-cover" />
          <h3 class="mt-4 text-xl font-bold text-gray-900">{{ item.title }}</h3>
          <p class="mt-2 text-sm text-gray-600">{{ item.desc }}</p>
          <button class="mt-5 rounded-full bg-orange-50 px-4 py-2 text-sm font-semibold text-[#F97316] transition-colors hover:bg-orange-100">Ver documento</button>
        </article>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '@/components/landing/Footer/Footer.vue';

const items = [
  { title: 'Informe anual de resultados', desc: 'Evidencia de avances en politicas, servicios y transformacion social.', image: '/img/fondo7.jpg' },
  { title: 'Guia tecnica de atencion integral', desc: 'Lineamientos para equipos de salud con enfoque de derechos.', image: '/img/fondo8.jpg' },
  { title: 'Boletin de indicadores SSR', desc: 'Seguimiento trimestral de cobertura, acceso y calidad.', image: '/img/fondo9.jpg' }
];

onMounted(() => {
  document.title = 'Publicaciones | MNMNS';
  window.scrollTo(0, 0);
});
</script>
