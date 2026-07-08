<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <PageHero
      :kicker="$t('multimedia_page.hero_kicker')"
      :title="$t('multimedia_page.hero_title')"
      :subtitle="$t('multimedia_page.hero_subtitle')"
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
            <img :src="card.image" :alt="$t(card.title)" class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/55 via-black/10 to-transparent"></div>
            <div class="absolute bottom-4 left-4 right-4 flex items-end justify-between gap-3">
              <span class="rounded-full bg-white/90 px-3 py-1 text-xs font-bold uppercase tracking-wide text-gray-900 backdrop-blur">{{ $t(card.tag) }}</span>
              <span class="rounded-full bg-[#F97316] px-3 py-1 text-xs font-bold uppercase tracking-wide text-white">{{ $t(card.type) }}</span>
            </div>
          </div>
          <div class="p-5">
            <h3 class="text-xl font-bold text-gray-900 group-hover:text-[#F97316]">{{ $t(card.title) }}</h3>
            <p class="mt-2 text-sm leading-relaxed text-gray-600">{{ $t(card.desc) }}</p>
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
  { title: 'multimedia_page.item1_title', desc: 'multimedia_page.item1_desc', image: '/img/fondo1.jpg', tag: 'multimedia_page.item1_tag', type: 'multimedia_page.item1_type' },
  { title: 'multimedia_page.item2_title', desc: 'multimedia_page.item2_desc', image: '/img/fondo2.jpg', tag: 'multimedia_page.item2_tag', type: 'multimedia_page.item2_type' },
  { title: 'multimedia_page.item3_title', desc: 'multimedia_page.item3_desc', image: '/img/fondo3.png', tag: 'multimedia_page.item3_tag', type: 'multimedia_page.item3_type' },
  { title: 'multimedia_page.item4_title', desc: 'multimedia_page.item4_desc', image: '/img/fondo4.jpg', tag: 'multimedia_page.item4_tag', type: 'multimedia_page.item4_type' },
  { title: 'multimedia_page.item5_title', desc: 'multimedia_page.item5_desc', image: '/img/fondo5.jpg', tag: 'multimedia_page.item5_tag', type: 'multimedia_page.item5_type' },
  { title: 'multimedia_page.item6_title', desc: 'multimedia_page.item6_desc', image: '/img/fondo6.jpg', tag: 'multimedia_page.item6_tag', type: 'multimedia_page.item6_type' }
];

onMounted(() => {
  document.title = $t('multimedia_page.document_title') + ' | MNMNS';
  window.scrollTo(0, 0);
});
</script>