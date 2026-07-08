<template>
  <div class="pt-20 bg-gray-50 min-h-screen flex flex-col">
    <PageHero
      :kicker="$t('blog_page.hero_kicker')"
      :title="$t('blog_page.hero_title')"
      :subtitle="$t('blog_page.hero_subtitle')"
      backgroundImage="/img/fondo9.jpg"
    />

    <section class="py-12 flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
        
        <div class="lg:col-span-1">
          <div class="bg-white rounded-3xl p-6 shadow-sm border border-gray-100 sticky top-28">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-10 h-10 rounded-full bg-orange-50 text-[#F97316] flex items-center justify-center">
                <i class="pi pi-pencil text-lg"></i>
              </div>
              <h2 class="text-xl font-bold text-gray-800">{{ $t('blog_page.create_post_heading') }}</h2>
            </div>

            <form @submit.prevent="publicarPost" class="space-y-4">
              <div>
                <label class="block text-xs font-bold text-gray-500 uppercase mb-1">{{ $t('blog_page.category_label') }}</label>
                <select v-model="nuevoPost.categoria" class="w-full bg-gray-50 border border-gray-200 text-gray-700 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#F97316]/50 focus:border-[#F97316] transition-all appearance-none cursor-pointer">
                  <option value="Recomendacion">{{ $t('blog_page.category_option_recommendation') }}</option>
                  <option value="Testimonio">{{ $t('blog_page.category_option_testimony') }}</option>
                  <option value="Opinion">{{ $t('blog_page.category_option_opinion') }}</option>
                  <option value="Duda">{{ $t('blog_page.category_option_doubt') }}</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-bold text-gray-500 uppercase mb-1">{{ $t('blog_page.title_label') }}</label>
                <input v-model="nuevoPost.titulo" type="text" :placeholder="$t('blog_page.title_placeholder')" required
                       class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#F97316]/50 focus:border-[#F97316] transition-all">
              </div>

              <div>
                <label class="block text-xs font-bold text-gray-500 uppercase mb-1">{{ $t('blog_page.author_label') }}</label>
                <input v-model="nuevoPost.autor" type="text" :placeholder="$t('blog_page.author_placeholder')" 
                       class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#F97316]/50 focus:border-[#F97316] transition-all">
              </div>

              <div>
                <label class="block text-xs font-bold text-gray-500 uppercase mb-1">{{ $t('blog_page.message_label') }}</label>
                <textarea v-model="nuevoPost.contenido" rows="4" :placeholder="$t('blog_page.message_placeholder')" required
                          class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#F97316]/50 focus:border-[#F97316] transition-all resize-none"></textarea>
              </div>

              <button type="submit" :disabled="isSubmitting"
                      class="w-full bg-[#F97316] hover:bg-[#EA580C] text-white font-bold py-3 px-6 rounded-xl transition-all shadow-md hover:shadow-lg flex justify-center items-center gap-2 disabled:opacity-70 disabled:cursor-not-allowed mt-2">
                <i v-if="isSubmitting" class="pi pi-spinner animate-spin"></i>
                <span v-else>{{ $t('blog_page.publish_now_button') }}</span>
              </button>
            </form>
          </div>
        </div>

        <div class="lg:col-span-2">
          <div class="flex justify-between items-center mb-6">
            <h2 class="text-2xl font-bold text-gray-800">{{ $t('blog_page.recent_posts_heading') }}</h2>
            <span class="text-sm font-medium text-gray-500 bg-gray-200 px-3 py-1 rounded-full">{{ posts.length }} {{ $t('blog_page.articles_count_suffix') }}</span>
          </div>

          <div v-if="postError" class="mb-4 rounded-2xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-700">
            {{ postError }}
          </div>

          <TransitionGroup name="list" tag="div" class="space-y-6 relative">
            
            <article v-for="post in posts" :key="post.id" 
                     class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
              
              <div class="flex justify-between items-start mb-4">
                <div class="flex items-center gap-3">
                  <div class="w-12 h-12 rounded-full bg-gradient-to-br from-orange-100 to-orange-50 flex items-center justify-center text-[#F97316] font-bold text-xl border border-orange-100">
                    {{ post.autor.charAt(0).toUpperCase() }}
                  </div>
                  <div>
                    <div class="font-bold text-gray-900">{{ post.autor }}</div>
                    <div class="text-xs text-gray-400 font-medium">{{ post.fecha }}</div>
                  </div>
                </div>
                <span :class="[
                    'px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wide',
                    post.categoria === 'Testimonio' ? 'bg-purple-50 text-purple-600' :
                    post.categoria === 'Recomendacion' ? 'bg-green-50 text-green-600' :
                    post.categoria === 'Duda' ? 'bg-orange-50 text-orange-600' :
                    'bg-orange-50 text-[#F97316]'
                  ]">
                  {{ categoriaLabel(post.categoria) }}
                </span>
              </div>

              <h3 class="text-xl font-bold text-gray-900 mb-2">{{ post.titulo }}</h3>
              <p class="text-gray-600 leading-relaxed whitespace-pre-line">{{ post.contenido }}</p>
              
              <div class="mt-6 pt-4 border-t border-gray-50 flex gap-6">
                <button
                  @click="darLike(post.id)"
                  :disabled="likeLoadingByPost[post.id]"
                  class="flex items-center gap-2 text-gray-400 hover:text-pink-500 transition-colors group disabled:opacity-50"
                >
                  <i class="pi pi-heart group-hover:scale-110 transition-transform"></i>
                  <span class="text-sm font-medium">{{ post.likes }}</span>
                </button>
                <button class="flex items-center gap-2 text-gray-400 hover:text-[#F97316] transition-colors group">
                  <i class="pi pi-comment group-hover:scale-110 transition-transform"></i>
                  <span class="text-sm font-medium">{{ $t('blog_page.comment_button') }}</span>
                </button>
              </div>

            </article>

          </TransitionGroup>

          <div v-if="!isLoadingPosts && posts.length === 0" class="text-center py-20 bg-white rounded-3xl border border-gray-100 shadow-sm mt-6">
            <i class="pi pi-inbox text-5xl text-gray-300 mb-4"></i>
            <h3 class="text-xl font-bold text-gray-700">{{ $t('blog_page.no_posts_title') }}</h3>
            <p class="text-gray-500 mt-2">{{ $t('blog_page.no_posts_subtitle') }}</p>
          </div>

          <div v-if="isLoadingPosts" class="text-center py-14 text-gray-500">
            <i class="pi pi-spinner animate-spin text-2xl"></i>
            <p class="mt-2">{{ $t('blog_page.loading_posts_message') }}</p>
          </div>

        </div>

      </div>
    </section>

    <Footer class="mt-auto" />
  </div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue';
