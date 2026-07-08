<template>
  <div class="min-h-screen bg-white pt-20">
    <PageHero
      :kicker="$t('campanas_page.kicker_comunidad')"
      :title="$t('campanas_page.title_campanas')"
      :subtitle="$t('campanas_page.subtitle_descripcion')"
      backgroundImage="/img/fondo12.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        <article v-for="item in campaigns" :key="item.title" class="rounded-3xl border border-orange-100 bg-white p-7 shadow-sm">
          <div class="mb-4 inline-flex rounded-full bg-orange-50 px-3 py-1 text-xs font-bold uppercase tracking-wider text-[#F97316]">{{ $t('campanas_page.campana_activa_tag') }}</div>
          <h3 class="text-2xl font-bold text-gray-900">{{ item.title }}</h3>
          <p class="mt-3 text-gray-600">{{ item.desc }}</p>
          <div class="mt-6 flex gap-3">
            <button class="rounded-full bg-[#F97316] px-4 py-2 text-sm font-semibold text-white">{{ $t('campanas_page.btn_participar') }}</button>
            <button class="rounded-full border border-orange-200 px-4 py-2 text-sm font-semibold text-[#F97316]">{{ $t('campanas_page.btn_conocer_mas') }}</button>
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
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const campaigns = [
  { title: t('campanas_page.campaign_parto_title'), desc: t('campanas_page.campaign_parto_desc') },
  { title: t('campanas_page.campaign_juventudes_title'), desc: t('campanas_page.campaign_juventudes_desc') }
];

onMounted(() => {
  document.title = t('campanas_page.document_title_prefix') + ' | MNMNS';
  window.scrollTo(0, 0);
});
</script>