<template>
  <div class="min-h-screen bg-white pt-20">
    <PageHero
      kicker="Que Hacemos"
      title="Politicas publicas"
      subtitle="Producto 1: fortalecimiento de leyes, politicas y planes para ampliar cobertura universal y acceso en salud y derechos sexuales y reproductivos."
      backgroundImage="/img/fondo5.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <article class="rounded-3xl border border-gray-100 bg-white p-8 shadow-sm">
        <h2 class="text-2xl font-bold text-gray-900">Intervenciones estrategicas</h2>
        <p class="mt-4 leading-relaxed text-gray-600">
          El Producto 1 aporta a los resultados transformadores del plan estrategico y al UNSDCF mediante un entorno politico que expanda cobertura y acceso a salud materna, planificacion familiar y atencion de VBG en contextos de desarrollo y humanitarios.
        </p>
        <p class="mt-4 leading-relaxed text-gray-600">
          La MNMNS apoya el monitoreo de recomendaciones de comités de tratados de Naciones Unidas, reforzando diseño e implementación de políticas de SSR y VBG con rendición de cuentas participativa.
        </p>

        <ul class="mt-8 space-y-3 text-gray-700">
          <li><span class="font-bold text-[#F97316]">a)</span> Fortalecer capacidades de gobiernos para incrementar y monitorear asignaciones presupuestarias e incorporar servicios integrales de SSR en el SUS.</li>
          <li><span class="font-bold text-[#F97316]">b)</span> Impulsar resultados transformadores en PDES 2021-2025 y planes sectoriales, multisectoriales y locales con enfoque intercultural.</li>
          <li><span class="font-bold text-[#F97316]">c)</span> Fortalecer a ministerios y gobiernos subnacionales en diseno, implementacion, monitoreo y evaluacion de leyes y planes de SSR.</li>
          <li><span class="font-bold text-[#F97316]">d)</span> Potenciar enfoque de genero, derechos humanos e interculturalidad en planes de formacion de EIS.</li>
          <li><span class="font-bold text-[#F97316]">e)</span> Ampliar la enfermeria obstetrica con mejoras normativas, formativas, laborales y de prestacion de servicios.</li>
          <li><span class="font-bold text-[#F97316]">f)</span> Fortalecer sociedad civil y organizaciones comunitarias para monitorear compromisos y calidad de servicios SSR y VBG.</li>
          <li><span class="font-bold text-[#F97316]">g)</span> Promover inclusion de SSR y VBG en politicas de adaptacion climatica y gestion de riesgo de desastres.</li>
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
  document.title = 'Politicas publicas y rendicion de cuentas | MNMNS';
  window.scrollTo(0, 0);
});
</script>
