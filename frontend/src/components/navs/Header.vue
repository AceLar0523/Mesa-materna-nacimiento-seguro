<template>
  <div class="main-nav bg-white/90 backdrop-blur-md sticky top-0 z-50 shadow-sm transition-all duration-300">
    <div class="nav-items max-w-7xl mx-auto flex justify-between items-center p-4">
      <router-link to="/" class="logo flex items-center gap-2">
        <img src="/img/logo1.jpg" alt="MNMNS Maternidad Segura Logo" class="h-10 w-auto rounded-full object-contain" />
        <span class="font-bold text-[#F97316] text-lg hidden md:block">
          Mesa de Maternidad
        </span>
      </router-link>

      <div class="flex gap-2 md:hidden">
        <button class="mobile-menu-button text-[#F97316]" aria-label="Abrir Búsqueda" @click="openSearch">
          <i class="pi pi-search text-xl"></i>
        </button>
        <button class="mobile-menu-button text-[#F97316]" aria-label="Abrir Menú" @click="toggleDrawer">
          <i class="pi pi-bars text-xl"></i>
        </button>
      </div>

      <nav class="desktop-nav hidden md:flex items-center gap-6 font-medium text-gray-700">
        <FadeContent blur>
          <div class="flex gap-6">
            <router-link 
              v-for="link in navLinks" 
              :key="link.path" 
              :to="link.path"
              class="relative group py-2 text-sm hover:text-[#F97316] transition-colors duration-300"
            >
              {{ link.name }}
              <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#F97316] transition-all duration-300 group-hover:w-full"></span>
            </router-link>

            <!-- Language Switcher Desktop -->
            <div class="relative group flex items-center">
              <button class="flex items-center gap-1 py-2 text-sm text-gray-700 hover:text-[#F97316] transition-colors">
                <i class="pi pi-globe"></i> {{ t('nav.language') }}
              </button>
              <div class="absolute top-full right-0 mt-2 w-32 bg-white border border-gray-100 rounded-lg shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                <button @click="changeGoogleLanguage('es')" class="block w-full text-left px-4 py-2 text-sm hover:bg-[#F97316]/10" :class="locale === 'es' ? 'text-[#F97316] font-bold' : 'text-gray-700'">{{ t('nav.es') }}</button>
                <button @click="changeGoogleLanguage('ay')" class="block w-full text-left px-4 py-2 text-sm hover:bg-[#F97316]/10" :class="locale === 'ay' ? 'text-[#F97316] font-bold' : 'text-gray-700'">{{ t('nav.ay') }}</button>
                <button @click="changeGoogleLanguage('qu')" class="block w-full text-left px-4 py-2 text-sm hover:bg-[#F97316]/10" :class="locale === 'qu' ? 'text-[#F97316] font-bold' : 'text-gray-700'">{{ t('nav.qu') }}</button>
              </div>
            </div>
          </div>
        </FadeContent>

        <FadeContent blur>
          <button class="text-[#F97316] hover:text-[#EA580C] transition-colors ml-2" @click="openSearch">
            <i class="pi pi-search text-lg"></i>
          </button>
        </FadeContent>
      </nav>
    </div>

    <Transition name="fade">
      <div v-if="isDrawerOpen" class="drawer-overlay fixed inset-0 bg-black/50 z-40" @click="closeDrawer"></div>
    </Transition>
    
    <Transition name="slide">
      <div v-if="isDrawerOpen" class="drawer-content fixed top-0 right-0 h-full w-64 bg-white z-50 shadow-xl flex flex-col">
        <div class="drawer-header p-4 border-b border-gray-100 flex justify-between items-center">
          <span class="font-bold text-[#F97316]">Menú</span>
          <button class="close-button text-gray-500 hover:text-red-500 transition-colors" aria-label="Cerrar Menú" @click="closeDrawer">
            <i class="pi pi-times text-xl"></i>
          </button>
        </div>

        <div class="drawer-body flex-1 overflow-y-auto p-4 flex flex-col gap-4">
          <router-link 
            v-for="link in navLinks" 
            :key="link.path" 
            :to="link.path"
            @click="closeDrawer"
            class="block py-3 px-4 rounded-lg text-gray-700 hover:bg-[#F97316]/10 hover:text-[#F97316] transition-all duration-200"
          >
            {{ link.name }}
          </router-link>

          <div class="border-t border-gray-100 pt-4 mt-2">
            <p class="px-4 text-xs font-bold text-gray-400 mb-2 uppercase">{{ t('nav.language') }}</p>
            <button @click="changeGoogleLanguage('es'); closeDrawer()" class="block w-full text-left py-3 px-4 rounded-lg text-gray-700 hover:bg-[#F97316]/10" :class="{'text-[#F97316] font-bold': locale === 'es'}">{{ t('nav.es') }}</button>
            <button @click="changeGoogleLanguage('ay'); closeDrawer()" class="block w-full text-left py-3 px-4 rounded-lg text-gray-700 hover:bg-[#F97316]/10" :class="{'text-[#F97316] font-bold': locale === 'ay'}">{{ t('nav.ay') }}</button>
            <button @click="changeGoogleLanguage('qu'); closeDrawer()" class="block w-full text-left py-3 px-4 rounded-lg text-gray-700 hover:bg-[#F97316]/10" :class="{'text-[#F97316] font-bold': locale === 'qu'}">{{ t('nav.qu') }}</button>
          </div>
        </div>
      </div>
    </Transition>

    <SearchDialog :is-open="isSearchOpen" @close="closeSearch" @open="openSearch" />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import FadeContent from '../../content/Animations/FadeContent/FadeContent.vue';
import SearchDialog from '../common/SearchDialog.vue';

const isDrawerOpen = ref(false);
const isSearchOpen = ref(false);
const route = useRoute();
const router = useRouter();
const { t, locale } = useI18n({ useScope: 'global' });

// Nuevas rutas para la ONG
const navLinks = computed(() => [
  { name: t('nav.home'), path: '/' },
  { name: t('nav.about'), path: '/conocenos' },
  { name: t('nav.blog'), path: '/blog' },
  { name: t('nav.news'), path: '/noticias' },
  { name: t('nav.data'), path: '/datos' },
  { name: t('nav.institutions'), path: '/instituciones' },
  { name: t('nav.contact'), path: '/contactanos' },
  { name: t('nav.public_sector'), path: '/sector-publico/asistente-obstetrico' }
]);

const toggleDrawer = () => { isDrawerOpen.value = !isDrawerOpen.value; };
const closeDrawer = () => { isDrawerOpen.value = false; };
const openSearch = () => { isSearchOpen.value = true; };
const closeSearch = () => { isSearchOpen.value = false; };

const handleKeyDown = (e: KeyboardEvent) => {
  if (e.key === 'Escape' && isDrawerOpen.value) closeDrawer();
  if (e.key === 'Escape' && isSearchOpen.value) closeSearch();
};

const changeGoogleLanguage = (langCode: string) => {
  locale.value = langCode;
  
  const select = document.querySelector('.goog-te-combo') as HTMLSelectElement;
  if (select) {
    select.value = langCode;
    select.dispatchEvent(new Event('change'));
  } else {
    document.cookie = `googtrans=/es/${langCode}; path=/`;
    document.cookie = `googtrans=/es/${langCode}; path=/; domain=${window.location.hostname}`;
    window.location.reload();
  }
};

onMounted(() => { document.addEventListener('keydown', handleKeyDown); });
onUnmounted(() => { document.removeEventListener('keydown', handleKeyDown); });
</script>

<style scoped>
/* Transiciones para el Drawer Móvil */
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.slide-enter-active, .slide-leave-active { transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
.slide-enter-from, .slide-leave-to { transform: translateX(100%); }
</style>