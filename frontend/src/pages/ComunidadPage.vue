<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <PageHero
      kicker="Comunidad"
      title="Comunidad"
      subtitle="Un espacio para conversar, aprender y movilizar accion colectiva por la salud sexual y reproductiva."
      backgroundImage="/img/hero-comunidad.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
        <router-link v-for="item in items" :key="item.to" :to="item.to" class="group rounded-3xl border border-gray-100 bg-white p-7 shadow-sm transition-all hover:-translate-y-1 hover:shadow-xl">
          <div class="mb-4 inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-orange-50 text-[#F97316]">
            <i :class="['pi text-xl', item.icon]"></i>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 group-hover:text-[#F97316]">{{ item.title }}</h3>
          <p class="mt-3 text-gray-600">{{ item.desc }}</p>
        </router-link>
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
  { title: 'Blog', to: '/blog', icon: 'pi-pencil', desc: 'Historias, reflexiones y recomendaciones de especialistas y comunidad.' },
  { title: 'Ultimas Noticias', to: '/noticias', icon: 'pi-megaphone', desc: 'Actualizaciones institucionales, avances y articulacion con aliados.' },
  { title: 'Publicaciones', to: '/comunidad/publicaciones', icon: 'pi-file', desc: 'Documentos tecnicos, guias y material de consulta publica.' },
  { title: 'Campanas', to: '/comunidad/campanas', icon: 'pi-bullhorn', desc: 'Iniciativas de sensibilizacion para promover derechos y prevencion.' },
  { title: 'Multimedia', to: '/comunidad/multimedia', icon: 'pi-video', desc: 'Videos, galerias y piezas visuales para educacion comunitaria.' },
  { title: 'Instituciones', to: '/instituciones', icon: 'pi-building', desc: 'Conoce la red interinstitucional que hace posible esta agenda.' }
];

onMounted(() => {
  document.title = 'Comunidad | MNMNS Bolivia';
  window.scrollTo(0, 0);
});
</script>
