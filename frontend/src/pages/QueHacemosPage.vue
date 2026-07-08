<template>
  <div class="min-h-screen bg-[#fffaf5] pt-20">
    <PageHero
      :kicker="$t('que_hacemos_page.hero_kicker')"
      :title="$t('que_hacemos_page.hero_title')"
      :subtitle="$t('que_hacemos_page.hero_subtitle')"
      backgroundImage="/img/hero-que-hacemos.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        <router-link to="/que-hacemos/politicas-publicas-rendicion-cuentas" class="group rounded-3xl border border-orange-100 bg-white p-7 shadow-sm transition-all hover:-translate-y-1 hover:shadow-xl">
          <p class="text-xs font-bold uppercase tracking-widest text-[#F97316]">{{ $t('que_hacemos_page.product1_kicker') }}</p>
          <h3 class="mt-3 text-2xl font-bold text-gray-900 group-hover:text-[#F97316]">{{ $t('que_hacemos_page.product1_title') }}</h3>
          <p class="mt-3 text-gray-600">{{ $t('que_hacemos_page.product1_description') }}</p>
        </router-link>

        <router-link to="/que-hacemos/acceso-calidad-servicios-atencion" class="group rounded-3xl border border-orange-100 bg-white p-7 shadow-sm transition-all hover:-translate-y-1 hover:shadow-xl">
          <p class="text-xs font-bold uppercase tracking-widest text-[#F97316]">{{ $t('que_hacemos_page.product2_kicker') }}</p>
          <h3 class="mt-3 text-2xl font-bold text-gray-900 group-hover:text-[#F97316]">{{ $t('que_hacemos_page.product2_title') }}</h3>
          <p class="mt-3 text-gray-600">{{ $t('que_hacemos_page.product2_description') }}</p>
        </router-link>

        <router-link to="/que-hacemos/transformacion-normas-sociales-genero" class="group rounded-3xl border border-orange-100 bg-white p-7 shadow-sm transition-all hover:-translate-y-1 hover:shadow-xl">
          <p class="text-xs font-bold uppercase tracking-widest text-[#F97316]">{{ $t('que_hacemos_page.product3_kicker') }}</p>
          <h3 class="mt-3 text-2xl font-bold text-gray-900 group-hover:text-[#F97316]">{{ $t('que_hacemos_page.product3_title') }}</h3>
          <p class="mt-3 text-gray-600">{{ $t('que_hacemos_page.product3_description') }}</p>
        </router-link>

        <router-link to="/datos" class="group rounded-3xl border border-orange-100 bg-white p-7 shadow-sm transition-all hover:-translate-y-1 hover:shadow-xl">
          <p class="text-xs font-bold uppercase tracking-widest text-[#F97316]">{{ $t('que_hacemos_page.monitoring_kicker') }}</p>
          <h3 class="mt-3 text-2xl font-bold text-gray-900 group-hover:text-[#F97316]">{{ $t('que_hacemos_page.data_title') }}</h3>
          <p class="mt-3 text-gray-600">{{ $t('que_hacemos_page.data_description') }}</p>
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

onMounted(() => {
  document.title = 'Que hacemos | MNMNS Bolivia'; // This is a script string, not covered by the prompt's rules for replacement.
  window.scrollTo(0, 0);
});
</script>