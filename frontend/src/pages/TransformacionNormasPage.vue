<template>
  <div class="min-h-screen bg-white pt-20">
    <PageHero
      :kicker="$t('transformacion_normas_page.kicker')"
      :title="$t('transformacion_normas_page.title')"
      :subtitle="$t('transformacion_normas_page.subtitle')"
      backgroundImage="/img/fondo7.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <article class="rounded-3xl border border-gray-100 bg-white p-8 shadow-sm">
        <h2 class="text-2xl font-bold text-gray-900">{{ $t('transformacion_normas_page.intervenciones_estrategicas_title') }}</h2>
        <p class="mt-4 leading-relaxed text-gray-600">
          {{ $t('transformacion_normas_page.descripcion_producto') }}
        </p>

        <ul class="mt-8 space-y-3 text-gray-700">
          <li><span class="font-bold text-[#F97316]">a)</span> {{ $t('transformacion_normas_page.punto_a') }}</li>
          <li><span class="font-bold text-[#F97316]">b)</span> {{ $t('transformacion_normas_page.punto_b') }}</li>
          <li><span class="font-bold text-[#F97316]">c)</span> {{ $t('transformacion_normas_page.punto_c') }}</li>
          <li><span class="font-bold text-[#F97316]">d)</span> {{ $t('transformacion_normas_page.punto_d') }}</li>
          <li><span class="font-bold text-[#F97316]">e)</span> {{ $t('transformacion_normas_page.punto_e') }}</li>
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
import { useI18n } from 'vue-i18n'; // Import useI18n for script setup translations

const { t } = useI18n(); // Initialize useI18n

onMounted(() => {
  document.title = t('transformacion_normas_page.document_title');
  window.scrollTo(0, 0);
});
</script>