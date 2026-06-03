<template>
  <div class="fixed bottom-6 right-6 z-50 flex flex-col items-end">
    <Transition name="fade-slide">
      <div v-if="isOpen" class="mb-4 w-80 sm:w-96 bg-white rounded-2xl shadow-2xl border border-gray-200 overflow-hidden flex flex-col h-[500px]">
        <div class="bg-[#F97316] text-white p-4 flex justify-between items-center">
          <div class="flex items-center gap-2">
            <i class="pi pi-comments text-xl"></i>
            <h3 class="font-bold">Asistente Materno</h3>
          </div>
          <button @click="isOpen = false" class="hover:text-gray-200 transition-colors">
            <i class="pi pi-times"></i>
          </button>
        </div>

        <div class="flex-1 p-4 overflow-y-auto bg-gray-50 flex flex-col gap-3" ref="chatBox">
          <div v-for="(msg, index) in messages" :key="index" 
            :class="['max-w-[85%] p-3 rounded-2xl text-sm whitespace-pre-line', msg.isBot ? 'bg-white border border-gray-100 text-gray-800 self-start rounded-tl-none shadow-sm' : 'bg-[#F97316] text-white self-end rounded-tr-none shadow-md']">
            {{ msg.text }}
          </div>
          <div v-if="isLoading" class="text-gray-400 text-sm flex gap-1 items-center self-start bg-white p-3 rounded-2xl rounded-tl-none shadow-sm">
            <i class="pi pi-spin pi-spinner"></i> Escribiendo...
          </div>
        </div>

        <div class="p-3 bg-white border-t border-gray-100 flex items-center gap-2">
             <input v-model="userInput" @keyup.enter="sendMessage" type="text" placeholder="Haz tu consulta..." 
               class="flex-1 border-none focus:ring-0 bg-gray-100 rounded-full px-4 py-2 text-sm text-gray-900 placeholder:text-gray-400 caret-gray-900 outline-none" />
          <button @click="sendMessage" :disabled="isLoading || !userInput.trim()" 
                  class="bg-[#F97316] text-white w-10 h-10 rounded-full flex justify-center items-center hover:bg-orange-600 disabled:opacity-50 transition-colors">
            <i class="pi pi-send"></i>
          </button>
        </div>
      </div>
    </Transition>

    <button @click="isOpen = !isOpen" 
            class="w-14 h-14 bg-[#F97316] hover:bg-orange-600 text-white rounded-full shadow-xl flex justify-center items-center transition-transform hover:scale-110 active:scale-95">
      <i :class="isOpen ? 'pi pi-times text-2xl' : 'pi pi-comment text-2xl'"></i>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick } from 'vue';

type ChatMessage = {
  text: string;
  isBot: boolean;
};

const isOpen = ref(false);
const userInput = ref('');
const isLoading = ref(false);
const chatBox = ref<HTMLElement | null>(null);

const messages = ref<ChatMessage[]>([
  { text: '¡Hola! Soy el asistente de la Mesa Nacional de Maternidad. ¿En qué te puedo ayudar hoy?', isBot: true }
]);

const scrollToBottom = async () => {
  await nextTick();
  if (chatBox.value) {
    chatBox.value.scrollTop = chatBox.value.scrollHeight;
  }
};

const sendMessage = async () => {
  const text = userInput.value.trim();
  if (!text || isLoading.value) return;

  messages.value.push({ text, isBot: false });
  userInput.value = '';
  isLoading.value = true;
  await scrollToBottom();

  try {
    const response = await fetch('http://127.0.0.1:8000/api/chat/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mensaje: text })
    });
    
    const data = await response.json();
    const botReply =
      (typeof data?.respuesta === 'string' && data.respuesta.trim()) ||
      (typeof data?.respuesta_texto === 'string' && data.respuesta_texto.trim()) ||
      (typeof data?.reply === 'string' && data.reply.trim()) ||
      (typeof data?.message === 'string' && data.message.trim()) ||
      (!response.ok ? 'No se pudo procesar tu consulta en este momento.' : 'No se recibió una respuesta válida del asistente.');

    messages.value.push({ text: botReply, isBot: true });
  } catch (error) {
    messages.value.push({ text: 'Lo siento, hubo un problema al conectar con el servidor.', isBot: true });
  } finally {
    isLoading.value = false;
    await scrollToBottom();
  }
};
</script>

<style scoped>
.fade-slide-enter-active, .fade-slide-leave-active {
  transition: all 0.3s ease;
}
.fade-slide-enter-from, .fade-slide-leave-to {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}
</style>