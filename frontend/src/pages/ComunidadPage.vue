<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <PageHero
      :kicker="$t('comunidad_page.kicker')"
      :title="$t('comunidad_page.title')"
      :subtitle="$t('comunidad_page.subtitle')"
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
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const items = [
  { title: t('comunidad_page.item_blog_title'), to: '/blog', icon: 'pi-pencil', desc: t('comunidad_page.item_blog_desc') },
  { title: t('comunidad_page.item_news_title'), to: '/noticias', icon: 'pi-megaphone', desc: t('comunidad_page.item_news_desc') },
  { title: t('comunidad_page.item_publications_title'), to: '/comunidad/publicaciones', icon: 'pi-file', desc: t('comunidad_page.item_publications_desc') },
  { title: t('comunidad_page.item_campaigns_title'), to: '/comunidad/campanas', icon: 'pi-bullhorn', desc: t('comunidad_page.item_campaigns_desc') },
  { title: t('comunidad_page.item_multimedia_title'), to: '/comunidad/multimedia', icon: 'pi-video', desc: t('comunidad_page.item_multimedia_desc') },
  { title: t('comunidad_page.item_institutions_title'), to: '/instituciones', icon: 'pi-building', desc: t('comunidad_page.item_institutions_desc') }
];

onMounted(() => {
  document.title = t('comunidad_page.doc_title_prefix') + ' | MNMNS Bolivia';
  window.scrollTo(0, 0);
});
</script>