<template>
  <div class="min-h-screen bg-white pt-20">
    <PageHero
      kicker="Comunidad"
      title="Campañas"
      subtitle="Movilizacion social para prevenir violencia, embarazos no intencionales y muertes maternas evitables."
      backgroundImage="/img/fondo12.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        <article v-for="item in campaigns" :key="item.title" class="rounded-3xl border border-orange-100 bg-white p-7 shadow-sm">
          <div class="mb-4 inline-flex rounded-full bg-orange-50 px-3 py-1 text-xs font-bold uppercase tracking-wider text-[#F97316]">Campaña activa</div>
          <h3 class="text-2xl font-bold text-gray-900">{{ item.title }}</h3>
          <p class="mt-3 text-gray-600">{{ item.desc }}</p>
          <div class="mt-6 flex gap-3">
            <button class="rounded-full bg-[#F97316] px-4 py-2 text-sm font-semibold text-white">Participar</button>
            <button class="rounded-full border border-orange-200 px-4 py-2 text-sm font-semibold text-[#F97316]">Conocer mas</button>
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

const campaigns = [
  { title: 'Mi parto, mis derechos', desc: 'Informacion comunitaria para promover atencion respetuosa y segura durante embarazo y parto.' },
  { title: 'Juventudes con autonomia', desc: 'Acciones educomunicativas para fortalecer decisiones informadas en salud sexual y reproductiva.' }
];

onMounted(() => {
  document.title = 'Campanas | MNMNS';
  window.scrollTo(0, 0);
});
</script>
