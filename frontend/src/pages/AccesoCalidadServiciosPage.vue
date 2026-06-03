<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <PageHero
      kicker="Que Hacemos"
      title="Acceso a calidad de servicios de atencion"
      subtitle="Producto 2: fortalecer capacidades nacionales y subnacionales para garantizar cobertura universal y servicios de SSR y VBG de alta calidad."
      backgroundImage="/img/fondo6.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <article class="rounded-3xl border border-gray-100 bg-white p-8 shadow-sm">
        <h2 class="text-2xl font-bold text-gray-900">Intervenciones estrategicas</h2>
        <p class="mt-4 leading-relaxed text-gray-600">
          Este producto contribuye a mejorar condiciones de salud, acceso a servicios sanitarios de calidad, derecho a educacion y reduccion de violencia contra mujeres, ninas, ninos y adolescentes.
        </p>

        <ul class="mt-8 space-y-3 text-gray-700">
          <li><span class="font-bold text-[#F97316]">a.i)</span> Fortalecer APS para calidad y disponibilidad continua de cuidados obstetricos y neonatales de emergencia.</li>
          <li><span class="font-bold text-[#F97316]">a.ii)</span> Fortalecer estandares interculturales y de calidad para ampliar acceso de mujeres indigenas y rurales.</li>
          <li><span class="font-bold text-[#F97316]">a.iii)</span> Ampliar despliegue de enfermeria obstetrica para partos seguros e incremento de anticonceptivos modernos.</li>
          <li><span class="font-bold text-[#F97316]">a.iv)</span> Mejorar proyeccion y adquisicion de anticonceptivos para asegurar disponibilidad hasta la ultima milla.</li>
          <li><span class="font-bold text-[#F97316]">b)</span> Desarrollar capacidades del personal de salud y de instituciones garantes para atencion integral en VBG.</li>
          <li><span class="font-bold text-[#F97316]">c)</span> Asistencia tecnica al Ministerio de Educacion y gobiernos subnacionales para fortalecer EIS dentro y fuera de escuelas.</li>
          <li><span class="font-bold text-[#F97316]">d)</span> Fortalecer sociedad civil y organizaciones comunitarias para incrementar demanda de SSR y vida libre de violencia.</li>
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

onMounted(() => {
  document.title = 'Acceso a calidad de servicios de atencion | MNMNS';
  window.scrollTo(0, 0);
});
</script>
