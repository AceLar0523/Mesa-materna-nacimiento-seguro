<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <PageHero
      kicker="Nuestra Labor"
      title="MNMNS y cooperación internacional"
      subtitle="La MNMNS opera en plataformas globales para definir estándares de calidad, compartir evidencia, fortalecer sistemas de salud y garantizar que cada mujer, persona joven y adolescente ejerzan sus derechos sexuales y reproductivos."
      backgroundImage="/img/fondo4.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 gap-10 lg:grid-cols-[1.05fr_0.95fr]">
        <div>
          <p class="mt-4 max-w-4xl text-gray-600 leading-relaxed">
            La MNMNS a través de sus espacios de cooperación internacional define marcos estratégicos, prioridades programáticas, estándares de calidad y alianzas globales que luego se adaptan en oficinas regionales y se implementan en cada país. Esto significa que decisiones en foros internacionales tienen impacto directo en consultorios rurales de Bolivia, escuelas donde hablamos de derechos y hospitales donde atienden partos.
          </p>
          <p class="mt-4 max-w-4xl text-gray-600 leading-relaxed">
            El trabajo global busca reducir desigualdades estructurales que persisten a pesar de los compromisos internacionales asumidos (Objetivos de Desarrollo Sostenible, Derechos Humanos, Convención de Eliminación de Todas las Formas de Discriminación contra la Mujer). Para ello, articula gobiernos, agencias multilaterales, academia, sector privado y movimientos sociales en búsqueda de soluciones sostenibles.
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
            <p class="text-xs font-bold uppercase tracking-[0.2em] text-orange-100">Global</p>
            <p class="mt-1 text-lg font-bold">Marco, alianzas y resultados</p>
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
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">Arquitectura global</p>
          <h2 class="mt-3 text-3xl font-extrabold text-gray-900">Cómo opera la agenda mundial</h2>
          <div class="mt-6 space-y-4">
            <div v-for="item in globalLayers" :key="item.title" class="rounded-2xl bg-gray-50 p-5">
              <h3 class="font-bold text-gray-900">{{ item.title }}</h3>
              <p class="mt-2 text-gray-600">{{ item.desc }}</p>
            </div>
          </div>
        </article>

        <article class="rounded-[2rem] bg-gray-900 p-8 text-white shadow-2xl">
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-orange-300">Prioridades</p>
          <h2 class="mt-3 text-3xl font-extrabold md:text-4xl">Tres resultados transformadores que orientan el trabajo global</h2>
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
            <p class="text-sm font-bold uppercase tracking-[0.2em] text-orange-300">Cierre</p>
            <h2 class="mt-3 text-3xl font-extrabold md:text-4xl">Una visión internacional para transformar realidades locales.</h2>
            <p class="mt-4 max-w-3xl text-white/80">
              El trabajo de la cooperación internacional da coherencia a la acción y permite que cada oficina país se apoye en una estrategia clara, medible y alineada a derechos.
            </p>
          </div>

          <div class="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-1">
            <router-link to="/nuestra-labor/mnmns-en-bolivia" class="rounded-2xl bg-white/10 px-5 py-4 font-semibold text-white transition-colors hover:bg-white/15">Ver MNMNS en Bolivia</router-link>
            <router-link to="/que-hacemos" class="rounded-2xl bg-[#F97316] px-5 py-4 font-semibold text-white transition-colors hover:bg-[#EA580C]">Explorar qué hacemos</router-link>
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

const commitments = [
  { title: 'Misión', desc: 'Proteger derechos y ampliar oportunidades para mujeres, adolescentes y jóvenes.' },
  { title: 'Escala', desc: 'Definir marcos, financiamiento y alianzas globales con impacto local.' },
  { title: 'Coherencia', desc: 'Alinear prioridades entre sede, regiones y países.' }
];

const results = [
  {
    icon: 'pi-heart',
    title: 'Salud materna prevenible',
    desc: 'Poner fin a las muertes maternas evitables mediante servicios de calidad, acceso oportuno y atención respetuosa.'
  },
  {
    icon: 'pi-users',
    title: 'Planificación familiar',
    desc: 'Reducir la necesidad insatisfecha de métodos anticonceptivos y fortalecer la autonomía reproductiva.'
  },
  {
    icon: 'pi-shield',
    title: 'Vida libre de violencia',
    desc: 'Impulsar sistemas y comunidades que prevengan y respondan a la violencia basada en género.'
  }
];

const globalLayers = [
  {
    title: 'Normas y estrategias',
    desc: 'Se definen prioridades, metas y herramientas que orientan la cooperación internacional de la MNMNS.'
  },
  {
    title: 'Alianzas multilaterales',
    desc: 'Se articulan gobiernos, agencias ONU, academia, sector privado y sociedad civil para ampliar alcance.'
  },
  {
    title: 'Aprendizaje y rendición de cuentas',
    desc: 'La medición de resultados permite ajustar acciones y compartir lecciones entre regiones.'
  }
];

const transformativeGoals = [
  {
    title: 'Fin de muertes maternas evitables',
    desc: 'Cada embarazada debe recibir atención adecuada, oportuna y con respeto.'
  },
  {
    title: 'Cero necesidad insatisfecha',
    desc: 'Las personas deben poder decidir libremente sobre su salud y su proyecto de vida.'
  },
  {
    title: 'Cero violencia basada en género',
    desc: 'La prevención y la respuesta institucional son parte central del desarrollo sostenible.'
  },
  {
    title: 'Juventudes con potencial',
    desc: 'Las personas jóvenes necesitan información, oportunidades y entornos seguros para prosperar.'
  }
];

onMounted(() => {
  document.title = 'MNMNS y cooperación internacional';
  window.scrollTo(0, 0);
});
</script>
