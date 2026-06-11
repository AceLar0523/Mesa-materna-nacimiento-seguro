<template>
  <div class="space-y-6">
    <main class="grid gap-6">
      <div class="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 class="text-3xl font-black text-slate-900">Morbilidad Materna Extrema</h1>
          <p class="text-sm text-slate-500 mt-1">Registro y análisis bajo el enfoque de las "3 Demoras"</p>
        </div>
        <button type="button" class="rounded-full bg-[#EC4899] px-5 py-2.5 text-sm font-bold text-white shadow-md transition hover:bg-[#BE185D] flex items-center gap-2" @click="openNewModal">
          <i class="pi pi-plus font-bold"></i>
          Nuevo Registro
        </button>
      </div>

      <div class="grid gap-4 md:grid-cols-3">
        <article class="rounded-3xl border border-pink-100 bg-white p-5 shadow-sm">
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-pink-500">Total Casos</p>
          <h2 class="mt-2 text-4xl font-black text-slate-900">{{ records.length }}</h2>
        </article>
        <article class="rounded-3xl border border-emerald-100 bg-white p-5 shadow-sm">
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-emerald-500">Sobrevivientes</p>
          <h2 class="mt-2 text-4xl font-black text-slate-900">{{ countByStatus('survived') }}</h2>
        </article>
        <article class="rounded-3xl border border-slate-200 bg-white p-5 shadow-sm">
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Fallecidas</p>
          <h2 class="mt-2 text-4xl font-black text-slate-900">{{ countByStatus('deceased') }}</h2>
        </article>
      </div>

      <section class="grid gap-4">
        <div v-if="loading" class="flex flex-col items-center justify-center py-12 text-pink-500">
          <i class="pi pi-spin pi-spinner text-4xl mb-4"></i>
          <p class="font-bold text-slate-600">Cargando registros...</p>
        </div>

        <article v-else-if="records.length === 0" class="rounded-[2rem] border border-dashed border-pink-200 bg-white px-6 py-12 text-center shadow-sm">
          <p class="text-xs font-bold uppercase tracking-[0.25em] text-pink-500">Sin Registros</p>
          <h3 class="mt-3 text-2xl font-black text-slate-900">No hay casos Near-Miss registrados</h3>
          <p class="mx-auto mt-3 max-w-2xl text-sm leading-6 text-slate-600">
            Comienza agregando el primer registro clínico para llevar el análisis epidemiológico de morbilidad materna extrema.
          </p>
          <button class="mt-6 rounded-full bg-pink-50 px-6 py-2 font-bold text-pink-600 transition hover:bg-pink-100" @click="openNewModal">
            Agregar el primer caso
          </button>
        </article>

        <article v-else v-for="record in records" :key="record.id" class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm transition hover:shadow-md">
          <div class="flex flex-wrap items-start justify-between gap-4">
            <div>
              <div class="flex items-center gap-3">
                <span class="rounded-full px-3 py-1 text-xs font-bold" :class="record.survival_status === 'survived' ? 'bg-emerald-50 text-emerald-700' : 'bg-slate-100 text-slate-700'">
                  {{ record.survival_status === 'survived' ? 'Sobrevivió' : 'Falleció' }}
                </span>
                <h3 class="font-black text-slate-900 text-lg">{{ getConditionLabel(record.condition) }}</h3>
              </div>
              <p class="mt-2 text-sm text-slate-600 font-medium">Paciente de {{ record.patient_age }} años ({{ record.gestational_age }} sem. de gestación)</p>
              <p class="mt-1 text-xs text-slate-400">Registrado el {{ formatDate(record.created_at) }}</p>
            </div>

            <div class="flex gap-2">
              <button class="rounded-full bg-slate-50 p-2 text-slate-500 transition hover:bg-slate-100 hover:text-slate-900" title="Ver/Editar" @click="viewRecord(record)">
                <i class="pi pi-pencil"></i>
              </button>
              <button class="rounded-full bg-rose-50 p-2 text-rose-500 transition hover:bg-rose-100 hover:text-rose-700" title="Eliminar" @click="confirmDelete(record.id)">
                <i class="pi pi-trash"></i>
              </button>
            </div>
          </div>

          <div class="mt-6 border-t border-slate-100 pt-4">
            <p class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">Análisis de 3 Demoras</p>
            <div class="grid grid-cols-3 gap-2">
              <div class="rounded-xl p-3 border" :class="record.delay_1_decision ? 'bg-orange-50 border-orange-200 text-orange-800' : 'bg-slate-50 border-slate-100 text-slate-400'">
                <p class="text-xs font-bold mb-1">D1: Decisión</p>
                <p class="text-[0.7rem] line-clamp-2 leading-snug">{{ record.delay_1_decision ? (record.delay_1_details || 'Demora identificada') : 'Sin demora' }}</p>
              </div>
              <div class="rounded-xl p-3 border" :class="record.delay_2_transport ? 'bg-orange-50 border-orange-200 text-orange-800' : 'bg-slate-50 border-slate-100 text-slate-400'">
                <p class="text-xs font-bold mb-1">D2: Transporte</p>
                <p class="text-[0.7rem] line-clamp-2 leading-snug">{{ record.delay_2_transport ? (record.delay_2_details || 'Demora identificada') : 'Sin demora' }}</p>
              </div>
              <div class="rounded-xl p-3 border" :class="record.delay_3_care ? 'bg-orange-50 border-orange-200 text-orange-800' : 'bg-slate-50 border-slate-100 text-slate-400'">
                <p class="text-xs font-bold mb-1">D3: Atención</p>
                <p class="text-[0.7rem] line-clamp-2 leading-snug">{{ record.delay_3_care ? (record.delay_3_details || 'Demora identificada') : 'Sin demora' }}</p>
              </div>
            </div>
          </div>
        </article>
      </section>
    </main>

    <!-- Modal Form -->
    <div v-if="showModal" class="fixed inset-0 z-[100] flex items-center justify-center bg-slate-900/50 backdrop-blur-sm p-4 overflow-y-auto" @click.self="closeModal">
      <div class="w-full max-w-3xl rounded-[2rem] bg-white shadow-2xl overflow-hidden my-8">
        <div class="flex items-center justify-between border-b border-slate-100 px-8 py-5 bg-slate-50/50">
          <h2 class="text-xl font-black text-slate-900">{{ isEditing ? 'Editar Registro Clínico' : 'Nuevo Registro Near-Miss' }}</h2>
          <button class="text-slate-400 transition hover:text-rose-500" @click="closeModal">
            <i class="pi pi-times text-xl"></i>
          </button>
        </div>

        <form @submit.prevent="saveRecord" class="px-8 py-6 space-y-8 max-h-[70vh] overflow-y-auto">
          
          <div class="space-y-4">
            <h3 class="text-sm font-bold uppercase tracking-wider text-pink-500 flex items-center gap-2">
              <i class="pi pi-user"></i> Datos Clínicos
            </h3>
            <div class="grid gap-4 md:grid-cols-2">
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Edad de la Paciente</label>
                <input type="number" v-model="formData.patient_age" required min="10" max="60" class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-2.5 text-sm font-medium focus:border-pink-500 focus:bg-white focus:outline-none focus:ring-1 focus:ring-pink-500" />
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Edad Gestacional (Sem)</label>
                <input type="number" v-model="formData.gestational_age" required min="0" max="42" class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-2.5 text-sm font-medium focus:border-pink-500 focus:bg-white focus:outline-none focus:ring-1 focus:ring-pink-500" />
              </div>
            </div>
            
            <div class="grid gap-4 md:grid-cols-2">
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Condición Principal</label>
                <select v-model="formData.condition" required class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-2.5 text-sm font-medium focus:border-pink-500 focus:bg-white focus:outline-none focus:ring-1 focus:ring-pink-500">
                  <option value="hemorrhage">Hemorragia severa</option>
                  <option value="hypertension">Trastorno hipertensivo severo (Preeclampsia/Eclampsia)</option>
                  <option value="sepsis">Infección sistémica severa / Sepsis</option>
                  <option value="other">Otra complicación severa</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Supervivencia</label>
                <select v-model="formData.survival_status" required class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-2.5 text-sm font-medium focus:border-pink-500 focus:bg-white focus:outline-none focus:ring-1 focus:ring-pink-500">
                  <option value="survived">Sobrevivió</option>
                  <option value="deceased">Falleció</option>
                </select>
              </div>
            </div>
          </div>

          <div class="space-y-4 rounded-2xl bg-orange-50/50 p-6 border border-orange-100">
            <div class="mb-2">
              <h3 class="text-sm font-bold uppercase tracking-wider text-orange-600 flex items-center gap-2">
                <i class="pi pi-exclamation-triangle"></i> Análisis: Las 3 Demoras
              </h3>
              <p class="text-xs text-orange-600/70 mt-1">Identifique los cuellos de botella críticos en la atención</p>
            </div>

            <div class="space-y-3">
              <div class="rounded-xl border bg-white p-4 transition-colors" :class="formData.delay_1_decision ? 'border-orange-300 shadow-sm' : 'border-slate-200'">
                <label class="flex items-start gap-3 cursor-pointer">
                  <input type="checkbox" v-model="formData.delay_1_decision" class="mt-1 h-4 w-4 rounded border-slate-300 text-orange-500 focus:ring-orange-500" />
                  <div class="flex-1">
                    <span class="block text-sm font-bold text-slate-900">Demora 1: Decisión de buscar ayuda</span>
                    <span class="block text-xs text-slate-500 mb-2">Falta de conocimiento, factores culturales, económicos.</span>
                    <textarea v-if="formData.delay_1_decision" v-model="formData.delay_1_details" rows="2" class="w-full rounded-lg border border-slate-200 bg-slate-50 p-2 text-sm focus:border-orange-500 focus:bg-white focus:outline-none focus:ring-1 focus:ring-orange-500" placeholder="Detalles de la demora..."></textarea>
                  </div>
                </label>
              </div>

              <div class="rounded-xl border bg-white p-4 transition-colors" :class="formData.delay_2_transport ? 'border-orange-300 shadow-sm' : 'border-slate-200'">
                <label class="flex items-start gap-3 cursor-pointer">
                  <input type="checkbox" v-model="formData.delay_2_transport" class="mt-1 h-4 w-4 rounded border-slate-300 text-orange-500 focus:ring-orange-500" />
                  <div class="flex-1">
                    <span class="block text-sm font-bold text-slate-900">Demora 2: Transporte al centro</span>
                    <span class="block text-xs text-slate-500 mb-2">Distancia, falta de caminos, ausencia de ambulancia.</span>
                    <textarea v-if="formData.delay_2_transport" v-model="formData.delay_2_details" rows="2" class="w-full rounded-lg border border-slate-200 bg-slate-50 p-2 text-sm focus:border-orange-500 focus:bg-white focus:outline-none focus:ring-1 focus:ring-orange-500" placeholder="Detalles de la demora..."></textarea>
                  </div>
                </label>
              </div>

              <div class="rounded-xl border bg-white p-4 transition-colors" :class="formData.delay_3_care ? 'border-orange-300 shadow-sm' : 'border-slate-200'">
                <label class="flex items-start gap-3 cursor-pointer">
                  <input type="checkbox" v-model="formData.delay_3_care" class="mt-1 h-4 w-4 rounded border-slate-300 text-orange-500 focus:ring-orange-500" />
                  <div class="flex-1">
                    <span class="block text-sm font-bold text-slate-900">Demora 3: Atención oportuna</span>
                    <span class="block text-xs text-slate-500 mb-2">Falta de personal, insumos, sangre, o retrasos administrativos.</span>
                    <textarea v-if="formData.delay_3_care" v-model="formData.delay_3_details" rows="2" class="w-full rounded-lg border border-slate-200 bg-slate-50 p-2 text-sm focus:border-orange-500 focus:bg-white focus:outline-none focus:ring-1 focus:ring-orange-500" placeholder="Detalles de la demora..."></textarea>
                  </div>
                </label>
              </div>
            </div>
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Notas Adicionales</label>
            <textarea v-model="formData.notes" rows="3" class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-2.5 text-sm focus:border-pink-500 focus:bg-white focus:outline-none focus:ring-1 focus:ring-pink-500" placeholder="Observaciones generales..."></textarea>
          </div>

        </form>

        <div class="flex items-center justify-end gap-3 border-t border-slate-100 bg-slate-50/50 px-8 py-4">
          <button type="button" class="rounded-full px-5 py-2 text-sm font-bold text-slate-600 transition hover:bg-slate-100" @click="closeModal">Cancelar</button>
          <button type="button" class="rounded-full bg-pink-500 px-6 py-2 text-sm font-bold text-white shadow-md transition hover:bg-pink-600 flex items-center gap-2" :disabled="saving" @click="saveRecord">
            <i v-if="saving" class="pi pi-spin pi-spinner"></i>
            {{ saving ? 'Guardando...' : 'Guardar' }}
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { apiUrl } from '@/utils/api';

