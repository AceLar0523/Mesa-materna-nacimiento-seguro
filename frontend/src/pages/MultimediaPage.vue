<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <PageHero
      kicker="Comunidad"
      title="Multimedia"
      subtitle="Galeria de recursos audiovisuales para difusion, formacion y sensibilizacion comunitaria."
      backgroundImage="/img/fondo12.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
        <article
          v-for="card in media"
          :key="card.title"
          class="group overflow-hidden rounded-3xl border border-gray-100 bg-white shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
        >
          <div class="relative h-56 overflow-hidden">
            <img :src="card.image" :alt="card.title" class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/55 via-black/10 to-transparent"></div>
            <div class="absolute bottom-4 left-4 right-4 flex items-end justify-between gap-3">
              <span class="rounded-full bg-white/90 px-3 py-1 text-xs font-bold uppercase tracking-wide text-gray-900 backdrop-blur">{{ card.tag }}</span>
              <span class="rounded-full bg-[#F97316] px-3 py-1 text-xs font-bold uppercase tracking-wide text-white">{{ card.type }}</span>
            </div>
          </div>
          <div class="p-5">
            <h3 class="text-xl font-bold text-gray-900 group-hover:text-[#F97316]">{{ card.title }}</h3>
            <p class="mt-2 text-sm leading-relaxed text-gray-600">{{ card.desc }}</p>
          </div>
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

const media = [
  { title: 'Video institucional', desc: 'Resumen de trabajo en territorios priorizados.', image: '/img/fondo1.jpg', tag: 'Video', type: 'Destacado' },
  { title: 'Serie fotográfica', desc: 'Historias visuales desde centros de salud y comunidades.', image: '/img/fondo2.jpg', tag: 'Galería', type: 'Territorio' },
  { title: 'Cápsulas educativas', desc: 'Material corto para redes y procesos de formación.', image: '/img/fondo3.png', tag: 'Educación', type: 'RRSS' },
  { title: 'Talleres comunitarios', desc: 'Encuentros de intercambio con familias, personal de salud y líderes locales.', image: '/img/fondo4.jpg', tag: 'Taller', type: 'Comunidad' },
  { title: 'Testimonios', desc: 'Relatos en primera persona sobre acompañamiento y atención oportuna.', image: '/img/fondo5.jpg', tag: 'Voces', type: 'Historias' },
  { title: 'Cobertura en campo', desc: 'Registros visuales de actividades en municipios priorizados.', image: '/img/fondo6.jpg', tag: 'Cobertura', type: 'Campo' }
];

onMounted(() => {
  document.title = 'Multimedia | MNMNS';
  window.scrollTo(0, 0);
});
</script>
