<template>
  <div class="pt-20 bg-gray-50 min-h-screen flex flex-col">
    <PageHero
      kicker="Comunidad"
      title="Voces de la Comunidad"
      subtitle="Un espacio para compartir recomendaciones, testimonios y opiniones sobre la maternidad y el nacimiento seguro en Bolivia."
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
              <h2 class="text-xl font-bold text-gray-800">Crear Publicación</h2>
            </div>

            <form @submit.prevent="publicarPost" class="space-y-4">
              <div>
                <label class="block text-xs font-bold text-gray-500 uppercase mb-1">Categoría</label>
                <select v-model="nuevoPost.categoria" class="w-full bg-gray-50 border border-gray-200 text-gray-700 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#F97316]/50 focus:border-[#F97316] transition-all appearance-none cursor-pointer">
                  <option value="Recomendacion">Recomendación Médica</option>
                  <option value="Testimonio">Testimonio de Vida</option>
                  <option value="Opinion">Opinión</option>
                  <option value="Duda">Duda / Consulta</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-bold text-gray-500 uppercase mb-1">Título</label>
                <input v-model="nuevoPost.titulo" type="text" placeholder="Ej. Mi experiencia en la Casa Materna..." required
                       class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#F97316]/50 focus:border-[#F97316] transition-all">
              </div>

              <div>
                <label class="block text-xs font-bold text-gray-500 uppercase mb-1">Tu Nombre (Opcional)</label>
                <input v-model="nuevoPost.autor" type="text" placeholder="Anónimo" 
                       class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#F97316]/50 focus:border-[#F97316] transition-all">
              </div>

              <div>
                <label class="block text-xs font-bold text-gray-500 uppercase mb-1">Tu Mensaje</label>
                <textarea v-model="nuevoPost.contenido" rows="4" placeholder="Escribe aquí tu mensaje, consejo o historia..." required
                          class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#F97316]/50 focus:border-[#F97316] transition-all resize-none"></textarea>
              </div>

              <button type="submit" :disabled="isSubmitting"
                      class="w-full bg-[#F97316] hover:bg-[#EA580C] text-white font-bold py-3 px-6 rounded-xl transition-all shadow-md hover:shadow-lg flex justify-center items-center gap-2 disabled:opacity-70 disabled:cursor-not-allowed mt-2">
                <i v-if="isSubmitting" class="pi pi-spinner animate-spin"></i>
                <span v-else>Publicar ahora</span>
              </button>
            </form>
          </div>
        </div>

        <div class="lg:col-span-2">
          <div class="flex justify-between items-center mb-6">
            <h2 class="text-2xl font-bold text-gray-800">Publicaciones Recientes</h2>
            <span class="text-sm font-medium text-gray-500 bg-gray-200 px-3 py-1 rounded-full">{{ posts.length }} artículos</span>
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
                  <span class="text-sm font-medium">Comentar</span>
                </button>
              </div>

            </article>

          </TransitionGroup>

          <div v-if="!isLoadingPosts && posts.length === 0" class="text-center py-20 bg-white rounded-3xl border border-gray-100 shadow-sm mt-6">
            <i class="pi pi-inbox text-5xl text-gray-300 mb-4"></i>
            <h3 class="text-xl font-bold text-gray-700">Aún no hay publicaciones</h3>
            <p class="text-gray-500 mt-2">¡Sé la primera persona en compartir tu experiencia!</p>
          </div>

          <div v-if="isLoadingPosts" class="text-center py-14 text-gray-500">
            <i class="pi pi-spinner animate-spin text-2xl"></i>
            <p class="mt-2">Cargando publicaciones...</p>
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
  if (categoria === 'Recomendacion') return 'Recomendación';
  if (categoria === 'Opinion') return 'Opinión';
  if (categoria === 'Noticia') return 'Noticia';
  if (categoria === 'Publicacion') return 'Publicación';
  return categoria;
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
      throw new Error('No se pudieron cargar las publicaciones.');
    }

    const data = (await response.json()) as BlogPostApi[];
    setPostsFromApi(data);
  } catch (error) {
    postError.value = error instanceof Error ? error.message : 'Error inesperado al cargar el blog.';
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
      postError.value = 'Se recibieron datos no validos del stream del blog.';
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
      throw new Error('No se pudo publicar el mensaje. Intenta nuevamente.');
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
      summary: 'Publicacion exitosa',
      detail: 'Tu publicacion se guardo correctamente.',
      life: 3000
    });
  } catch (error) {
    postError.value = error instanceof Error ? error.message : 'Error inesperado al publicar.';
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
      throw new Error('No se pudo registrar tu reaccion.');
    }

    const data = (await response.json()) as BlogPostApi;
    posts.value = posts.value.map((post) => (post.id === postId ? mapApiToUI(data) : post));
  } catch (error) {
    postError.value = error instanceof Error ? error.message : 'Error inesperado al reaccionar.';
  } finally {
    likeLoadingByPost.value = { ...likeLoadingByPost.value, [postId]: false };
  }
};

onMounted(() => {
  document.title = 'Blog y Comunidad | Mesa de Maternidad Bolivia';
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