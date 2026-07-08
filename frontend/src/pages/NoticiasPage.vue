<template>
  <div class="pt-20 bg-gray-50 min-h-screen flex flex-col">
    <PageHero
      :kicker="$t('noticias_page.kicker_sala_prensa')"
      :title="$t('noticias_page.titulo_ultimas_noticias')"
      :subtitle="$t('noticias_page.subtitulo_descripcion_noticias')"
      backgroundImage="/img/fondo10.jpg"
    />

    <section class="py-12 flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
      <div v-if="errorMessage" class="mb-4 rounded-2xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-700">
        {{ errorMessage }}
      </div>

      <div v-if="isLoading" class="py-16 text-center text-gray-500">
        {{ $t('noticias_page.cargando_noticias') }}
      </div>

      <div v-else class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
        <article v-for="item in newsPosts" :key="item.id" class="bg-white rounded-2xl overflow-hidden shadow-sm border border-gray-100 hover:shadow-lg transition-all duration-300 group flex flex-col">
          <div class="h-48 bg-gray-100 relative overflow-hidden flex items-center justify-center">
            <img src="/img/fondo13.png" :alt="$t('noticias_page.alt_noticia')" class="h-full w-full object-cover group-hover:scale-105 transition-transform duration-700" />
          </div>
          <div class="p-6 flex flex-col flex-1">
            <div class="flex justify-between items-center mb-3">
              <span class="text-[#F97316] text-xs font-bold uppercase tracking-wider">{{ item.categoria }}</span>
              <span class="text-gray-400 text-xs font-medium">{{ formatDate(item.created_at) }}</span>
            </div>
            <h3 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-[#F97316] transition-colors line-clamp-2">
              {{ item.titulo }}
            </h3>
            <p class="text-gray-600 text-sm mb-6 line-clamp-4 flex-1 whitespace-pre-line">
              {{ item.contenido }}
            </p>
            <div class="mt-auto pt-4 border-t border-gray-50">
              <span class="text-gray-900 font-medium text-sm group-hover:text-[#F97316] transition-colors">
                {{ $t('noticias_page.fuente') }}: {{ item.autor || $t('noticias_page.mesa_maternidad') }}
              </span>
            </div>
          </div>
        </article>
      </div>

      <div v-if="!isLoading && newsPosts.length === 0" class="py-16 text-center text-gray-500">
        {{ $t('noticias_page.no_hay_noticias') }}
      </div>
    </section>

    <Footer class="mt-auto" />
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '../components/landing/Footer/Footer.vue';
import { apiUrl } from '@/utils/api';
import { useI18n } from 'vue-i18n';

type BlogCategory = 'Recomendacion' | 'Testimonio' | 'Opinion' | 'Duda' | 'Noticia' | 'Publicacion';

interface BlogPost {
  id: number;
  autor: string;
  categoria: BlogCategory;
  titulo: string;
  contenido: string;
  likes: number;
  created_at: string;
}

const posts = ref<BlogPost[]>([]);
const isLoading = ref(true);
const errorMessage = ref('');

const { t } = useI18n();

const newsPosts = computed(() => posts.value.filter((post) => post.categoria === 'Noticia'));

function formatDate(value: string): string {
  return new Date(value).toLocaleDateString('es-BO', { day: '2-digit', month: 'short', year: 'numeric' });
}

async function loadNews(): Promise<void> {
  try {
    errorMessage.value = '';
    const response = await fetch(apiUrl('/blog-posts/'));
    if (!response.ok) {
      throw new Error(t('noticias_page.error_cargar_noticias'));
    }

    posts.value = (await response.json()) as BlogPost[];
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : t('noticias_page.error_inesperado_cargar_noticias');
  } finally {
    isLoading.value = false;
  }
}

onMounted(() => {
  document.title = t('noticias_page.document_title');
  window.scrollTo(0, 0);
  void loadNews();
});
</script>