interface NearMissRecord {
  id?: number;
  patient_age: number | null;
  gestational_age: number | null;
  condition: string;
  health_center: number | null;
  delay_1_decision: boolean;
  delay_1_details: string;
  delay_2_transport: boolean;
  delay_2_details: string;
  delay_3_care: boolean;
  delay_3_details: string;
  survival_status: string;
  notes: string;
  created_at?: string;
}

const defaultForm: NearMissRecord = {
  patient_age: null,
  gestational_age: null,
  condition: 'hemorrhage',
  health_center: null,
  delay_1_decision: false,
  delay_1_details: '',
  delay_2_transport: false,
  delay_2_details: '',
  delay_3_care: false,
  delay_3_details: '',
  survival_status: 'survived',
  notes: ''
};

const records = ref<NearMissRecord[]>([]);
const loading = ref(true);
const saving = ref(false);
const showModal = ref(false);
const isEditing = ref(false);
const formData = ref<NearMissRecord>({ ...defaultForm });

const fetchRecords = async () => {
  loading.value = true;
  try {
    const res = await fetch(apiUrl('/near-miss/'));
    if (res.ok) {
      records.value = await res.json();
    }
  } catch (error) {
    console.error('Error fetching near miss records:', error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchRecords();
});

const openNewModal = () => {
  formData.value = { ...defaultForm };
  isEditing.value = false;
  showModal.value = true;
};

const viewRecord = (record: NearMissRecord) => {
  formData.value = { ...record };
  isEditing.value = true;
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
};

const saveRecord = async () => {
  saving.value = true;
  try {
    const method = isEditing.value ? 'PUT' : 'POST';
    const url = isEditing.value 
      ? apiUrl(`/near-miss/${formData.value.id}/`) 
      : apiUrl('/near-miss/');
      
    const res = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData.value),
    });
    
    if (res.ok) {
      closeModal();
      fetchRecords();
    } else {
      alert('Error al guardar el registro');
    }
  } catch (error) {
    console.error('Save error:', error);
    alert('Error de red al guardar');
  } finally {
    saving.value = false;
  }
};

const confirmDelete = async (id?: number) => {
  if (!id) return;
  if (confirm('¿Está seguro de eliminar este registro Near-Miss?')) {
    try {
      const res = await fetch(apiUrl(`/near-miss/${id}/`), {
        method: 'DELETE',
      });
      if (res.ok) {
        fetchRecords();
      }
    } catch (error) {
      console.error('Delete error:', error);
    }
  }
};

const getConditionLabel = (val: string) => {
  const map: Record<string, string> = {
    hemorrhage: 'Hemorragia severa',
    hypertension: 'Trastorno hipertensivo',
    sepsis: 'Sepsis',
    other: 'Otra complicación'
  };
  return map[val] || val;
};

function countByStatus(status: 'survived' | 'deceased'): number {
  return records.value.filter((r) => r.survival_status === status).length;
}

const formatDate = (dateString?: string) => {
  if (!dateString) return '';
  return new Date(dateString).toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute:'2-digit' });
};
</script>
