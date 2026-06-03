<template>
  <div class="min-h-screen bg-white pt-20">
    <PageHero
      kicker="Que Hacemos"
      title="Transformacion de las normas sociales de genero"
      subtitle="Producto 3: fortalecer actores e instituciones para enfrentar normas discriminatorias y proteger autonomia corporal y vida libre de violencia."
      backgroundImage="/img/fondo7.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <article class="rounded-3xl border border-gray-100 bg-white p-8 shadow-sm">
        <h2 class="text-2xl font-bold text-gray-900">Intervenciones estrategicas</h2>
        <p class="mt-4 leading-relaxed text-gray-600">
          Este producto aporta a la reduccion de violencia y discriminacion mediante un enfoque socioecologico en niveles individual, familiar, comunitario, institucional y estatal.
        </p>

        <ul class="mt-8 space-y-3 text-gray-700">
          <li><span class="font-bold text-[#F97316]">a)</span> Fortalecer instituciones nacionales y subnacionales para enfrentar normas nocivas en salud, educacion y proteccion.</li>
          <li><span class="font-bold text-[#F97316]">b)</span> Asistencia tecnica para estrategias innovadoras que incrementen capacidades y autonomia de ninas, adolescentes y mujeres.</li>
          <li><span class="font-bold text-[#F97316]">c)</span> Potenciar liderazgo y exigibilidad de derechos desde sociedad civil, movimientos sociales y juventudes.</li>
          <li><span class="font-bold text-[#F97316]">d)</span> Apoyar a gobiernos municipales en reconocimiento y ampliacion de buenas practicas y masculinidades positivas.</li>
          <li><span class="font-bold text-[#F97316]">e)</span> Alianzas con ONU, Gobierno, OSC, medios, sector privado y academia para estrategias de comunicacion preventiva.</li>
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
  document.title = 'Transformacion de normas sociales de genero | MNMNS';
  window.scrollTo(0, 0);
});
</script>
