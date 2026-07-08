<template>
  <div class="min-h-screen bg-white pt-20">
    <PageHero
      :kicker="$t('unfpa_bolivia_page.hero_kicker')"
      :title="$t('unfpa_bolivia_page.hero_title')"
      :subtitle="$t('unfpa_bolivia_page.hero_subtitle')"
      backgroundImage="/img/fondo1.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-3">
        <article v-for="item in focusAreas" :key="item.title" class="rounded-3xl border border-gray-100 bg-white p-7 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
          <div class="mb-5 inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-orange-50 text-[#F97316]">
            <i :class="['pi text-xl', item.icon]"></i>
          </div>
          <h2 class="text-2xl font-bold text-gray-900">{{ $t(item.title) }}</h2>
          <p class="mt-3 leading-relaxed text-gray-600">{{ $t(item.desc) }}</p>
        </article>
      </div>
    </section>

    <section class="bg-[#fff7ed] py-16">
      <div class="mx-auto grid max-w-7xl grid-cols-1 gap-10 px-4 sm:px-6 lg:grid-cols-[1.1fr_0.9fr] lg:px-8">
        <div>
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">{{ $t('unfpa_bolivia_page.priorities_kicker') }}</p>
          <h2 class="mt-3 text-3xl font-extrabold text-gray-900 md:text-4xl">{{ $t('unfpa_bolivia_page.priorities_title') }}</h2>
          <div class="mt-8 space-y-4">
            <article v-for="priority in priorities" :key="priority.title" class="rounded-2xl border border-orange-100 bg-white p-5 shadow-sm">
              <h3 class="text-lg font-bold text-gray-900">{{ $t(priority.title) }}</h3>
              <p class="mt-2 text-gray-600">{{ $t(priority.desc) }}</p>
            </article>
          </div>
        </div>

        <div class="relative overflow-hidden rounded-[2rem] border border-orange-100 bg-white p-5 shadow-xl">
          <img src="/img/fondo2.jpg" :alt="$t('unfpa_bolivia_page.priorities_map_alt')" class="h-full w-full rounded-[1.5rem] object-cover" />
          <div class="mt-5 grid grid-cols-2 gap-4 text-center">
            <div class="rounded-2xl bg-orange-50 p-4">
              <p class="text-sm font-semibold text-gray-500">{{ $t('unfpa_bolivia_page.priorities_focus_label') }}</p>
              <p class="mt-1 text-lg font-bold text-gray-900">{{ $t('unfpa_bolivia_page.priorities_focus_value') }}</p>
            </div>
            <div class="rounded-2xl bg-orange-50 p-4">
              <p class="text-sm font-semibold text-gray-500">{{ $t('unfpa_bolivia_page.priorities_alliance_label') }}</p>
              <p class="mt-1 text-lg font-bold text-gray-900">{{ $t('unfpa_bolivia_page.priorities_alliance_value') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white py-16 border-t border-gray-200">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-12 lg:grid-cols-2">
          <div>
            <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">{{ $t('unfpa_bolivia_page.context_kicker') }}</p>
            <h2 class="mt-3 text-3xl font-extrabold text-gray-900">{{ $t('unfpa_bolivia_page.context_title') }}</h2>
            <p class="mt-4 max-w-2xl text-gray-600 leading-relaxed">
              {{ $t('unfpa_bolivia_page.context_paragraph1') }}
            </p>
            <p class="mt-4 max-w-2xl text-gray-600 leading-relaxed">
              {{ $t('unfpa_bolivia_page.context_paragraph2') }}
            </p>
          </div>
          <div class="bg-orange-50 rounded-[2rem] p-8 ring-1 ring-orange-100">
            <h3 class="text-lg font-bold text-gray-900 mb-6">{{ $t('unfpa_bolivia_page.actors_title') }}</h3>
            <ul class="space-y-4 text-gray-600">
              <li class="flex gap-3">
                <span class="text-[#F97316] font-bold">•</span>
                <span><span v-html="$t('unfpa_bolivia_page.actor_minsalud')"></span></span>
              </li>
              <li class="flex gap-3">
                <span class="text-[#F97316] font-bold">•</span>
                <span><span v-html="$t('unfpa_bolivia_page.actor_sedes')"></span></span>
              </li>
              <li class="flex gap-3">
                <span class="text-[#F97316] font-bold">•</span>
                <span><span v-html="$t('unfpa_bolivia_page.actor_international')"></span></span>
              </li>
              <li class="flex gap-3">
                <span class="text-[#F97316] font-bold">•</span>
                <span><span v-html="$t('unfpa_bolivia_page.actor_social')"></span></span>
              </li>
              <li class="flex gap-3">
                <span class="text-[#F97316] font-bold">•</span>
                <span><span v-html="$t('unfpa_bolivia_page.actor_medical')"></span></span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        <article class="rounded-[2rem] bg-white p-8 shadow-sm ring-1 ring-gray-100">
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">{{ $t('unfpa_bolivia_page.achievements_kicker') }}</p>
          <h2 class="mt-3 text-2xl font-extrabold text-gray-900 mb-6">{{ $t('unfpa_bolivia_page.achievements_title') }}</h2>
          <ul class="space-y-3 text-gray-600">
            <li class="flex gap-3">
              <span class="text-[#F97316] font-bold text-xl leading-none mt-1">✓</span>
              <span>{{ $t('unfpa_bolivia_page.achievement_policy') }}</span>
            </li>
            <li class="flex gap-3">
              <span class="text-[#F97316] font-bold text-xl leading-none mt-1">✓</span>
              <span>{{ $t('unfpa_bolivia_page.achievement_maternity_homes') }}</span>
            </li>
            <li class="flex gap-3">
              <span class="text-[#F97316] font-bold text-xl leading-none mt-1">✓</span>
              <span>{{ $t('unfpa_bolivia_page.achievement_articulation') }}</span>
            </li>
            <li class="flex gap-3">
              <span class="text-[#F97316] font-bold text-xl leading-none mt-1">✓</span>
              <span>{{ $t('unfpa_bolivia_page.achievement_community_awareness') }}</span>
            </li>
            <li class="flex gap-3">
              <span class="text-[#F97316] font-bold text-xl leading-none mt-1">✓</span>
              <span>{{ $t('unfpa_bolivia_page.achievement_indicators') }}</span>
            </li>
          </ul>
        </article>

        <article class="rounded-[2rem] bg-gray-900 p-8 text-white shadow-2xl">
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-orange-300">{{ $t('unfpa_bolivia_page.challenges_kicker') }}</p>
          <h2 class="mt-3 text-2xl font-extrabold md:text-2xl mb-6">{{ $t('unfpa_bolivia_page.challenges_title') }}</h2>
          <ul class="space-y-3">
            <li class="flex gap-3">
              <span class="text-orange-300 font-bold text-xl leading-none mt-1">→</span>
              <span class="text-white/90">{{ $t('unfpa_bolivia_page.challenge_mortality') }}</span>
            </li>
            <li class="flex gap-3">
              <span class="text-orange-300 font-bold text-xl leading-none mt-1">→</span>
              <span class="text-white/90">{{ $t('unfpa_bolivia_page.challenge_coverage') }}</span>
            </li>
            <li class="flex gap-3">
              <span class="text-orange-300 font-bold text-xl leading-none mt-1">→</span>
              <span class="text-white/90">{{ $t('unfpa_bolivia_page.challenge_human_resources') }}</span>
            </li>
            <li class="flex gap-3">
              <span class="text-orange-300 font-bold text-xl leading-none mt-1">→</span>
              <span class="text-white/90">{{ $t('unfpa_bolivia_page.challenge_financial_sustainability') }}</span>
            </li>
            <li class="flex gap-3">
              <span class="text-orange-300 font-bold text-xl leading-none mt-1">→</span>
              <span class="text-white/90">{{ $t('unfpa_bolivia_page.challenge_technology_integration') }}</span>
            </li>
          </ul>
        </article>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8">
      <div class="rounded-[2rem] bg-gray-900 px-8 py-10 text-white shadow-2xl sm:px-10">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-[1.2fr_0.8fr] lg:items-center">
          <div>
            <p class="text-sm font-bold uppercase tracking-[0.2em] text-orange-300">{{ $t('unfpa_bolivia_page.closing_kicker') }}</p>
            <h2 class="mt-3 text-3xl font-extrabold md:text-4xl">{{ $t('unfpa_bolivia_page.closing_title') }}</h2>
            <p class="mt-4 max-w-3xl text-white/80">
              {{ $t('unfpa_bolivia_page.closing_paragraph') }}
            </p>
          </div>

          <div class="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-1">
            <router-link to="/que-hacemos" class="rounded-2xl bg-white/10 px-5 py-4 font-semibold text-white transition-colors hover:bg-white/15">{{ $t('unfpa_bolivia_page.closing_link_explore') }}</router-link>
            <router-link to="/contactanos" class="rounded-2xl bg-[#F97316] px-5 py-4 font-semibold text-white transition-colors hover:bg-[#EA580C]">{{ $t('unfpa_bolivia_page.closing_link_contact') }}</router-link>
          </div>
        </div>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useI18n } from 'vue-i18n';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '@/components/landing/Footer/Footer.vue';

const { t } = useI18n();

const focusAreas = [
  {
    icon: 'pi-heart',
    title: 'unfpa_bolivia_page.focus_area_maternal_title',
    desc: 'unfpa_bolivia_page.focus_area_maternal_desc'
  },
  {
    icon: 'pi-shield',
    title: 'unfpa_bolivia_page.focus_area_violence_title',
    desc: 'unfpa_bolivia_page.focus_area_violence_desc'
  },
  {
    icon: 'pi-sitemap',
    title: 'unfpa_bolivia_page.focus_area_articulated_title',
    desc: 'unfpa_bolivia_page.focus_area_articulated_desc'
  }
];

const priorities = [
  {
    title: 'unfpa_bolivia_page.priority_evidence_title',
    desc: 'unfpa_bolivia_page.priority_evidence_desc'
  },
  {
    title: 'unfpa_bolivia_page.priority_services_title',
    desc: 'unfpa_bolivia_page.priority_services_desc'
  },
  {
    title: 'unfpa_bolivia_page.priority_social_changes_title',
    desc: 'unfpa_bolivia_page.priority_social_changes_desc'
  }
];

onMounted(() => {
  document.title = t('unfpa_bolivia_page.document_title');
  window.scrollTo(0, 0);
});
</script>