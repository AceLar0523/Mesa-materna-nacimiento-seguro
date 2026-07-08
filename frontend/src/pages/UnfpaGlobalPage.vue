<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <PageHero
      :kicker="$t('unfpa_global_page.nuestra_labor')"
      :title="$t('unfpa_global_page.mnmns_cooperacion_internacional')"
      :subtitle="$t('unfpa_global_page.mnmns_opera_plataformas')"
      backgroundImage="/img/fondo4.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-10 lg:grid-cols-[1.05fr_0.95fr]">
        <div>
          <p class="mt-4 max-w-4xl text-gray-600 leading-relaxed">
            {{ $t('unfpa_global_page.mnmns_cooperacion_internacional_impacto') }}
          </p>
          <p class="mt-4 max-w-4xl text-gray-600 leading-relaxed">
            {{ $t('unfpa_global_page.trabajo_global_reducir_desigualdades') }}
          </p>

          <div class="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-3">
            <div v-for="item in commitments" :key="item.title" class="rounded-2xl bg-gray-50 p-5 shadow-sm ring-1 ring-gray-100">
              <p class="text-sm font-semibold text-gray-500">{{ item.title }}</p>
              <p class="mt-2 text-sm text-gray-600">{{ item.desc }}</p>
            </div>
          </div>
        </div>

        <div class="relative">
          <div class="rounded-[2rem] border border-orange-100 bg-[#fff7ed] p-5 shadow-2xl">
            <img src="/img/fondo5.jpg" alt="MNMNS Global" class="w-full rounded-[1.5rem] bg-white p-4 shadow-sm" />
          </div>
          <div class="absolute -bottom-5 right-6 rounded-2xl bg-[#F97316] px-5 py-4 text-white shadow-xl">
            <p class="text-xs font-bold uppercase tracking-[0.2em] text-orange-100">{{ $t('unfpa_global_page.card_global_kicker') }}</p>
            <p class="mt-1 text-lg font-bold">{{ $t('unfpa_global_page.card_global_title') }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-3">
        <article v-for="item in results" :key="item.title" class="rounded-3xl border border-gray-100 bg-white p-7 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
          <div class="mb-5 inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-orange-50 text-[#F97316]">
            <i :class="['pi text-xl', item.icon]"></i>
          </div>
          <h2 class="text-2xl font-bold text-gray-900">{{ item.title }}</h2>
          <p class="mt-3 text-gray-600">{{ item.desc }}</p>
        </article>
      </div>
    </section>

    <section class="bg-[#fff7ed] py-16">
      <div class="mx-auto grid max-w-7xl grid-cols-1 gap-8 px-4 sm:px-6 lg:grid-cols-[0.9fr_1.1fr] lg:px-8">
        <article class="rounded-[2rem] bg-white p-8 shadow-sm ring-1 ring-orange-100">
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">{{ $t('unfpa_global_page.architecture_kicker') }}</p>
          <h2 class="mt-3 text-3xl font-extrabold text-gray-900">{{ $t('unfpa_global_page.como_opera_agenda_mundial') }}</h2>
          <div class="mt-6 space-y-4">
            <div v-for="item in globalLayers" :key="item.title" class="rounded-2xl bg-gray-50 p-5">
              <h3 class="font-bold text-gray-900">{{ item.title }}</h3>
              <p class="mt-2 text-gray-600">{{ item.desc }}</p>
            </div>
          </div>
        </article>

        <article class="rounded-[2rem] bg-gray-900 p-8 text-white shadow-2xl">
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-orange-300">{{ $t('unfpa_global_page.priorities_kicker') }}</p>
          <h2 class="mt-3 text-3xl font-extrabold md:text-4xl">{{ $t('unfpa_global_page.tres_resultados_transformadores') }}</h2>
          <div class="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div v-for="item in transformativeGoals" :key="item.title" class="rounded-2xl bg-white/10 p-5">
              <h3 class="font-bold text-white">{{ item.title }}</h3>
              <p class="mt-2 text-sm text-white/75">{{ item.desc }}</p>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8">
      <div class="rounded-[2rem] bg-gray-900 px-8 py-10 text-white shadow-2xl sm:px-10">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-[1.05fr_0.95fr] lg:items-center">
          <div>
            <p class="text-sm font-bold uppercase tracking-[0.2em] text-orange-300">{{ $t('unfpa_global_page.conclusion_kicker') }}</p>
            <h2 class="mt-3 text-3xl font-extrabold md:text-4xl">{{ $t('unfpa_global_page.vision_internacional_transformar') }}</h2>
            <p class="mt-4 max-w-3xl text-white/80">
              {{ $t('unfpa_global_page.cooperacion_internacional_coherencia') }}
            </p>
          </div>

          <div class="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-1">
            <router-link to="/nuestra-labor/mnmns-en-bolivia" class="rounded-2xl bg-white/10 px-5 py-4 font-semibold text-white transition-colors hover:bg-white/15">{{ $t('unfpa_global_page.link_mnmns_bolivia') }}</router-link>
            <router-link to="/que-hacemos" class="rounded-2xl bg-[#F97316] px-5 py-4 font-semibold text-white transition-colors hover:bg-[#EA580C]">{{ $t('unfpa_global_page.link_que_hacemos') }}</router-link>
          </div>
        </div>
      </div>
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

const commitments = [
  { title: t('unfpa_global_page.commitment_mission_title'), desc: t('unfpa_global_page.commitment_mission_desc') },
  { title: t('unfpa_global_page.commitment_scale_title'), desc: t('unfpa_global_page.commitment_scale_desc') },
  { title: t('unfpa_global_page.commitment_coherence_title'), desc: t('unfpa_global_page.commitment_coherence_desc') }
];

const results = [
  {
    icon: 'pi-heart',
    title: t('unfpa_global_page.result_maternal_health_title'),
    desc: t('unfpa_global_page.result_maternal_health_desc')
  },
  {
    icon: 'pi-users',
    title: t('unfpa_global_page.result_family_planning_title'),
    desc: t('unfpa_global_page.result_family_planning_desc')
  },
  {
    icon: 'pi-shield',
    title: t('unfpa_global_page.result_violence_free_life_title'),
    desc: t('unfpa_global_page.result_violence_free_life_desc')
  }
];

const globalLayers = [
  {
    title: t('unfpa_global_page.global_layers_norms_title'),
    desc: t('unfpa_global_page.global_layers_norms_desc')
  },
  {
    title: t('unfpa_global_page.global_layers_alliances_title'),
    desc: t('unfpa_global_page.global_layers_alliances_desc')
  },
  {
    title: t('unfpa_global_page.global_layers_learning_title'),
    desc: t('unfpa_global_page.global_layers_learning_desc')
  }
];

const transformativeGoals = [
  {
    title: t('unfpa_global_page.transformative_goal_maternal_death_title'),
    desc: t('unfpa_global_page.transformative_goal_maternal_death_desc')
  },
  {
    title: t('unfpa_global_page.transformative_goal_unmet_need_title'),
    desc: t('unfpa_global_page.transformative_goal_unmet_need_desc')
  },
  {
    title: t('unfpa_global_page.transformative_goal_gender_violence_title'),
    desc: t('unfpa_global_page.transformative_goal_gender_violence_desc')
  },
  {
    title: t('unfpa_global_page.transformative_goal_youth_potential_title'),
    desc: t('unfpa_global_page.transformative_goal_youth_potential_desc')
  }
];

onMounted(() => {
  document.title = t('unfpa_global_page.mnmns_cooperacion_internacional');
  window.scrollTo(0, 0);
});
</script>