<template>
  <header class="fixed top-0 z-50 w-full bg-white/95 backdrop-blur-sm shadow-sm transition-all duration-300">
    <div class="mx-auto flex h-20 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
      <router-link to="/" class="flex items-center gap-3">
        <div class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-2xl bg-white p-1.5 shadow-sm ring-1 ring-gray-100">
          <img src="/img/logo1.jpg" alt="MNMNS Bolivia" class="h-full w-full object-contain" />
        </div>
        <div class="flex flex-col">
          <span class="text-lg font-bold leading-tight text-[#F97316]">Mesa de Maternidad</span>
          <span class="text-xs font-medium text-gray-500">Y Nacimiento Seguro</span>
        </div>
      </router-link>

      <nav class="hidden items-center gap-5 lg:flex">
        <template v-for="section in menuSections" :key="section.key">
          <div
            v-if="section.children"
            class="relative"
            @mouseenter="openDesktopMenu = section.key"
            @mouseleave="openDesktopMenu = null"
          >
            <button
              class="flex items-center gap-2 rounded-full px-3 py-2 text-sm font-semibold transition-colors"
              :class="isSectionActive(section) ? 'text-[#F97316] bg-orange-50' : 'text-gray-700 hover:text-[#991a73] hover:bg-orange-50'"
            >
              {{ section.label }}
              <i class="pi text-xs" :class="openDesktopMenu === section.key ? 'pi-angle-up' : 'pi-angle-down'"></i>
            </button>

            <transition name="menu-fade">
              <div
                v-if="openDesktopMenu === section.key"
                class="absolute left-0 top-full mt-2 w-80 rounded-2xl border border-orange-100 bg-white p-3 shadow-xl"
              >
                <router-link
                  v-for="child in section.children"
                  :key="child.key"
                  :to="child.to"
                  class="block rounded-xl px-4 py-3 text-sm font-medium transition-colors"
                  :class="isRouteActive(child.to) ? 'bg-orange-50 text-[#F97316]' : 'text-gray-700 hover:bg-orange-50 hover:text-[#991a73]'"
                >
                  {{ child.label }}
                </router-link>
              </div>
            </transition>
          </div>

          <router-link
            v-else
            :to="section.to"
            class="rounded-full px-3 py-2 text-sm font-semibold transition-colors"
            :class="isRouteActive(section.to) ? 'text-[#F97316] bg-orange-50' : 'text-gray-700 hover:text-[#991a73] hover:bg-orange-50'"
          >
            {{ section.label }}
          </router-link>
        </template>
      </nav>

      <div class="hidden items-center gap-3 lg:flex">
        <div class="group relative">
          <button
            class="flex items-center gap-2 rounded-full border border-teal-100 bg-white px-4 py-2 text-sm font-bold text-[#0F766E] shadow-sm transition hover:border-teal-200 hover:bg-teal-50"
            type="button"
          >
            {{ $t('nav.public_sector') }}
            <i class="pi pi-chevron-down text-[0.7rem] transition group-hover:rotate-180"></i>
          </button>

          <div class="invisible absolute right-0 top-full z-50 mt-3 w-[340px] translate-y-2 opacity-0 transition duration-200 group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100">
            <div class="overflow-hidden rounded-[1.5rem] border border-teal-100 bg-white p-3 shadow-[0_25px_80px_-35px_rgba(15,118,110,0.5)]">
              <p class="px-3 pb-2 text-[0.65rem] font-black uppercase tracking-[0.3em] text-slate-400">{{ $t('nav.modulos_funcionales') }}</p>
              <router-link
                v-for="module in publicSectorModules"
                :key="module.path"
                :to="module.path"
                class="flex items-start gap-3 rounded-2xl px-3 py-3 transition hover:bg-teal-50"
              >
                <span class="mt-0.5 flex h-10 w-10 items-center justify-center rounded-2xl bg-gradient-to-br text-white shadow-sm" :class="module.accent">
                  <i :class="module.icon"></i>
                </span>
                <span class="flex-1">
                  <span class="block text-sm font-bold text-slate-900">{{ module.label }}</span>
                  <span class="block text-xs text-slate-500">{{ module.description }}</span>
                </span>
              </router-link>
            </div>
          </div>
        </div>

        <div class="hidden items-center gap-3 lg:flex">
          <router-link
            to="/login"
            class="rounded-full border-2 border-[#F97316] px-5 py-2 text-sm font-bold text-[#F97316] transition-all hover:bg-orange-50"
          >
            {{ $t('nav.iniciar_sesion') }}
          </router-link>
          <a
            href="/doname"
            target="_blank"
            rel="noreferrer"
            class="rounded-full bg-gradient-to-r from-[#F97316] to-[#991a73] px-5 py-2 text-sm font-bold text-white shadow-md transition-colors hover:from-[#EA580C] hover:to-[#7d155f]"
          >
            {{ $t('nav.doname') }}
          </a>

          <!-- Language Switcher Desktop -->
          <div class="relative group">
            <button class="flex items-center gap-1 rounded-full border border-gray-200 bg-white px-4 py-2 text-sm font-bold text-gray-700 shadow-sm transition hover:border-[#F97316] hover:text-[#F97316]">
              <i class="pi pi-globe"></i> {{ locale === 'es' ? 'ES' : locale === 'ay' ? 'AY' : 'QU' }}
            </button>
            <div class="invisible absolute right-0 top-full z-50 mt-2 w-32 translate-y-2 opacity-0 transition duration-200 group-hover:visible group-hover:translate-y-0 group-hover:opacity-100">
              <div class="overflow-hidden rounded-[1rem] border border-gray-100 bg-white p-2 shadow-lg">
                <button @click="changeGoogleLanguage('es')" class="block w-full rounded-lg text-left px-3 py-2 text-sm hover:bg-[#F97316]/10" :class="locale === 'es' ? 'text-[#F97316] font-bold' : 'text-gray-700'">Español</button>
                <button @click="changeGoogleLanguage('ay')" class="block w-full rounded-lg text-left px-3 py-2 text-sm hover:bg-[#F97316]/10" :class="locale === 'ay' ? 'text-[#F97316] font-bold' : 'text-gray-700'">Aymara</button>
                <button @click="changeGoogleLanguage('qu')" class="block w-full rounded-lg text-left px-3 py-2 text-sm hover:bg-[#F97316]/10" :class="locale === 'qu' ? 'text-[#F97316] font-bold' : 'text-gray-700'">Quechua</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <button class="text-[#991a73] lg:hidden" aria-label="Abrir menú" @click="toggleDrawer">
        <i class="pi pi-bars text-2xl"></i>
      </button>
    </div>

    <Transition name="fade">
      <div v-if="isDrawerOpen" class="fixed inset-0 z-40 bg-black/50" @click="closeDrawer"></div>
    </Transition>

    <Transition name="slide">
      <aside
        v-if="isDrawerOpen"
        class="fixed right-0 top-0 z-50 flex h-full w-80 max-w-[88vw] flex-col bg-white shadow-2xl"
      >
        <div class="flex items-center justify-between border-b border-gray-100 p-4">
          <span class="font-bold text-[#991a73]">Navegacion</span>
          <button class="text-gray-500 transition-colors hover:text-red-500" aria-label="Cerrar menú" @click="closeDrawer">
            <i class="pi pi-times text-xl"></i>
          </button>
        </div>

        <div class="flex-1 overflow-y-auto p-4">
          <div class="space-y-2">
            <template v-for="section in menuSections" :key="section.key">
              <div v-if="section.children" class="rounded-xl border border-gray-100">
                <button
                  class="flex w-full items-center justify-between rounded-xl px-4 py-3 text-left text-sm font-semibold text-gray-700 transition-colors hover:bg-orange-50 hover:text-[#991a73]"
                  @click="toggleMobileSection(section.key)"
                >
                  {{ section.label }}
                  <i class="pi text-xs" :class="expandedMobileSection === section.key ? 'pi-angle-up' : 'pi-angle-down'"></i>
                </button>
                <div v-if="expandedMobileSection === section.key" class="space-y-1 px-2 pb-3">
                  <router-link
                    v-for="child in section.children"
                    :key="child.key"
                    :to="child.to"
                    class="block rounded-lg px-3 py-2 text-sm transition-colors"
                    :class="isRouteActive(child.to) ? 'bg-orange-50 text-[#F97316] font-medium' : 'text-gray-600 hover:bg-orange-50 hover:text-[#991a73]'"
                    @click="closeDrawer"
                  >
                    {{ child.label }}
                  </router-link>
                </div>
              </div>

              <router-link
                v-else
                :to="section.to"
                class="block rounded-xl px-4 py-3 text-sm font-semibold transition-colors"
                :class="isRouteActive(section.to) ? 'bg-orange-50 text-[#F97316]' : 'text-gray-700 hover:bg-orange-50 hover:text-[#991a73]'"
                @click="closeDrawer"
              >
                {{ section.label }}
              </router-link>
            </template>

            <details class="rounded-xl border border-teal-100 bg-white">
              <summary class="flex cursor-pointer list-none items-center justify-between rounded-xl px-4 py-3 text-sm font-semibold text-[#0F766E]">
                <span>{{ $t('nav.public_sector') }}</span>
                <i class="pi pi-chevron-down text-xs"></i>
              </summary>
              <div class="space-y-2 px-3 pb-3">
                <router-link
                  v-for="module in publicSectorModules"
                  :key="module.path"
                  :to="module.path"
                  class="flex items-start gap-3 rounded-xl px-3 py-3 text-sm transition hover:bg-teal-50"
                  @click="closeDrawer"
                >
                  <span class="mt-0.5 flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br text-white" :class="module.accent">
                    <i :class="module.icon"></i>
                  </span>
                  <span>
                    <span class="block font-bold text-slate-900">{{ module.label }}</span>
                    <span class="block text-xs text-slate-500">{{ module.description }}</span>
                  </span>
                </router-link>
              </div>
            </details>

            <a
              href="/doname"
              target="_blank"
              rel="noreferrer"
              class="mt-2 block rounded-xl bg-gradient-to-r from-[#F97316] to-[#991a73] px-4 py-3 text-center text-sm font-bold text-white transition-colors hover:from-[#EA580C] hover:to-[#7d155f]"
              @click="closeDrawer"
            >
              {{ $t('nav.doname') }}
            </a>

            <!-- Language Switcher Mobile -->
            <div class="mt-4 border-t border-gray-100 pt-4">
              <p class="px-4 text-xs font-bold text-gray-400 mb-2 uppercase">Idioma</p>
              <button @click="changeGoogleLanguage('es'); closeDrawer()" class="block w-full text-left py-3 px-4 rounded-xl text-sm font-semibold text-gray-700 hover:bg-[#F97316]/10" :class="{'text-[#F97316] font-bold': locale === 'es'}">Español</button>
              <button @click="changeGoogleLanguage('ay'); closeDrawer()" class="block w-full text-left py-3 px-4 rounded-xl text-sm font-semibold text-gray-700 hover:bg-[#F97316]/10" :class="{'text-[#F97316] font-bold': locale === 'ay'}">Aymara</button>
              <button @click="changeGoogleLanguage('qu'); closeDrawer()" class="block w-full text-left py-3 px-4 rounded-xl text-sm font-semibold text-gray-700 hover:bg-[#F97316]/10" :class="{'text-[#F97316] font-bold': locale === 'qu'}">Quechua</button>
            </div>

            <router-link
              to="/login"
              class="mt-2 block rounded-xl border-2 border-[#F97316] px-4 py-3 text-center text-sm font-bold text-[#F97316] transition-all hover:bg-orange-50"
              @click="closeDrawer"
            >
              {{ $t('nav.iniciar_sesion') }}
            </router-link>
          </div>
        </div>
      </aside>
    </Transition>
  </header>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useI18n } from 'vue-i18n';

