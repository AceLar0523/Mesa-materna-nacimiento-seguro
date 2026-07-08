<template>
  <div class="pt-20 bg-gray-50 min-h-screen">
    <PageHero
      :kicker="$t('conocenos_page.hero_kicker')"
      :title="$t('conocenos_page.hero_title')"
      :subtitle="$t('conocenos_page.hero_subtitle')"
      backgroundImage="/img/fondo12.jpg"
    />

    <section class="py-16 md:py-24 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div>
          <h2 class="text-3xl font-bold text-gray-900 mb-6">{{ $t('conocenos_page.q_es_mnmns_title') }}</h2>
          <p class="text-gray-600 mb-4 leading-relaxed">
            {{ $t('conocenos_page.mnmns_desc1_part1') }}<strong>MNMNS</strong>{{ $t('conocenos_page.mnmns_desc1_part2') }}<strong>UNICEF</strong>{{ $t('conocenos_page.mnmns_desc1_part3') }}
          </p>
          <p class="text-gray-600 leading-relaxed">
            {{ $t('conocenos_page.q_es_mnmns_desc2') }}
          </p>
        </div>
        <div class="bg-orange-100 rounded-3xl h-80 relative overflow-hidden shadow-lg flex items-center justify-center">
          <i class="pi pi-users text-7xl text-[#F97316] opacity-50"></i>
          <span class="absolute bottom-4 right-4 bg-white px-3 py-1 text-xs font-bold text-[#F97316] rounded-full shadow">
            {{ $t('conocenos_page.alianza_label') }}
          </span>
        </div>
      </div>
    </section>

    <section class="bg-white py-16 border-t border-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          
          <div class="p-10 rounded-3xl bg-orange-50/50 border border-orange-100 hover:shadow-xl transition-shadow duration-300">
            <div class="w-14 h-14 bg-[#F97316] rounded-2xl flex items-center justify-center mb-6 shadow-md">
              <i class="pi pi-compass text-2xl text-white"></i>
            </div>
            <h3 class="text-2xl font-bold text-gray-900 mb-4">{{ $t('conocenos_page.mision_title') }}</h3>
            <p class="text-gray-600 leading-relaxed">
              {{ $t('conocenos_page.mision_desc') }}
            </p>
          </div>

          <div class="p-10 rounded-3xl bg-green-50/50 border border-green-100 hover:shadow-xl transition-shadow duration-300">
            <div class="w-14 h-14 bg-[#00833D] rounded-2xl flex items-center justify-center mb-6 shadow-md">
              <i class="pi pi-eye text-2xl text-white"></i>
            </div>
            <h3 class="text-2xl font-bold text-gray-900 mb-4">{{ $t('conocenos_page.vision_title') }}</h3>
            <p class="text-gray-600 leading-relaxed">
              {{ $t('conocenos_page.vision_desc') }}
            </p>
          </div>

        </div>
      </div>
    </section>

    <section class="py-16 md:py-24 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 class="text-3xl font-bold text-center text-gray-900 mb-12">{{ $t('conocenos_page.pilares_title') }}</h2>
      
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="text-center group">
          <div class="w-20 h-20 mx-auto bg-gray-50 rounded-full flex items-center justify-center mb-4 group-hover:bg-[#F97316] transition-colors duration-300 shadow-sm border border-gray-100">
            <i class="pi pi-heart text-2xl text-[#F97316] group-hover:text-white transition-colors"></i>
          </div>
          <h4 class="font-bold text-lg text-gray-900 mb-2">{{ $t('conocenos_page.pilar1_title') }}</h4>
          <p class="text-sm text-gray-600">{{ $t('conocenos_page.pilar1_desc') }}</p>
        </div>
        
        <div class="text-center group">
          <div class="w-20 h-20 mx-auto bg-gray-50 rounded-full flex items-center justify-center mb-4 group-hover:bg-[#F97316] transition-colors duration-300 shadow-sm border border-gray-100">
            <i class="pi pi-building text-2xl text-[#F97316] group-hover:text-white transition-colors"></i>
          </div>
          <h4 class="font-bold text-lg text-gray-900 mb-2">{{ $t('conocenos_page.pilar2_title') }}</h4>
          <p class="text-sm text-gray-600">{{ $t('conocenos_page.pilar2_desc') }}</p>
        </div>
        
        <div class="text-center group">
          <div class="w-20 h-20 mx-auto bg-gray-50 rounded-full flex items-center justify-center mb-4 group-hover:bg-[#F97316] transition-colors duration-300 shadow-sm border border-gray-100">
            <i class="pi pi-users text-2xl text-[#F97316] group-hover:text-white transition-colors"></i>
          </div>
          <h4 class="font-bold text-lg text-gray-900 mb-2">{{ $t('conocenos_page.pilar3_title') }}</h4>
          <p class="text-sm text-gray-600">{{ $t('conocenos_page.pilar3_desc') }}</p>
        </div>

        <div class="text-center group">
          <div class="w-20 h-20 mx-auto bg-gray-50 rounded-full flex items-center justify-center mb-4 group-hover:bg-[#F97316] transition-colors duration-300 shadow-sm border border-gray-100">
            <i class="pi pi-chart-line text-2xl text-[#F97316] group-hover:text-white transition-colors"></i>
          </div>
          <h4 class="font-bold text-lg text-gray-900 mb-2">{{ $t('conocenos_page.pilar4_title') }}</h4>
          <p class="text-sm text-gray-600">{{ $t('conocenos_page.pilar4_desc') }}</p>
        </div>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '../components/landing/Footer/Footer.vue';

onMounted(() => {
  document.title = 'Conócenos | MNMNS Bolivia';
  window.scrollTo(0, 0);
});
</script>