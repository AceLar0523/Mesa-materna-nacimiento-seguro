<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <PageHero
      :kicker="$t('acceso_calidad_servicios_page.hero_kicker')"
      :title="$t('acceso_calidad_servicios_page.hero_title')"
      :subtitle="$t('acceso_calidad_servicios_page.hero_subtitle')"
      backgroundImage="/img/fondo6.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <article class="rounded-3xl border border-gray-100 bg-white p-8 shadow-sm">
        <h2 class="text-2xl font-bold text-gray-900">{{ $t('acceso_calidad_servicios_page.interventions_title') }}</h2>
        <p class="mt-4 leading-relaxed text-gray-600">
          {{ $t('acceso_calidad_servicios_page.interventions_description') }}
        </p>

        <ul class="mt-8 space-y-3 text-gray-700">
          <li><span class="font-bold text-[#F97316]">a.i)</span> {{ $t('acceso_calidad_servicios_page.intervention_ai') }}</li>
          <li><span class="font-bold text-[#F97316]">a.ii)</span> {{ $t('acceso_calidad_servicios_page.intervention_aii') }}</li>
          <li><span class="font-bold text-[#F97316]">a.iii)</span> {{ $t('acceso_calidad_servicios_page.intervention_aiii') }}</li>
          <li><span class="font-bold text-[#F97316]">a.iv)</span> {{ $t('acceso_calidad_servicios_page.intervention_aiv') }}</li>
          <li><span class="font-bold text-[#F97316]">b)</span> {{ $t('acceso_calidad_servicios_page.intervention_b') }}</li>
          <li><span class="font-bold text-[#F97316]">c)</span> {{ $t('acceso_calidad_servicios_page.intervention_c') }}</li>
          <li><span class="font-bold text-[#F97316]">d)</span> {{ $t('acceso_calidad_servicios_page.intervention_d') }}</li>
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
import { useI18n } from 'vue-i18n'; // Import useI18n

const { t } = useI18n(); // Initialize useI18n

onMounted(() => {
  document.title = t('acceso_calidad_servicios_page.document_title');
  window.scrollTo(0, 0);
});
</script>