type ChildLink = {
  key: string;
  label: string;
  to: string;
};

type MenuSection = {
  key: string;
  label: string;
  to: string;
  children?: ChildLink[];
};

const route = useRoute();
const { t, locale } = useI18n({ useScope: 'global' });

const menuSections = computed<MenuSection[]>(() => [
  { key: 'inicio', label: t('nav.home'), to: '/' },
  {
    key: 'nuestra-labor',
    label: t('nav.nuestra_labor'),
    to: '/nuestra-labor',
    children: [
      { key: 'labor-conocenos', label: t('nav.about'), to: '/conocenos' },
      { key: 'labor-bolivia', label: t('nav.mnmns_bolivia'), to: '/nuestra-labor/mnmns-en-bolivia' },
      { key: 'labor-representante', label: t('nav.representante'), to: '/nuestra-labor/representante' },
      {
        key: 'labor-lac',
        label: t('nav.coop_regional'),
        to: '/nuestra-labor/mnmns-america-latina-caribe'
      },
      { key: 'labor-global', label: t('nav.coop_internacional'), to: '/nuestra-labor/mnmns-global' }
    ]
  },
  {
    key: 'que-hacemos',
    label: t('nav.que_hacemos'),
    to: '/que-hacemos',
    children: [
      {
        key: 'qh-politicas',
        label: t('nav.politicas_publicas'),
        to: '/que-hacemos/politicas-publicas-rendicion-cuentas'
      },
      {
        key: 'qh-acceso',
        label: t('nav.acceso_calidad'),
        to: '/que-hacemos/acceso-calidad-servicios-atencion'
      },
      {
        key: 'qh-transformacion',
        label: t('nav.transformacion_normas'),
        to: '/que-hacemos/transformacion-normas-sociales-genero'
      },
      { key: 'qh-datos', label: t('nav.data'), to: '/datos' }
    ]
  },
  {
    key: 'comunidad',
    label: t('nav.comunidad'),
    to: '/comunidad',
    children: [
      { key: 'com-blog', label: t('nav.blog'), to: '/blog' },
      { key: 'com-noticias', label: t('nav.news'), to: '/noticias' },
      { key: 'com-publicaciones', label: t('nav.publicaciones'), to: '/comunidad/publicaciones' },
      { key: 'com-campanas', label: t('nav.campanas'), to: '/comunidad/campanas' },
      { key: 'com-multimedia', label: t('nav.multimedia'), to: '/comunidad/multimedia' },
      { key: 'com-instituciones', label: t('nav.institutions'), to: '/instituciones' }
    ]
  },
  { key: 'contactanos', label: t('nav.contact'), to: '/contactanos' }
]);

