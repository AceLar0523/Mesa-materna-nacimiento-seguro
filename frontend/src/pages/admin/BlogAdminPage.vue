<template>
  <div class="space-y-6">
    <div class="rounded-[2rem] border border-orange-100 bg-white p-6 shadow-sm">
      <div class="flex flex-wrap items-start justify-between gap-4">
        <div>
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-[#F97316]">CRUD real</p>
          <h2 class="mt-2 text-3xl font-black text-slate-900">Blog</h2>
          <p class="mt-2 max-w-3xl text-sm text-slate-600">Los registros se guardan en la tabla BlogPost y se reflejan también en las páginas públicas.</p>
        </div>
        <div class="rounded-2xl bg-orange-50 px-4 py-2 text-sm font-semibold text-[#EA580C]">
          {{ posts.length }} registros
        </div>
      </div>

      <form class="mt-6 grid gap-4 lg:grid-cols-2" @submit.prevent="savePost">
        <label class="space-y-2 lg:col-span-2">
          <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Título</span>
          <input v-model="form.titulo" class="input-base" type="text" required />
        </label>
        <label class="space-y-2">
          <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Autor / Fuente</span>
          <input v-model="form.autor" class="input-base" type="text" placeholder="Anonimo" />
        </label>
        <label class="space-y-2">
          <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Categoría</span>
          <select v-model="form.categoria" class="input-base">
            <option value="Recomendacion">Recomendación médica</option>
            <option value="Testimonio">Testimonio de vida</option>
            <option value="Opinion">Opinión</option>
            <option value="Duda">Duda / Consulta</option>
            <option value="Noticia">Noticia</option>
            <option value="Publicacion">Publicación</option>
          </select>
        </label>
        <label class="space-y-2 lg:col-span-2">
          <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Contenido</span>
          <textarea v-model="form.contenido" rows="6" class="input-base resize-none" required></textarea>
        </label>
        <div class="lg:col-span-2 flex flex-wrap gap-3">
          <button type="submit" class="rounded-full bg-gradient-to-r from-[#F97316] to-[#991a73] px-5 py-3 text-sm font-black text-white shadow-lg">
            {{ editingId ? 'Actualizar' : 'Guardar' }}
          </button>
          <button type="button" class="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700" @click="resetForm">
            Limpiar
          </button>
        </div>
      </form>
    </div>

    <div v-if="errorMessage" class="rounded-2xl border border-rose-100 bg-rose-50 px-4 py-3 text-sm text-rose-700">
      {{ errorMessage }}
    </div>

    <div class="grid gap-4">
      <article v-for="post in posts" :key="post.id" class="rounded-[2rem] border border-slate-200 bg-white p-5 shadow-sm">
        <div class="flex flex-wrap items-start justify-between gap-4">
          <div class="max-w-3xl">
            <div class="flex flex-wrap items-center gap-2 text-xs font-bold uppercase tracking-[0.25em] text-slate-500">
              <span class="rounded-full bg-orange-50 px-3 py-1 text-[#EA580C]">{{ categoryLabel(post.categoria) }}</span>
              <span>{{ formatDate(post.created_at) }}</span>
            </div>
            <h3 class="mt-3 text-2xl font-black text-slate-900">{{ post.titulo }}</h3>
            <p class="mt-2 text-sm text-slate-600">{{ post.autor || 'Anonimo' }}</p>
            <p class="mt-4 whitespace-pre-line text-sm leading-6 text-slate-700">{{ post.contenido }}</p>
          </div>

          <div class="flex flex-wrap gap-2">
            <button type="button" class="rounded-full bg-slate-950 px-4 py-2 text-sm font-bold text-white" @click="editPost(post)">
              Editar
            </button>
            <button type="button" class="rounded-full border border-rose-200 bg-white px-4 py-2 text-sm font-bold text-rose-600" @click="deletePost(post.id)">
              Eliminar
            </button>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
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
  updated_at: string;
}

const posts = ref<BlogPost[]>([]);
const editingId = ref<number | null>(null);
const errorMessage = ref('');

const form = reactive({
  autor: '',
  categoria: 'Testimonio' as BlogCategory,
  titulo: '',
  contenido: ''
});

function resetForm(): void {
  editingId.value = null;
  form.autor = '';
  form.categoria = 'Testimonio';
  form.titulo = '';
  form.contenido = '';
}

function editPost(post: BlogPost): void {
  editingId.value = post.id;
  form.autor = post.autor;
  form.categoria = post.categoria;
  form.titulo = post.titulo;
  form.contenido = post.contenido;
}

function categoryLabel(category: BlogCategory): string {
  const labels: Record<BlogCategory, string> = {
    Recomendacion: 'Recomendación médica',
    Testimonio: 'Testimonio de vida',
    Opinion: 'Opinión',
    Duda: 'Duda / Consulta',
    Noticia: 'Noticia',
    Publicacion: 'Publicación'
  };

  return labels[category];
}

function formatDate(value: string): string {
  return new Date(value).toLocaleDateString('es-BO', { day: '2-digit', month: 'short', year: 'numeric' });
}

async function loadPosts(): Promise<void> {
  const response = await fetch(apiUrl('/blog-posts/'));
  posts.value = response.ok ? ((await response.json()) as BlogPost[]) : [];
}

async function savePost(): Promise<void> {
  errorMessage.value = '';

  const payload = {
    autor: form.autor,
    categoria: form.categoria,
    titulo: form.titulo,
    contenido: form.contenido
  };

  const response = await fetch(
    editingId.value ? apiUrl(`/blog-posts/${editingId.value}/`) : apiUrl('/blog-posts/'),
    {
      method: editingId.value ? 'PATCH' : 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    }
  );

  if (!response.ok) {
    errorMessage.value = 'No se pudo guardar la publicación.';
    return;
  }

  await loadPosts();
  resetForm();
}

async function deletePost(postId: number): Promise<void> {
  const response = await fetch(apiUrl(`/blog-posts/${postId}/`), { method: 'DELETE' });
  if (!response.ok) {
    errorMessage.value = 'No se pudo eliminar la publicación.';
    return;
  }

  await loadPosts();
  if (editingId.value === postId) {
    resetForm();
  }
}

onMounted(() => {
  document.title = 'Blog | Admin';
  void loadPosts();
});
</script>

<style scoped>
.input-base {
  width: 100%;
  border-radius: 1rem;
  border: 1px solid rgb(226 232 240);
  background: rgb(248 250 252);
  padding: 0.875rem 1rem;
  outline: none;
}
</style>