import { useToast } from 'primevue/usetoast';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '../components/landing/Footer/Footer.vue';
import { apiUrl } from '@/utils/api';
import { useI18n } from 'vue-i18n'; // ADDED

const { t } = useI18n(); // ADDED

type CategoriaBlog = 'Recomendacion' | 'Testimonio' | 'Opinion' | 'Duda' | 'Noticia' | 'Publicacion';

interface BlogPostApi {
  id: number;
  autor: string;
  categoria: CategoriaBlog;
  titulo: string;
  contenido: string;
  likes: number;
  created_at: string;
}

interface BlogPostUI {
  id: number;
  autor: string;
  fecha: string;
  categoria: CategoriaBlog;
  titulo: string;
  contenido: string;
  likes: number;
}

const isSubmitting = ref(false);
const isLoadingPosts = ref(true);
const postError = ref('');
const likeLoadingByPost = ref<Record<number, boolean>>({});
const toast = useToast();
let stream: EventSource | null = null;

const nuevoPost = ref({
  titulo: '',
  autor: '',
  categoria: 'Testimonio' as CategoriaBlog,
  contenido: ''
});

const posts = ref<BlogPostUI[]>([]);

const categoriaLabel = (categoria: CategoriaBlog): string => {
  if (categoria === 'Recomendacion') return t('blog_page.category_display_recommendation');
  if (categoria === 'Opinion') return t('blog_page.category_display_opinion');
  if (categoria === 'Noticia') return t('blog_page.category_display_news');
  if (categoria === 'Publicacion') return t('blog_page.category_display_publication');
  if (categoria === 'Testimonio') return t('blog_page.category_display_testimony');
  if (categoria === 'Duda') return t('blog_page.category_display_doubt');
  return categoria; // Fallback for unknown categories
};

