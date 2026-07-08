<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <PageHero
      :kicker="$t('representante_page.hero_kicker')"
      :title="$t('representante_page.hero_title')"
      :subtitle="$t('representante_page.hero_subtitle')"
      backgroundImage="/img/fondo2.jpg"
    />

    <!-- Sección de Representantes -->
    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8">
      <div class="mb-12">
        <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">{{ $t('representante_page.representatives_section_kicker') }}</p>
        <h2 class="mt-3 text-4xl font-extrabold text-gray-900">{{ $t('representante_page.representatives_section_title') }}</h2>
        <p class="mt-4 max-w-3xl text-gray-600">
          {{ $t('representante_page.representatives_section_description') }}
        </p>
      </div>

      <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-5">
        <div v-for="representative in representatives" :key="representative.id" class="group overflow-hidden rounded-[2rem] bg-white shadow-lg ring-1 ring-gray-200 transition-all duration-300 hover:shadow-2xl hover:ring-orange-200">
          <!-- Foto del representante -->
          <div class="relative overflow-hidden bg-gradient-to-br from-orange-100 to-yellow-100 h-64">
            <img 
              :src="representative.photo" 
              :alt="representative.name"
              class="h-full w-full object-cover"
            />
          </div>

          <!-- Logo institución -->
          <div class="flex justify-center px-4 pt-4">
            <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-orange-50 ring-1 ring-orange-200">
              <img 
                v-if="representative.institutionLogo"
                :src="representative.institutionLogo" 
                :alt="representative.institution"
                class="h-12 w-12 object-contain"
              />
              <span v-else class="text-2xl text-orange-500">🏛️</span>
            </div>
          </div>

          <!-- Información -->
          <div class="px-5 pb-6 pt-4">
            <h3 class="text-lg font-bold text-gray-900">{{ representative.name }}</h3>
            <p class="mt-1 text-sm font-semibold text-[#F97316]">{{ representative.specialty }}</p>
            <p class="mt-2 text-sm text-gray-500 font-medium">{{ representative.institution }}</p>

            <!-- Breve biografía -->
            <p class="mt-3 text-xs text-gray-600 line-clamp-3">
              {{ representative.biography }}
            </p>

            <!-- Enlaces de redes sociales -->
            <div class="mt-4 flex gap-3">
              <a 
                v-if="representative.linkedin"
                :href="representative.linkedin"
                target="_blank"
                rel="noopener noreferrer"
                class="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-50 text-blue-600 hover:bg-blue-100 transition-colors"
                :title="$t('representante_page.linkedin_title')"
              >
                <span class="text-sm font-bold">in</span>
              </a>
              <a 
                v-if="representative.facebook"
                :href="representative.facebook"
                target="_blank"
                rel="noopener noreferrer"
                class="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-50 text-blue-700 hover:bg-blue-100 transition-colors"
                :title="$t('representante_page.facebook_title')"
              >
                <span class="text-sm font-bold">f</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sección de Contexto Institucional -->
    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="mb-12">
        <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">{{ $t('representante_page.context_section_kicker') }}</p>
        <h2 class="mt-3 text-4xl font-extrabold text-gray-900">{{ $t('representante_page.context_section_title') }}</h2>
      </div>

      <div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
        <!-- Card: Coordinación Técnica -->
        <div class="rounded-[1.5rem] border border-orange-100 bg-gradient-to-br from-[#fff7ed] to-white p-8 shadow-md hover:shadow-lg transition-shadow">
          <div class="flex h-14 w-14 items-center justify-center rounded-full bg-[#F97316]/10">
            <span class="text-2xl">🏛️</span>
          </div>
          <h3 class="mt-4 text-xl font-bold text-gray-900">{{ $t('representante_page.coordination_card_title') }}</h3>
          <p class="mt-3 text-gray-600">
            {{ $t('representante_page.coordination_card_description') }}
          </p>
          <div class="mt-5 flex flex-wrap gap-2">
            <span class="rounded-full bg-orange-100 px-3 py-1 text-xs font-semibold text-[#F97316]">{{ $t('representante_page.coordination_tag1') }}</span>
            <span class="rounded-full bg-orange-100 px-3 py-1 text-xs font-semibold text-[#F97316]">{{ $t('representante_page.coordination_tag2') }}</span>
          </div>
        </div>

        <!-- Card: Fortalecimiento de Capacidades -->
        <div class="rounded-[1.5rem] border border-orange-100 bg-gradient-to-br from-[#fff7ed] to-white p-8 shadow-md hover:shadow-lg transition-shadow">
          <div class="flex h-14 w-14 items-center justify-center rounded-full bg-[#F97316]/10">
            <span class="text-2xl">📚</span>
          </div>
          <h3 class="mt-4 text-xl font-bold text-gray-900">{{ $t('representante_page.capacity_card_title') }}</h3>
          <p class="mt-3 text-gray-600">
            {{ $t('representante_page.capacity_card_description') }}
          </p>
          <div class="mt-5 flex flex-wrap gap-2">
            <span class="rounded-full bg-orange-100 px-3 py-1 text-xs font-semibold text-[#F97316]">{{ $t('representante_page.capacity_tag1') }}</span>
            <span class="rounded-full bg-orange-100 px-3 py-1 text-xs font-semibold text-[#F97316]">{{ $t('representante_page.capacity_tag2') }}</span>
          </div>
        </div>

        <!-- Card: Monitoreo y Evaluación -->
        <div class="rounded-[1.5rem] border border-orange-100 bg-gradient-to-br from-[#fff7ed] to-white p-8 shadow-md hover:shadow-lg transition-shadow">
          <div class="flex h-14 w-14 items-center justify-center rounded-full bg-[#F97316]/10">
            <span class="text-2xl">📊</span>
          </div>
          <h3 class="mt-4 text-xl font-bold text-gray-900">{{ $t('representante_page.monitoring_card_title') }}</h3>
          <p class="mt-3 text-gray-600">
            {{ $t('representante_page.monitoring_card_description') }}
          </p>
          <div class="mt-5 flex flex-wrap gap-2">
            <span class="rounded-full bg-orange-100 px-3 py-1 text-xs font-semibold text-[#F97316]">{{ $t('representante_page.monitoring_tag1') }}</span>
            <span class="rounded-full bg-orange-100 px-3 py-1 text-xs font-semibold text-[#F97316]">{{ $t('representante_page.monitoring_tag2') }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Sección de Impacto e Historia -->
    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="rounded-[2rem] bg-gradient-to-r from-gray-900 to-gray-800 p-12 text-white shadow-2xl overflow-hidden relative">
        <div class="absolute -right-20 -top-20 h-40 w-40 bg-[#F97316]/20 rounded-full blur-3xl"></div>
        <div class="relative z-10">
          <p class="text-sm font-bold uppercase tracking-[0.2em] text-orange-300">{{ $t('representante_page.mission_kicker') }}</p>
          <h2 class="mt-4 text-4xl font-extrabold md:text-5xl">{{ $t('representante_page.mission_title') }}</h2>
          <p class="mt-6 max-w-3xl text-lg text-gray-300 leading-relaxed">
            {{ $t('representante_page.mission_description') }}
          </p>

          <div class="mt-10 grid grid-cols-1 gap-6 md:grid-cols-3">
            <div class="rounded-2xl bg-white/10 p-6 backdrop-blur-sm">
              <p class="text-3xl font-bold text-orange-300">5</p>
              <p class="mt-2 text-sm font-semibold text-gray-300">{{ $t('representante_page.stats_reps_title') }}</p>
              <p class="mt-1 text-xs text-gray-400">{{ $t('representante_page.stats_reps_description') }}</p>
            </div>
            <div class="rounded-2xl bg-white/10 p-6 backdrop-blur-sm">
              <p class="text-3xl font-bold text-orange-300">9</p>
              <p class="mt-2 text-sm font-semibold text-gray-300">{{ $t('representante_page.stats_depts_title') }}</p>
              <p class="mt-1 text-xs text-gray-400">{{ $t('representante_page.stats_depts_description') }}</p>
            </div>
            <div class="rounded-2xl bg-white/10 p-6 backdrop-blur-sm">
              <p class="text-3xl font-bold text-orange-300">100%</p>
              <p class="mt-2 text-sm font-semibold text-gray-300">{{ $t('representante_page.stats_commitment_title') }}</p>
              <p class="mt-1 text-xs text-gray-400">{{ $t('representante_page.stats_commitment_description') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sección de Áreas Clave -->
    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="mb-12">
        <p class="text-sm font-bold uppercase tracking-[0.2em] text-[#F97316]">{{ $t('representante_page.pillars_kicker') }}</p>
        <h2 class="mt-3 text-4xl font-extrabold text-gray-900">{{ $t('representante_page.pillars_title') }}</h2>
        <p class="mt-4 max-w-3xl text-gray-600">
          {{ $t('representante_page.pillars_description') }}
        </p>
      </div>

      <div class="grid grid-cols-1 gap-8 md:grid-cols-2">
        <!-- Pilar 1 -->
        <div class="rounded-[2rem] bg-white p-10 shadow-lg ring-1 ring-gray-100 hover:shadow-xl transition-shadow">
          <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-orange-100">
            <span class="text-3xl">🏥</span>
          </div>
          <h3 class="mt-6 text-2xl font-bold text-gray-900">{{ $t('representante_page.pillar1_title') }}</h3>
          <p class="mt-4 text-gray-600">
            {{ $t('representante_page.pillar1_description') }}
          </p>
          <ul class="mt-6 space-y-2">
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar1_item1') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar1_item2') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar1_item3') }}</span>
            </li>
          </ul>
        </div>

        <!-- Pilar 2 -->
        <div class="rounded-[2rem] bg-white p-10 shadow-lg ring-1 ring-gray-100 hover:shadow-xl transition-shadow">
          <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-orange-100">
            <span class="text-3xl">🤝</span>
          </div>
          <h3 class="mt-6 text-2xl font-bold text-gray-900">{{ $t('representante_page.pillar2_title') }}</h3>
          <p class="mt-4 text-gray-600">
            {{ $t('representante_page.pillar2_description') }}
          </p>
          <ul class="mt-6 space-y-2">
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar2_item1') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar2_item2') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar2_item3') }}</span>
            </li>
          </ul>
        </div>

        <!-- Pilar 3 -->
        <div class="rounded-[2rem] bg-white p-10 shadow-lg ring-1 ring-gray-100 hover:shadow-xl transition-shadow">
          <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-orange-100">
            <span class="text-3xl">📋</span>
          </div>
          <h3 class="mt-6 text-2xl font-bold text-gray-900">{{ $t('representante_page.pillar3_title') }}</h3>
          <p class="mt-4 text-gray-600">
            {{ $t('representante_page.pillar3_description') }}
          </p>
          <ul class="mt-6 space-y-2">
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar3_item1') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar3_item2') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar3_item3') }}</span>
            </li>
          </ul>
        </div>

        <!-- Pilar 4 -->
        <div class="rounded-[2rem] bg-white p-10 shadow-lg ring-1 ring-gray-100 hover:shadow-xl transition-shadow">
          <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-orange-100">
            <span class="text-3xl">📊</span>
          </div>
          <h3 class="mt-6 text-2xl font-bold text-gray-900">{{ $t('representante_page.pillar4_title') }}</h3>
          <p class="mt-4 text-gray-600">
            {{ $t('representante_page.pillar4_description') }}
          </p>
          <ul class="mt-6 space-y-2">
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar4_item1') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar4_item2') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-[#F97316] font-bold">✓</span>
              <span class="text-sm text-gray-600">{{ $t('representante_page.pillar4_item3') }}</span>
            </li>
          </ul>
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
import { useI18n } from 'vue-i18n'; // Add this import

const { t } = useI18n(); // Initialize t function

interface Representative {
  id: number;
  name: string;
  specialty: string;
  institution: string;
  photo: string;
  institutionLogo?: string;
  biography: string;
  linkedin?: string;
  facebook?: string;
}

const representatives: Representative[] = [
  {
    id: 1,
    name: 'Daniel Rojas Loayza',
    specialty: 'Especialista en Salud Materna y Neonatal',
    institution: 'Ministerio de Salud',
    photo: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500&h=500&fit=crop',
    institutionLogo: '',
    biography: 'Especialista boliviano destacado en salud materna y neonatal que lidera procesos técnicos y políticos de la MNMNS. Su labor se centra en fortalecer políticas públicas y reducir mortalidad materna.',
    linkedin: 'https://linkedin.com',
    facebook: 'https://facebook.com'
  },
  {
    id: 2,
    name: 'Representante 2',
    specialty: 'Especialidad profesional',
    institution: 'Institución representada',
    photo: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=500&h=500&fit=crop',
    institutionLogo: '',
    biography: 'Información de la biografía del representante 2 que podrás actualizar con los datos correctos cuando dispongas de ellos.',
    linkedin: 'https://linkedin.com',
    facebook: 'https://facebook.com'
  },
  {
    id: 3,
    name: 'Representante 3',
    specialty: 'Especialidad profesional',
    institution: 'Institución representada',
    photo: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=500&h=500&fit=crop',
    institutionLogo: '',
    biography: 'Información de la biografía del representante 3 que podrás actualizar con los datos correctos cuando dispongas de ellos.',
    linkedin: 'https://linkedin.com',
    facebook: 'https://facebook.com'
  },
  {
    id: 4,
    name: 'Representante 4',
    specialty: 'Especialidad profesional',
    institution: 'Institución representada',
    photo: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=500&h=500&fit=crop',
    institutionLogo: '',
    biography: 'Información de la biografía del representante 4 que podrás actualizar con los datos correctos cuando dispongas de ellos.',
    linkedin: 'https://linkedin.com',
    facebook: 'https://facebook.com'
  },
  {
    id: 5,
    name: 'Representante 5',
    specialty: 'Especialidad profesional',
    institution: 'Institución representada',
    photo: 'https://images.unsplash.com/photo-1507539332640-34d4d73ba631?w=500&h=500&fit=crop',
    institutionLogo: '',
    biography: 'Información de la biografía del representante 5 que podrás actualizar con los datos correctos cuando dispongas de ellos.',
    linkedin: 'https://linkedin.com',
    facebook: 'https://facebook.com'
  }
];

const highlights = [
  { title: 'Especialidad', desc: 'Salud materna, neonatal y derechos sexuales y reproductivos con enfoque de equidad.' },
  { title: 'Enfoque', desc: 'Prevención de muertes maternas evitables y ampliación de acceso a servicios de calidad.' },
  { title: 'Ámbito', desc: 'Coordinación interinstitucional y liderazgo en salud reproductive en Bolivia.' }
];

const bibliography = [
  {
    title: 'Formación en Salud Materna y Neonatal',
    desc: 'Especialización profesional enfocada en calidad de atención, prevención de complications obstetricias y reducción de mortalidad.'
  },
  {
    title: 'Experiencia en Políticas Públicas en Salud',
    desc: 'Participación en el diseño e implementación de políticas públicas nacionales alineadas con derechos y evidencia científica.'
  },
  {
    title: 'Liderazgo en Coordinación Interinstitucional',
    desc: 'Trayectoria en articulación de alianzas multisectoriales entre Estado, cooperación internacional y sociedad civil.'
  }
];

const responsibilities = [
  {
    title: 'Fortalecimiento de capacidades técnicas',
    desc: 'Impulsar adopción de protocolos basados en evidencia para parto seguro, prevención de hemorragias posparto y fortalecimiento de redes de referencia obstétrica.'
  },
  {
    title: 'Promoción de atención respetuosa e intercultural',
    desc: 'Integrar saberes de comunidades indígenas y campesinas con medicina académica, reconociendo prácticas locales bajo la política SAFCI.'
  },
  {
    title: 'Análisis y monitoreo de indicadores',
    desc: 'Coordinar evaluación de indicadores de salud materna-neonatal y análisis de casos de mortalidad para generar recomendaciones estratégicas.'
  }
];

const sources = [
  'Doc: representante.txt - Perfil completo del especialista',
  'Ministerio de Salud y Deportes de Bolivia',
  'Mesa Nacional de Maternidad y Nacimiento Seguros (MNMNS)',
  'Sistema de Naciones Unidas en Bolivia'
];

onMounted(() => {
  document.title = t('representante_page.document_title');
  window.scrollTo(0, 0);
});
</script>