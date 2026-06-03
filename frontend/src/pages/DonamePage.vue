<template>
  <div class="min-h-screen bg-white pt-20">
    <PageHero
      kicker="Apoya"
      title="Tu apoyo salva vidas"
      subtitle="Con tu aporte fortalecemos servicios de salud materna, equipamiento neonatal y procesos comunitarios para llegar a quienes mas lo necesitan."
      backgroundImage="/img/hero-doname.jpg"
    />

    <section class="mx-auto max-w-5xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="rounded-3xl border border-orange-100 bg-[#fff7ed] p-8 shadow-sm md:p-10">
        <h2 class="text-3xl font-extrabold text-gray-900">Elige un monto de donacion</h2>
        <div class="mt-6 grid grid-cols-2 gap-4 md:grid-cols-4">
          <button v-for="amount in amounts" :key="amount" class="rounded-2xl bg-white px-4 py-4 font-bold text-[#F97316] shadow-sm transition hover:-translate-y-0.5 hover:shadow-md">{{ amount }}</button>
        </div>
        <a
          href="/contactanos"
          target="_blank"
          rel="noreferrer"
          class="mt-8 block w-full rounded-2xl bg-[#F97316] px-6 py-4 text-center text-lg font-bold text-white transition hover:bg-[#EA580C]"
        >
          Continuar con la donacion
        </a>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '@/components/landing/Footer/Footer.vue';

const amounts = ['Bs. 70', 'Bs. 150', 'Bs. 300', 'Bs. 600'];

onMounted(() => {
  document.title = 'Doname | MNMNS Bolivia';
  window.scrollTo(0, 0);
});
</script>
