<template>
  <div class="min-h-screen bg-white pt-20">
    <PageHero
      kicker="Nuestra Labor"
      title="MNMNS y cooperación regional"
      subtitle="La cooperación regional coordina prioridades comunes para acelerar la reducción de desigualdades, fortalecer sistemas de salud y proteger los derechos sexuales y reproductivos en contextos diversos."
      backgroundImage="/img/fondo3.png"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-10 lg:grid-cols-[1.05fr_0.95fr]">
        <div>
          <p class="mt-4 max-w-3xl text-gray-600 leading-relaxed">
            La cooperación regional de la MNMNS coordina prioridades comunes en América Latina y el Caribe para acelerar la reducción de desigualdades, fortalecer sistemas de salud y proteger los derechos sexuales y reproductivos en contextos diversos. Su trabajo conecta evidencia regional, asistencia técnica continua y respuesta rápida en escenarios humanitarios para que los países avancen con soluciones adaptadas a sus realidades sociales, culturales y territoriales.
          </p>
          <p class="mt-4 max-w-3xl text-gray-600 leading-relaxed">
            Como región, enfrentamos desafíos compartidos: mujeres indígenas con mortalidad materna 3 veces superior al promedio nacional, adolescentes sin acceso a anticonceptivos, violencia de género sin respuesta institucional coordinada. Pero también compartimos aprendizajes: un país que implementó casas maternas puede ayudar a otro a replicar, un servicio de emergencia obstétrica que funcionó en una ciudad puede adaptarse en zonas rurales.
          </p>

          <div class="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-3">
            <div v-for="stat in stats" :key="stat.label" class="rounded-2xl bg-white p-5 shadow-sm ring-1 ring-orange-100">
              <p class="text-sm font-semibold text-gray-500">{{ stat.label }}</p>
              <p class="mt-2 text-lg font-bold text-gray-900">{{ stat.value }}</p>
              <p class="mt-1 text-sm text-gray-600">{{ stat.desc }}</p>
            </div>
          </div>
        </div>

        <div class="relative">
          <div class="rounded-[2rem] border border-orange-100 bg-white p-5 shadow-2xl">
            <img src="/img/fondo8.jpg" alt="Red regional de la MNMNS" class="w-full rounded-[1.5rem]" />
          </div>
          <div class="absolute -bottom-6 left-6 rounded-2xl bg-gray-900 px-5 py-4 text-white shadow-xl">
            <p class="text-xs font-bold uppercase tracking-[0.2em] text-orange-300">Region</p>
            <p class="mt-1 text-lg font-bold">Cooperacion e impacto compartido</p>
          </div>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-4">
        <article v-for="item in pillars" :key="item.title" class="rounded-3xl border border-gray-100 bg-white p-7 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
          <div class="mb-5 inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-orange-50 text-[#F97316]">
            <i :class="['pi text-xl', item.icon]"></i>
          </div>
          <h2 class="text-xl font-bold text-gray-900">{{ item.title }}</h2>
          <p class="mt-3 text-gray-600">{{ item.desc }}</p>
        </article>
      </div>
    </section>

    <section class="bg-gray-50 py-16">
      <div class="mx-auto grid max-w-7xl grid-cols-1 gap-8 px-4 sm:px-6 lg:grid-cols-[0.95fr_1.05fr] lg:px-8">
        <div class="rounded-[2rem] bg-white p-8 shadow-sm ring-1 ring-gray-100">
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">Enfoque regional</p>
          <h2 class="mt-3 text-3xl font-extrabold text-gray-900">Una agenda común para múltiples contextos</h2>
          <p class="mt-4 text-gray-600">
            La región combina países con desafíos distintos, por eso la cooperación regional adapta herramientas, acompaña políticas y comparte aprendizajes que puedan escalarse de forma responsable.
          </p>

          <div class="mt-8 space-y-4">
            <div v-for="item in regionalLines" :key="item.title" class="rounded-2xl bg-orange-50 p-5">
              <h3 class="font-bold text-gray-900">{{ item.title }}</h3>
              <p class="mt-2 text-sm text-gray-600">{{ item.desc }}</p>
            </div>
          </div>
        </div>

        <div class="rounded-[2rem] bg-gray-900 p-8 text-white shadow-2xl">
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-orange-300">Cómo se traduce</p>
          <h2 class="mt-3 text-3xl font-extrabold md:text-4xl">Del marco regional a la acción nacional</h2>
          <div class="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2">
            <article v-for="item in pathways" :key="item.title" class="rounded-2xl bg-white/10 p-5">
              <h3 class="font-bold text-white">{{ item.title }}</h3>
              <p class="mt-2 text-sm text-white/75">{{ item.desc }}</p>
            </article>
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

const stats = [
  { label: 'Enfoque', value: 'Derechos', desc: 'Prioriza igualdad y acceso efectivo.' },
  { label: 'Método', value: 'Evidencia', desc: 'Usa datos para orientar acción.' },
  { label: 'Alcance', value: 'Regional', desc: 'Conecta países y aprendizajes.' }
];

const pillars = [
  {
    icon: 'pi-globe',
    title: 'Cooperación técnica',
    desc: 'Compartir metodologías y buenas prácticas entre países para acelerar resultados sostenibles.'
  },
  {
    icon: 'pi-heart',
    title: 'Salud y derechos',
    desc: 'Fortalecer políticas, servicios y sistemas para proteger la salud sexual y reproductiva.'
  },
  {
    icon: 'pi-bolt',
    title: 'Respuesta rápida',
    desc: 'Apoyar contextos humanitarios y de crisis para asegurar continuidad de servicios esenciales.'
  },
  {
    icon: 'pi-chart-line',
    title: 'Evidencia regional',
    desc: 'Producir análisis comparados que orienten decisiones de política pública y cooperación.'
  }
];

const regionalLines = [
  {
    title: 'Contextos diversos, una agenda común',
    desc: 'La región integra realidades urbanas, rurales, insulares y fronterizas, por lo que la respuesta debe ser flexible y contextualizada.'
  },
  {
    title: 'Aprendizaje entre países',
    desc: 'Los avances en un país pueden adaptarse en otros, favoreciendo eficiencia y mayor velocidad de implementación.'
  },
  {
    title: 'Enfoque en poblaciones dejadas atrás',
    desc: 'La oficina regional impulsa estrategias para que la respuesta llegue a quienes enfrentan más barreras de acceso.'
  }
];

const pathways = [
  { title: 'Políticas públicas', desc: 'Soporte para marcos normativos y planes nacionales alineados con derechos y evidencia.' },
  { title: 'Sistemas de salud', desc: 'Fortalecimiento de servicios, cadena de suministros y capacidades del personal.' },
  { title: 'Comunidades', desc: 'Trabajo con juventudes, liderazgos sociales y organizaciones territoriales.' },
  { title: 'Recuperación y crisis', desc: 'Acciones para sostener la atención en emergencia, migración o desastres.' }
];

onMounted(() => {
  document.title = 'MNMNS y cooperación regional';
  window.scrollTo(0, 0);
});
</script>
