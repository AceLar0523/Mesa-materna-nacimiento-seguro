<template>
  <div class="landing-wrapper bg-white overflow-hidden">
    <Hero />

    <section class="py-24 bg-gray-50/50">
      <ActionPillars />
    </section>

    <section class="py-20 bg-white">
      <MaternalGallery />
    </section>

    <section class="py-24 bg-[#F97316]/5">
      <DepartmentFocus />
    </section>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import Hero from '../components/landing/Hero/Hero.vue';
import ActionPillars from '../components/landing/ActionPillars/ActionPillars.vue';
import MaternalGallery from '../components/landing/MaternalGallery/MaternalGallery.vue';
import DepartmentFocus from '../components/landing/DepartmentFocus/DepartmentFocus.vue';
import Footer from '../components/landing/Footer/Footer.vue';
</script>