const publicSectorModules = computed(() => [
  {
    path: '/sector-publico/asistente-obstetrico',
    label: t('nav.asistente_obstetrico'),
    description: t('nav.asistente_desc'),
    icon: 'pi pi-calendar',
    accent: 'from-[#F97316] to-[#FB7185]'
  },
  {
    path: '/sector-publico/geolocalizador',
    label: t('nav.geolocalizador'),
    description: t('nav.geolocalizador_desc'),
    icon: 'pi pi-map-marker',
    accent: 'from-[#0F766E] to-[#14B8A6]'
  },
  {
    path: '/dashboard/sector-publico/near-miss',
    label: t('nav.morbilidad'),
    description: t('nav.morbilidad_desc'),
    icon: 'pi pi-heartbeat',
    accent: 'from-[#EC4899] to-[#F43F5E]'
  },
  {
    path: '/sector-publico/alarma-panico',
    label: t('nav.senales_alarma'),
    description: t('nav.senales_desc'),
    icon: 'pi pi-bell',
    accent: 'from-[#991B1B] to-[#F97316]'
  },
  {
    path: '/sector-publico/salud-adolescente',
    label: t('nav.salud_adolescente'),
    description: t('nav.salud_desc'),
    icon: 'pi pi-comments',
    accent: 'from-[#7C3AED] to-[#F97316]'
  }
]);

