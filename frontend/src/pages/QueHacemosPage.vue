<template>
  <div class="min-h-screen bg-[#fffaf5] pt-20">
    <PageHero
      kicker="Que Hacemos"
      title="La MNMNS trabaja en tres líneas estratégicas"
      subtitle="Las políticas públicas, los servicios de calidad y la transformación social son las palancas que usamos para garantizar una maternidad segura, una vida libre de violencia y derechos sexuales y reproductivos para todas: mujeres, adolescentes, jóvenes y personas de la diversidad sexual."
      backgroundImage="/img/hero-que-hacemos.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        <router-link to="/que-hacemos/politicas-publicas-rendicion-cuentas" class="group rounded-3xl border border-orange-100 bg-white p-7 shadow-sm transition-all hover:-translate-y-1 hover:shadow-xl">
          <p class="text-xs font-bold uppercase tracking-widest text-[#F97316]">Producto 1</p>
          <h3 class="mt-3 text-2xl font-bold text-gray-900 group-hover:text-[#F97316]">Políticas públicas y rendición de cuentas</h3>
          <p class="mt-3 text-gray-600">Aprovechamos análisis de datos, monitoreo de recomendaciones de tratados ONU y diálogo multisectorial para fortalecer leyes, planes y presupuestos que amplíen cobertura y acceso a salud sexual y reproductiva con enfoque de equidad.</p>
        </router-link>

        <router-link to="/que-hacemos/acceso-calidad-servicios-atencion" class="group rounded-3xl border border-orange-100 bg-white p-7 shadow-sm transition-all hover:-translate-y-1 hover:shadow-xl">
          <p class="text-xs font-bold uppercase tracking-widest text-[#F97316]">Producto 2</p>
          <h3 class="mt-3 text-2xl font-bold text-gray-900 group-hover:text-[#F97316]">Acceso a calidad de servicios de atención</h3>
          <p class="mt-3 text-gray-600">Fortalecemos capacidades técnicas, mejoramos disponibilidad de insumos neonatales, capacitamos personal sanitario y garantizamos servicios SSR (Salud Sexual y Reproductiva) y VBG (Violencia Basada en Género) de calidad en contextos de desarrollo y emergencia.</p>
        </router-link>

        <router-link to="/que-hacemos/transformacion-normas-sociales-genero" class="group rounded-3xl border border-orange-100 bg-white p-7 shadow-sm transition-all hover:-translate-y-1 hover:shadow-xl">
          <p class="text-xs font-bold uppercase tracking-widest text-[#F97316]">Producto 3</p>
          <h3 class="mt-3 text-2xl font-bold text-gray-900 group-hover:text-[#F97316]">Transformación de las normas sociales de género</h3>
          <p class="mt-3 text-gray-600">Trabajamos con comunidades, instituciones y líderes sociales para cuestionar normas discriminatorias que perpetúan desigualdad, violencia e inequidad. Promovemos espacios seguros, autonomía corporal y acceso a oportunidades para adolescentes y jóvenes.</p>
        </router-link>

        <router-link to="/datos" class="group rounded-3xl border border-orange-100 bg-white p-7 shadow-sm transition-all hover:-translate-y-1 hover:shadow-xl">
          <p class="text-xs font-bold uppercase tracking-widest text-[#F97316]">Monitoreo</p>
          <h3 class="mt-3 text-2xl font-bold text-gray-900 group-hover:text-[#F97316]">Datos</h3>
          <p class="mt-3 text-gray-600">Explora indicadores oficiales y avances trimestrales de impacto interinstitucional.</p>
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

onMounted(() => {
  document.title = 'Que hacemos | MNMNS Bolivia';
  window.scrollTo(0, 0);
});
</script>
