<template>
  <div class="min-h-screen bg-white pt-20">
    <PageHero
      kicker="Nuestra Labor"
      title="MNMNS en Bolivia"
      subtitle="La Mesa Nacional de Maternidad y Nacimiento Seguros acompaña al país para que cada mujer, adolescente y persona joven pueda ejercer sus derechos con información, servicios de calidad y entornos libres de violencia."
      backgroundImage="/img/fondo1.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-3">
        <article v-for="item in focusAreas" :key="item.title" class="rounded-3xl border border-gray-100 bg-white p-7 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
          <div class="mb-5 inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-orange-50 text-[#F97316]">
            <i :class="['pi text-xl', item.icon]"></i>
          </div>
          <h2 class="text-2xl font-bold text-gray-900">{{ item.title }}</h2>
          <p class="mt-3 leading-relaxed text-gray-600">{{ item.desc }}</p>
        </article>
      </div>
    </section>

    <section class="bg-[#fff7ed] py-16">
      <div class="mx-auto grid max-w-7xl grid-cols-1 gap-10 px-4 sm:px-6 lg:grid-cols-[1.1fr_0.9fr] lg:px-8">
        <div>
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">Prioridades de trabajo</p>
          <h2 class="mt-3 text-3xl font-extrabold text-gray-900 md:text-4xl">Una agenda enfocada en resultados transformadores</h2>
          <div class="mt-8 space-y-4">
            <article v-for="priority in priorities" :key="priority.title" class="rounded-2xl border border-orange-100 bg-white p-5 shadow-sm">
              <h3 class="text-lg font-bold text-gray-900">{{ priority.title }}</h3>
              <p class="mt-2 text-gray-600">{{ priority.desc }}</p>
            </article>
          </div>
        </div>

        <div class="relative overflow-hidden rounded-[2rem] border border-orange-100 bg-white p-5 shadow-xl">
          <img src="/img/fondo2.jpg" alt="Mapa de trabajo de la MNMNS" class="h-full w-full rounded-[1.5rem] object-cover" />
          <div class="mt-5 grid grid-cols-2 gap-4 text-center">
            <div class="rounded-2xl bg-orange-50 p-4">
              <p class="text-sm font-semibold text-gray-500">Enfoque</p>
              <p class="mt-1 text-lg font-bold text-gray-900">Territorial</p>
            </div>
            <div class="rounded-2xl bg-orange-50 p-4">
              <p class="text-sm font-semibold text-gray-500">Alianza</p>
              <p class="mt-1 text-lg font-bold text-gray-900">Multisectorial</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white py-16 border-t border-gray-200">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-12 lg:grid-cols-2">
          <div>
            <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">Contexto y desafío</p>
            <h2 class="mt-3 text-3xl font-extrabold text-gray-900">Por qué existe la MNMNS</h2>
            <p class="mt-4 max-w-2xl text-gray-600 leading-relaxed">
              Bolivia ha enfrentado durante décadas importantes desafíos en salud materna. Factores como la desigualdad social, barreras geográficas, limitaciones en los servicios de salud y diferencias culturales han incidido directamente en el riesgo de muerte durante el embarazo, parto o postparto. En este contexto, la MNMNS se consolida como un mecanismo de coordinación estratégica para enfrentar estos problemas de manera integral.
            </p>
            <p class="mt-4 max-w-2xl text-gray-600 leading-relaxed">
              Las mujeres indígenas y de bajos recursos son las más afectadas, lo que evidencia una fuerte inequidad estructural en salud que requiere respuestas coordinadas, sostenidas y multisectoriales.
            </p>
          </div>
          <div class="bg-orange-50 rounded-[2rem] p-8 ring-1 ring-orange-100">
            <h3 class="text-lg font-bold text-gray-900 mb-6">Actores que conforman la MNMNS</h3>
            <ul class="space-y-4 text-gray-600">
              <li class="flex gap-3">
                <span class="text-[#F97316] font-bold">•</span>
                <span><strong>Ministerio de Salud</strong> - Rector de políticas públicas y estrategia nacional</span>
              </li>
              <li class="flex gap-3">
                <span class="text-[#F97316] font-bold">•</span>
                <span><strong>Servicios Departamentales de Salud (SEDES)</strong> - Ejecución territorial</span>
              </li>
              <li class="flex gap-3">
                <span class="text-[#F97316] font-bold">•</span>
                <span><strong>Organismos internacionales</strong> - UNICEF, OPS/OMS, ONU (asistencia técnica y financiamiento)</span>
              </li>
              <li class="flex gap-3">
                <span class="text-[#F97316] font-bold">•</span>
                <span><strong>Organizaciones sociales</strong> - Confederaciones indígenas, organizaciones de mujeres, academia</span>
              </li>
              <li class="flex gap-3">
                <span class="text-[#F97316] font-bold">•</span>
                <span><strong>Sociedades médicas</strong> - Especialistas en ginecología, pediatría y medicina general</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        <article class="rounded-[2rem] bg-white p-8 shadow-sm ring-1 ring-gray-100">
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">Logros alcanzados</p>
          <h2 class="mt-3 text-2xl font-extrabold text-gray-900 mb-6">Avances demostrados</h2>
          <ul class="space-y-3 text-gray-600">
            <li class="flex gap-3">
              <span class="text-[#F97316] font-bold text-xl leading-none mt-1">✓</span>
              <span>Fortalecimiento de políticas públicas en salud materna a nivel nacional</span>
            </li>
            <li class="flex gap-3">
              <span class="text-[#F97316] font-bold text-xl leading-none mt-1">✓</span>
              <span>Implementación de casas maternas en zonas rurales y de difícil acceso</span>
            </li>
            <li class="flex gap-3">
              <span class="text-[#F97316] font-bold text-xl leading-none mt-1">✓</span>
              <span>Mayor articulación interinstitucional entre actores del sistema de salud</span>
            </li>
            <li class="flex gap-3">
              <span class="text-[#F97316] font-bold text-xl leading-none mt-1">✓</span>
              <span>Sensibilización comunitaria sobre importancia del parto seguro y respetado</span>
            </li>
            <li class="flex gap-3">
              <span class="text-[#F97316] font-bold text-xl leading-none mt-1">✓</span>
              <span>Mejora progresiva en indicadores de salud materna-neonatal</span>
            </li>
          </ul>
        </article>

        <article class="rounded-[2rem] bg-gray-900 p-8 text-white shadow-2xl">
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-orange-300">Desafíos pendientes</p>
          <h2 class="mt-3 text-2xl font-extrabold md:text-2xl mb-6">Trabajo que continúa</h2>
          <ul class="space-y-3">
            <li class="flex gap-3">
              <span class="text-orange-300 font-bold text-xl leading-none mt-1">→</span>
              <span class="text-white/90">Reducir aún más la mortalidad materna en zonas rurales e indígenas</span>
            </li>
            <li class="flex gap-3">
              <span class="text-orange-300 font-bold text-xl leading-none mt-1">→</span>
              <span class="text-white/90">Mejorar cobertura y acceso en territorios de mayor vulnerabilidad</span>
            </li>
            <li class="flex gap-3">
              <span class="text-orange-300 font-bold text-xl leading-none mt-1">→</span>
              <span class="text-white/90">Fortalecer recursos humanos y capacitación continua en zonas remotas</span>
            </li>
            <li class="flex gap-3">
              <span class="text-orange-300 font-bold text-xl leading-none mt-1">→</span>
              <span class="text-white/90">Garantizar sostenibilidad financiera de las acciones implementadas</span>
            </li>
            <li class="flex gap-3">
              <span class="text-orange-300 font-bold text-xl leading-none mt-1">→</span>
              <span class="text-white/90">Integrar tecnología e información para mejor monitoreo y decisión</span>
            </li>
          </ul>
        </article>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8">
      <div class="rounded-[2rem] bg-gray-900 px-8 py-10 text-white shadow-2xl sm:px-10">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-[1.2fr_0.8fr] lg:items-center">
          <div>
            <p class="text-sm font-bold uppercase tracking-[0.2em] text-orange-300">Cierre</p>
            <h2 class="mt-3 text-3xl font-extrabold md:text-4xl">Construimos un sistema de salud y protección que llegue primero a quienes más lo necesitan.</h2>
            <p class="mt-4 max-w-3xl text-white/80">
              Esta página resume el rol de la MNMNS en Bolivia y conecta con las líneas de trabajo de políticas públicas, calidad de servicios y transformación social que recorren el resto del sitio.
            </p>
          </div>

          <div class="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-1">
            <router-link to="/que-hacemos" class="rounded-2xl bg-white/10 px-5 py-4 font-semibold text-white transition-colors hover:bg-white/15">Explorar qué hacemos</router-link>
            <router-link to="/contactanos" class="rounded-2xl bg-[#F97316] px-5 py-4 font-semibold text-white transition-colors hover:bg-[#EA580C]">Contactar al equipo</router-link>
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

