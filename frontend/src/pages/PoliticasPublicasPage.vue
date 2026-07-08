<template>
  <div class="min-h-screen bg-white pt-20">
    <PageHero
      :kicker="$t('politicas_publicas_page.que_hacemos')"
      :title="$t('politicas_publicas_page.politicas_publicas_title')"
      :subtitle="$t('politicas_publicas_page.subtitle_producto1')"
      backgroundImage="/img/fondo5.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <article class="rounded-3xl border border-gray-100 bg-white p-8 shadow-sm">
        <h2 class="text-2xl font-bold text-gray-900">{{ $t('politicas_publicas_page.intervenciones_estrategicas_title') }}</h2>
        <p class="mt-4 leading-relaxed text-gray-600">
          {{ $t('politicas_publicas_page.parrafo1_estrategico') }}
        </p>
        <p class="mt-4 leading-relaxed text-gray-600">
          {{ $t('politicas_publicas_page.parrafo2_monitoreo') }}
        </p>

        <ul class="mt-8 space-y-3 text-gray-700">
          <li><span class="font-bold text-[#F97316]">a)</span> {{ $t('politicas_publicas_page.punto_a') }}</li>
          <li><span class="font-bold text-[#F97316]">b)</span> {{ $t('politicas_publicas_page.punto_b') }}</li>
          <li><span class="font-bold text-[#F97316]">c)</span> {{ $t('politicas_publicas_page.punto_c') }}</li>
          <li><span class="font-bold text-[#F97316]">d)</span> {{ $t('politicas_publicas_page.punto_d') }}</li>
          <li><span class="font-bold text-[#F97316]">e)</span> {{ $t('politicas_publicas_page.punto_e') }}</li>
          <li><span class="font-bold text-[#F97316]">f)</span> {{ $t('politicas_publicas_page.punto_f') }}</li>
          <li><span class="font-bold text-[#F97316]">g)</span> {{ $t('politicas_publicas_page.punto_g') }}</li>
        </ul>
      </article>
    </section>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '@/components/landing/Footer/Footer.vue';
import { useI18n } from 'vue-i18n'; // Se añadió para usar la función 't'

const { t } = useI18n(); // Se añadió para obtener la función 't'

onMounted(() => {
  document.title = t('politicas_publicas_page.document_title');
  window.scrollTo(0, 0);
});
</script>