<template>
  <div class="space-y-6">
    <div class="rounded-[2rem] border border-orange-100 bg-white p-6 shadow-sm">
      <div class="flex flex-wrap items-start justify-between gap-4">
        <div>
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-[#F97316]">Mensajes reales</p>
          <h2 class="mt-2 text-3xl font-black text-slate-900">Mensajes de contacto</h2>
          <p class="mt-2 max-w-3xl text-sm text-slate-600">Se leen desde ContactMessage en la base de datos. Desde aquí puedes revisar y eliminar mensajes si hace falta.</p>
        </div>
        <div class="rounded-2xl bg-orange-50 px-4 py-2 text-sm font-semibold text-[#EA580C]">
          {{ messages.length }} mensajes
        </div>
      </div>
    </div>

    <div v-if="errorMessage" class="rounded-2xl border border-rose-100 bg-rose-50 px-4 py-3 text-sm text-rose-700">
      {{ errorMessage }}
    </div>

    <div class="grid gap-6 lg:grid-cols-3">
      <section class="lg:col-span-1">
        <div class="rounded-[2rem] border border-slate-200 bg-white shadow-sm overflow-hidden">
          <div class="border-b border-slate-100 px-5 py-4">
            <h3 class="text-lg font-bold text-slate-900">Bandeja de entrada</h3>
          </div>
          <div class="divide-y divide-slate-100">
            <button
              v-for="msg in messages"
              :key="msg.id"
              type="button"
              class="flex w-full gap-3 px-5 py-4 text-left transition hover:bg-orange-50/50"
              :class="selectedMessage?.id === msg.id ? 'bg-orange-50/70' : ''"
              @click="selectedMessage = msg"
            >
              <div class="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-[#F97316] to-[#991a73] text-xs font-black text-white">
                {{ initials(msg.nombre) }}
              </div>
              <div class="min-w-0 flex-1">
                <div class="flex items-center justify-between gap-2">
                  <p class="truncate text-sm font-semibold text-slate-900">{{ msg.nombre }}</p>
                  <span class="text-xs text-slate-400">{{ formatDate(msg.created_at) }}</span>
                </div>
                <p class="truncate text-sm text-slate-600">{{ msg.asunto }}</p>
                <p class="truncate text-xs text-slate-500">{{ msg.email }}</p>
              </div>
            </button>
          </div>
        </div>
      </section>

      <section class="lg:col-span-2">
        <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm">
          <template v-if="selectedMessage">
            <div class="flex flex-wrap items-start justify-between gap-4 border-b border-slate-100 pb-4">
              <div>
                <p class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">{{ selectedMessage.asunto }}</p>
                <h3 class="mt-2 text-2xl font-black text-slate-900">{{ selectedMessage.nombre }}</h3>
                <p class="mt-1 text-sm text-slate-500">{{ selectedMessage.email }}</p>
              </div>
              <button type="button" class="rounded-full border border-rose-200 bg-white px-4 py-2 text-sm font-bold text-rose-600" @click="deleteMessage(selectedMessage.id)">
                Eliminar mensaje
              </button>
            </div>

            <div class="py-6">
              <p class="whitespace-pre-line text-sm leading-7 text-slate-700">{{ selectedMessage.mensaje }}</p>
            </div>
          </template>

          <template v-else>
            <div class="py-16 text-center text-slate-500">
              Selecciona un mensaje para verlo.
            </div>
          </template>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { apiUrl } from '@/utils/api';

interface ContactMessage {
  id: number;
  nombre: string;
  email: string;
  asunto: string;
  mensaje: string;
  created_at: string;
}

const messages = ref<ContactMessage[]>([]);
const selectedMessage = ref<ContactMessage | null>(null);
const errorMessage = ref('');

function initials(name: string): string {
  return name
    .split(' ')
    .filter(Boolean)
    .slice(0, 2)
    .map((part) => part[0])
    .join('')
    .toUpperCase();
}

function formatDate(value: string): string {
  return new Date(value).toLocaleDateString('es-BO', { day: '2-digit', month: 'short', year: 'numeric' });
}

async function loadMessages(): Promise<void> {
  const response = await fetch(apiUrl('/contact-messages/'));
  messages.value = response.ok ? ((await response.json()) as ContactMessage[]) : [];
  selectedMessage.value = messages.value[0] ?? null;
}

async function deleteMessage(messageId: number): Promise<void> {
  errorMessage.value = '';
  const response = await fetch(apiUrl(`/contact-messages/${messageId}/`), { method: 'DELETE' });

  if (!response.ok) {
    errorMessage.value = 'No se pudo eliminar el mensaje.';
    return;
  }

  await loadMessages();
}

onMounted(() => {
  document.title = 'Mensajes | Admin';
  void loadMessages();
});
</script>