const focusAreas = [
  {
    icon: 'pi-heart',
    title: 'Salud materna segura',
    desc: 'Acompañamos el fortalecimiento de servicios de emergencia obstétrica, control prenatal e institucionalización del parto seguro, respetuoso y de calidad.'
  },
  {
    icon: 'pi-shield',
    title: 'Prevención de violencia',
    desc: 'Impulsamos respuestas institucionales y comunitarias integrales para prevenir y atender la violencia basada en género en todos los espacios.'
  },
  {
    icon: 'pi-sitemap',
    title: 'Trabajo articulado',
    desc: 'Coordinamos con Estado, gobiernos locales, sociedad civil, comunidades indígenas y cooperación internacional para que la agenda tenga escala e impacto real.'
  }
];

const priorities = [
  {
    title: 'Evidencia para la decisión pública',
    desc: 'Realizamos análisis de casos de mortalidad materna, identificamos barreras de acceso (las tres demoras) y generamos recomendaciones estratégicas basadas en datos territoriales reales.'
  },
  {
    title: 'Servicios con calidad e interculturalidad',
    desc: 'Fortalecemos emergencias obstétricas, mejoramos disponibilidad de insumos neonatales, capacitamos personal y articulamos medicina académica con saberes de parteras tradicionales.'
  },
  {
    title: 'Cambios sociales sostenibles',
    desc: 'Trabajamos con comunidades indígenas y campesinas, jóvenes e instituciones para cuestionar normas discriminatorias, ampliar autonomía de mujeres y garantizar derechos sexuales y reproductivos.'
  }
];

onMounted(() => {
  document.title = 'MNMNS en Bolivia | Nuestra Labor';
  window.scrollTo(0, 0);
});
</script>