const mapApiToUI = (post: BlogPostApi): BlogPostUI => ({
  id: post.id,
  autor: post.autor,
  fecha: new Date(post.created_at).toLocaleDateString('es-BO', {
    day: '2-digit',
    month: 'short',
    year: 'numeric'
  }),
  categoria: post.categoria,
  titulo: post.titulo,
  contenido: post.contenido,
  likes: post.likes
});

const setPostsFromApi = (data: BlogPostApi[]) => {
  posts.value = data.map(mapApiToUI);
};

const cargarPosts = async () => {
  try {
    postError.value = '';
    const response = await fetch(apiUrl('/blog-posts/'));
    if (!response.ok) {
      throw new Error(t('blog_page.error_loading_posts'));
    }

    const data = (await response.json()) as BlogPostApi[];
    setPostsFromApi(data);
  } catch (error) {
    postError.value = error instanceof Error ? error.message : t('blog_page.error_unexpected_loading_blog');
  } finally {
    isLoadingPosts.value = false;
  }
};

const conectarStream = () => {
  stream = new EventSource(apiUrl('/blog/stream/'));

  stream.onmessage = (event: MessageEvent<string>) => {
    try {
      const data = JSON.parse(event.data) as BlogPostApi[];
      setPostsFromApi(data);
      postError.value = '';
    } catch {
      postError.value = t('blog_page.error_invalid_stream_data');
    }
  };

  stream.onerror = () => {
    // Avoid showing a disruptive banner while SSE reconnects automatically.
    stream?.close();
    setTimeout(conectarStream, 3000);
  };
};

const publicarPost = async () => {
  if (!nuevoPost.value.titulo || !nuevoPost.value.contenido) {
    return;
  }

  isSubmitting.value = true;
  postError.value = '';

  try {
    const response = await fetch(apiUrl('/blog-posts/'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        autor: nuevoPost.value.autor,
        categoria: nuevoPost.value.categoria,
        titulo: nuevoPost.value.titulo,
        contenido: nuevoPost.value.contenido
      })
    });

    if (!response.ok) {
      throw new Error(t('blog_page.error_publish_message_failed'));
    }

    const data = (await response.json()) as BlogPostApi;
    posts.value.unshift(mapApiToUI(data));

    nuevoPost.value = {
      titulo: '',
      autor: '',
      categoria: 'Testimonio',
      contenido: ''
    };

    toast.add({
      severity: 'success',
      summary: t('blog_page.toast_publish_success_summary'),
      detail: t('blog_page.toast_publish_success_detail'),
      life: 3000
    });
  } catch (error) {
    postError.value = error instanceof Error ? error.message : t('blog_page.error_unexpected_publishing');
  } finally {
    isSubmitting.value = false;
  }
};

const darLike = async (postId: number) => {
  likeLoadingByPost.value = { ...likeLoadingByPost.value, [postId]: true };

  try {
    const response = await fetch(apiUrl(`/blog-posts/${postId}/like/`), {
      method: 'POST'
    });

    if (!response.ok) {
      throw new Error(t('blog_page.error_reaction_failed'));
    }

    const data = (await response.json()) as BlogPostApi;
    posts.value = posts.value.map((post) => (post.id === postId ? mapApiToUI(data) : post));
  } catch (error) {
    postError.value = error instanceof Error ? error.message : t('blog_page.error_unexpected_reaction');
  } finally {
    likeLoadingByPost.value = { ...likeLoadingByPost.value, [postId]: false };
  }
};

onMounted(() => {
  document.title = t('blog_page.document_title');
  window.scrollTo(0, 0);
  void cargarPosts();
  conectarStream();
});

onUnmounted(() => {
  stream?.close();
});
</script>

<style scoped>
/* Transiciones mágicas de Vue para el TransitionGroup */
.list-move, /* aplica transición a elementos que se mueven */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(-30px) scale(0.95); /* Aparece desde arriba y ligeramente pequeño */
}

/* Asegura que los elementos que salen sean removidos del flujo para animación suave */
.list-leave-active {
  position: absolute;
  width: 100%;
}
</style>