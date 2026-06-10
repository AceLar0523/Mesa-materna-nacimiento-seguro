<template>
  <div class="min-h-screen bg-gray-50 pt-20 flex flex-col">
    <PageHero
      kicker="Comunidad"
      title="Publicaciones"
      subtitle="Repositorio de documentos técnicos guardados como publicaciones reales en la base de datos."
      backgroundImage="/img/fondo11.jpg"
    />

    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8 w-full flex-1">
      <div v-if="errorMessage" class="mb-4 rounded-2xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-700">
        {{ errorMessage }}
      </div>

      <div v-if="isLoading" class="py-16 text-center text-gray-500">
        Cargando publicaciones...
      </div>

      <div v-else class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
        <article v-for="item in publicationPosts" :key="item.id" class="rounded-2xl border border-gray-100 bg-white p-6 shadow-sm transition-all hover:-translate-y-1 hover:shadow-lg">
          <img src="/img/fondo7.jpg" :alt="item.titulo" class="h-36 w-full rounded-xl object-cover" />
          <div class="mt-4 flex items-center justify-between text-xs font-bold uppercase tracking-wider text-slate-500">
            <span class="text-[#F97316]">{{ item.categoria }}</span>
            <span>{{ formatDate(item.created_at) }}</span>
          </div>
          <h3 class="mt-4 text-xl font-bold text-gray-900">{{ item.titulo }}</h3>
          <p class="mt-2 text-sm text-gray-600 whitespace-pre-line">{{ item.contenido }}</p>
          <div class="mt-5 rounded-full bg-orange-50 px-4 py-2 text-sm font-semibold text-[#F97316]">
            Responsable: {{ item.autor || 'Equipo técnico' }}
          </div>
        </article>
      </div>

      <div v-if="!isLoading && publicationPosts.length === 0" class="py-16 text-center text-gray-500">
        Todavía no hay publicaciones registradas.
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '@/components/landing/Footer/Footer.vue';
import { apiUrl } from '@/utils/api';

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

const publicationPosts = computed(() => posts.value.filter((post) => post.categoria === 'Publicacion'));

function formatDate(value: string): string {
  return new Date(value).toLocaleDateString('es-BO', { day: '2-digit', month: 'short', year: 'numeric' });
}

async function loadPublications(): Promise<void> {
  try {
    errorMessage.value = '';
    const response = await fetch(apiUrl('/blog-posts/'));
    if (!response.ok) {
      throw new Error('No se pudieron cargar las publicaciones.');
    }

    posts.value = (await response.json()) as BlogPost[];
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : 'Error inesperado al cargar las publicaciones.';
  } finally {
    isLoading.value = false;
  }
}

onMounted(() => {
  document.title = 'Publicaciones | MNMNS';
  window.scrollTo(0, 0);
  void loadPublications();
});
</script>