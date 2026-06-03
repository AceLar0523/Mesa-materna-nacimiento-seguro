<template>
  <section
    class="relative isolate overflow-hidden text-white"
    :class="backgroundImage ? 'bg-gray-900' : 'bg-[#F97316]'"
  >
    <div
      class="absolute inset-0 bg-cover bg-center bg-no-repeat"
      :style="backgroundStyle"
      aria-hidden="true"
    ></div>
    <div class="absolute inset-0 bg-black/55"></div>
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_left,_rgba(255,255,255,0.18),_transparent_38%)]"></div>
    <div class="absolute -right-20 top-8 h-72 w-72 rounded-full bg-white/10 blur-3xl"></div>
    <div class="absolute -left-20 bottom-0 h-72 w-72 rounded-full bg-black/20 blur-3xl"></div>

    <div class="relative mx-auto flex min-h-[420px] max-w-7xl items-end px-4 py-16 sm:min-h-[480px] sm:px-6 lg:min-h-[540px] lg:px-8">
      <div class="max-w-4xl pb-2 text-left">
        <p v-if="kicker" class="mb-4 text-sm font-bold uppercase tracking-[0.3em] text-orange-100">
          {{ kicker }}
        </p>
        <h1 class="max-w-3xl text-4xl font-extrabold leading-[1.02] md:text-5xl lg:text-6xl xl:text-7xl">
          {{ title }}
        </h1>
        <p v-if="subtitle" class="mt-6 max-w-3xl text-lg font-medium leading-relaxed text-orange-50 md:text-xl">
          {{ subtitle }}
        </p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = withDefaults(
  defineProps<{
    title: string;
    subtitle?: string;
    kicker?: string;
    backgroundImage?: string;
  }>(),
  {
    backgroundImage: ''
  }
);

const backgroundStyle = computed(() => {
  if (!props.backgroundImage) {
    return {};
  }

  return {
    backgroundImage: `url(${props.backgroundImage})`
  };
});
</script>