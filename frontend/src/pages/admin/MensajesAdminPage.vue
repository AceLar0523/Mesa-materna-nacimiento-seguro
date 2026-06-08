<template>
  <div>
    <div class="admin-page-header">
      <h2>Mensajes</h2>
      <div class="breadcrumb">
        <router-link to="/dashboard">Dashboard</router-link>
        <i class="pi pi-angle-right text-xs"></i>
        <span>Mensajes</span>
      </div>
    </div>

    <div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
      <!-- Message List -->
      <div class="lg:col-span-1">
        <div class="admin-table-container">
          <div class="admin-table-header">
            <h3>Bandeja de Entrada</h3>
            <span class="inline-flex items-center rounded-full bg-orange-100 px-2.5 py-0.5 text-xs font-bold text-[#F97316]">
              3 nuevos
            </span>
          </div>
          <div class="divide-y divide-gray-50">
            <div
              v-for="msg in messages"
              :key="msg.id"
              class="flex cursor-pointer gap-3 p-4 transition-colors hover:bg-orange-50/50"
              :class="{ 'bg-orange-50/30': !msg.read }"
              @click="selectedMessage = msg"
            >
              <div
                class="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full text-xs font-bold text-white"
                :style="{ background: msg.avatarBg }"
              >
                {{ msg.initials }}
              </div>
              <div class="min-w-0 flex-1">
                <div class="flex items-center justify-between">
                  <p class="text-sm font-semibold text-gray-900 truncate">{{ msg.from }}</p>
                  <span class="text-xs text-gray-400 flex-shrink-0">{{ msg.time }}</span>
                </div>
                <p class="text-sm font-medium text-gray-700 truncate">{{ msg.subject }}</p>
                <p class="text-xs text-gray-500 truncate">{{ msg.preview }}</p>
              </div>
              <div v-if="!msg.read" class="mt-2 h-2 w-2 flex-shrink-0 rounded-full bg-[#F97316]"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Message Detail -->
      <div class="lg:col-span-2">
        <div class="admin-table-container">
          <template v-if="selectedMessage">
            <div class="border-b border-gray-100 p-6">
              <h3 class="text-lg font-bold text-gray-900 mb-1">{{ selectedMessage.subject }}</h3>
              <div class="flex items-center gap-3">
                <div
                  class="flex h-8 w-8 items-center justify-center rounded-full text-xs font-bold text-white"
                  :style="{ background: selectedMessage.avatarBg }"
                >
                  {{ selectedMessage.initials }}
                </div>
                <div>
                  <p class="text-sm font-semibold text-gray-900">{{ selectedMessage.from }}</p>
                  <p class="text-xs text-gray-500">{{ selectedMessage.email }} · {{ selectedMessage.time }}</p>
                </div>
              </div>
            </div>
            <div class="p-6">
              <p class="text-sm text-gray-700 leading-relaxed whitespace-pre-line">{{ selectedMessage.body }}</p>
            </div>
            <div class="border-t border-gray-100 p-4 flex gap-3">
              <button class="admin-btn-primary">
                <i class="pi pi-reply"></i>
                Responder
              </button>
              <button class="admin-topbar-icon-btn" title="Archivar">
                <i class="pi pi-inbox"></i>
              </button>
              <button class="admin-topbar-icon-btn" title="Eliminar">
                <i class="pi pi-trash"></i>
              </button>
            </div>
          </template>
          <template v-else>
            <div class="admin-empty-state">
              <i class="pi pi-envelope"></i>
              <h3>Selecciona un mensaje</h3>
              <p>Haz clic en un mensaje de la bandeja para ver su contenido</p>
            </div>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

interface Message {
  id: number;
  from: string;
  email: string;
  initials: string;
  avatarBg: string;
  subject: string;
  preview: string;
  body: string;
  time: string;
  read: boolean;
}

const selectedMessage = ref<Message | null>(null);

const messages: Message[] = [
  {
    id: 1,
    from: 'Dra. Elena Rojas',
    email: 'elena.rojas@hospital.gob.bo',
    initials: 'ER',
    avatarBg: 'linear-gradient(135deg, #F97316, #991a73)',
    subject: 'Solicitud de colaboración',
    preview: 'Buenos días, me gustaría coordinar una reunión...',
    body: 'Buenos días,\n\nMe gustaría coordinar una reunión para discutir la posibilidad de colaboración entre el Hospital de la Mujer y la Mesa de Maternidad y Nacimiento Seguro.\n\nTenemos un programa de capacitación para parteras comunitarias que podría beneficiarse de los recursos que ustedes manejan.\n\nQuedo atenta a su respuesta.\n\nSaludos cordiales,\nDra. Elena Rojas',
    time: 'Hace 1h',
    read: false,
  },
  {
    id: 2,
    from: 'Juan Condori',
    email: 'j.condori@gmail.com',
    initials: 'JC',
    avatarBg: 'linear-gradient(135deg, #3b82f6, #2563eb)',
    subject: 'Consulta sobre publicaciones',
    preview: 'Hola, ¿dónde puedo encontrar el informe anual...',
    body: 'Hola,\n\n¿Dónde puedo encontrar el informe anual de MNMNS del 2025? He buscado en la sección de publicaciones pero no lo encuentro.\n\nGracias,\nJuan Condori',
    time: 'Hace 3h',
    read: false,
  },
  {
    id: 3,
    from: 'ONG Warmi',
    email: 'contacto@warmi.org',
    initials: 'OW',
    avatarBg: 'linear-gradient(135deg, #10b981, #059669)',
    subject: 'Invitación a evento',
    preview: 'Les invitamos al foro sobre salud materna...',
    body: 'Estimados miembros de MNMNS,\n\nLes invitamos cordialmente al Foro Regional sobre Salud Materna que se llevará a cabo el 15 de julio de 2026 en la ciudad de Potosí.\n\nEl evento contará con la participación de expertos nacionales e internacionales.\n\nConfirmación antes del 1 de julio.\n\nAtentamente,\nONG Warmi',
    time: 'Ayer',
    read: false,
  },
  {
    id: 4,
    from: 'Sistema',
    email: 'noreply@mnmns.org',
    initials: 'S',
    avatarBg: 'linear-gradient(135deg, #64748b, #475569)',
    subject: 'Backup completado',
    preview: 'El backup automático del sistema se completó...',
    body: 'El backup automático del sistema se completó exitosamente.\n\nFecha: 05 de junio de 2026\nTamaño: 234 MB\nEstado: Exitoso',
    time: 'Hace 2 días',
    read: true,
  },
];

selectedMessage.value = messages[0];
</script>