const isDrawerOpen = ref(false);
const openDesktopMenu = ref<string | null>(null);
const expandedMobileSection = ref<string | null>(null);

const toggleDrawer = () => {
  isDrawerOpen.value = !isDrawerOpen.value;
  if (!isDrawerOpen.value) {
    expandedMobileSection.value = null;
  }
};

const closeDrawer = () => {
  isDrawerOpen.value = false;
  expandedMobileSection.value = null;
};

const toggleMobileSection = (sectionKey: string) => {
  expandedMobileSection.value = expandedMobileSection.value === sectionKey ? null : sectionKey;
};

const isRouteActive = (to: string) => {
  return route.path === to || (to !== '/' && route.path.startsWith(`${to}/`));
};

const isSectionActive = (section: MenuSection) => {
  if (isRouteActive(section.to)) {
    return true;
  }

  if (!section.children) {
    return false;
  }

  return section.children.some((child) => isRouteActive(child.to));
};

const changeGoogleLanguage = (langCode: string) => {
  locale.value = langCode;
  
  // Try to use the Google Translate select element if it's rendered
  const select = document.querySelector('.goog-te-combo') as HTMLSelectElement;
  if (select) {
    select.value = langCode;
    select.dispatchEvent(new Event('change'));
  } else {
    // Fallback: Set cookie and reload
    document.cookie = `googtrans=/es/${langCode}; path=/`;
    document.cookie = `googtrans=/es/${langCode}; path=/; domain=${window.location.hostname}`;
    window.location.reload();
  }
};
</script>

<style scoped>
.menu-fade-enter-active,
.menu-fade-leave-active {
  transition: all 0.2s ease;
}

.menu-fade-enter-from,
.menu-fade-leave-to {
  opacity: 0;
  transform: translateY(8px);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
  transition: transform 0.25s ease;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
}
</style>
