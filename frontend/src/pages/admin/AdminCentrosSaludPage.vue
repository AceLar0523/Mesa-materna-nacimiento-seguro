<template>
  <div class="space-y-6">
    <main class="grid gap-6 lg:grid-cols-[0.95fr_1.05fr]">
      <section class="rounded-3xl border border-teal-100 bg-white p-6 shadow-sm">
        <div class="flex items-center justify-between gap-4 mb-6">
          <div>
            <p class="text-xs font-bold uppercase tracking-[0.25em] text-teal-600">Formulario</p>
            <h2 class="mt-2 text-2xl font-black">{{ editingId ? 'Editar centro' : 'Nuevo centro' }}</h2>
          </div>
          <button class="rounded-full bg-teal-50 px-4 py-2 text-sm font-semibold text-teal-700" type="button" @click="resetForm">Limpiar</button>
        </div>

        <form class="grid gap-4 md:grid-cols-2" @submit.prevent="saveCenter">
          <label class="space-y-2 md:col-span-2"><span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Nombre</span><input v-model="form.nombre" class="input-base" type="text" required /></label>
          <label class="space-y-2"><span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Nivel</span><select v-model="form.nivel" class="input-base"><option value="I">Nivel I</option><option value="II">Nivel II</option><option value="III">Nivel III</option></select></label>
          <label class="space-y-2"><span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Ciudad</span><input v-model="form.ciudad" class="input-base" type="text" required /></label>
          <label class="space-y-2 md:col-span-2"><span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Dirección</span><input v-model="form.direccion" class="input-base" type="text" required /></label>
          <label class="space-y-2"><span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Teléfono</span><input v-model="form.telefono" class="input-base" type="text" required /></label>
          <label class="space-y-2"><span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Emergencia</span><input v-model="form.telefono_emergencia" class="input-base" type="text" /></label>
          <label class="space-y-2 md:col-span-2"><span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Horario</span><input v-model="form.horario" class="input-base" type="text" /></label>
          <label class="space-y-2"><span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Latitud</span><input v-model="form.latitude" class="input-base" type="number" step="0.000001" required /></label>
          <label class="space-y-2"><span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Longitud</span><input v-model="form.longitude" class="input-base" type="number" step="0.000001" required /></label>
          <label class="flex items-center gap-3 md:col-span-2"><input v-model="form.ambulancia_disponible" type="checkbox" class="h-5 w-5 rounded border-slate-300 text-teal-600" /><span class="text-sm font-semibold text-slate-700">Ambulancia disponible</span></label>
          <div class="md:col-span-2 flex flex-wrap gap-3">
            <button type="submit" class="rounded-full bg-gradient-to-r from-[#0F766E] to-[#14B8A6] px-5 py-3 text-sm font-black text-white shadow-lg">{{ editingId ? 'Actualizar' : 'Guardar' }}</button>
            <button type="button" class="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700" @click="resetForm">Reiniciar</button>
          </div>
        </form>
      </section>

      <section class="space-y-4">
        <article v-for="center in centers" :key="center.id" class="rounded-[2rem] border border-slate-200 bg-white p-5 shadow-lg">
          <div class="flex flex-wrap items-start justify-between gap-4">
            <div>
              <div class="flex items-center gap-2"><span class="rounded-full bg-teal-50 px-3 py-1 text-xs font-bold text-teal-700">Nivel {{ center.nivel }}</span><h3 class="font-black text-slate-900">{{ center.nombre }}</h3></div>
              <p class="mt-2 text-sm text-slate-600">{{ center.direccion }} · {{ center.ciudad }}</p>
              <p class="mt-2 text-xs text-slate-500">{{ center.telefono }} · {{ center.telefono_emergencia || 'Sin emergencia' }}</p>
            </div>
            <button class="rounded-full bg-slate-950 px-4 py-2 text-sm font-bold text-white" type="button" @click="populateForm(center)">Editar</button>
          </div>
        </article>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
import { apiUrl } from '@/utils/api';
import { type HealthCenter, type PublicSectorLevel } from '../client/public-sector';

type CenterForm = {
  nombre: string;
  nivel: PublicSectorLevel;
  direccion: string;
  ciudad: string;
  telefono: string;
  telefono_emergencia: string;
  horario: string;
  ambulancia_disponible: boolean;
  latitude: string;
  longitude: string;
};

const centers = ref<HealthCenter[]>([]);
const editingId = ref<number | null>(null);
const form = reactive<CenterForm>({
  nombre: '',
  nivel: 'I',
  direccion: '',
  ciudad: '',
  telefono: '',
  telefono_emergencia: '',
  horario: '',
  ambulancia_disponible: false,
  latitude: '-16.500000',
  longitude: '-68.150000'
});

function resetForm(): void {
  editingId.value = null;
  form.nombre = '';
  form.nivel = 'I';
  form.direccion = '';
  form.ciudad = '';
  form.telefono = '';
  form.telefono_emergencia = '';
  form.horario = '';
  form.ambulancia_disponible = false;
  form.latitude = '-16.500000';
  form.longitude = '-68.150000';
}

function populateForm(center: HealthCenter): void {
  editingId.value = center.id;
  form.nombre = center.nombre;
  form.nivel = center.nivel;
  form.direccion = center.direccion;
  form.ciudad = center.ciudad;
  form.telefono = center.telefono;
  form.telefono_emergencia = center.telefono_emergencia;
  form.horario = center.horario;
  form.ambulancia_disponible = center.ambulancia_disponible;
  form.latitude = String(center.latitude);
  form.longitude = String(center.longitude);
}

async function loadCenters(): Promise<void> {
  const response = await fetch(apiUrl('/health-centers/'));
  centers.value = response.ok ? ((await response.json()) as HealthCenter[]) : [];
}

async function saveCenter(): Promise<void> {
  const payload = {
    nombre: form.nombre,
    nivel: form.nivel,
    direccion: form.direccion,
    ciudad: form.ciudad,
    telefono: form.telefono,
    telefono_emergencia: form.telefono_emergencia,
    horario: form.horario,
    ambulancia_disponible: form.ambulancia_disponible,
    latitude: Number.parseFloat(form.latitude),
    longitude: Number.parseFloat(form.longitude),
  };

  const request = editingId.value
    ? fetch(apiUrl(`/health-centers/${editingId.value}/`), { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
    : fetch(apiUrl('/health-centers/'), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });

  const response = await request;
  if (response.ok) {
    await loadCenters();
    resetForm();
  }
}

onMounted(async () => {
  document.title = 'Admin centros | Mesa de Maternidad';
  await loadCenters();
});
</script>

<style scoped>
.input-base {
  width: 100%;
  border-radius: 1rem;
  border: 1px solid rgb(226 232 240);
  background: rgb(248 250 252);
  padding: 0.75rem 1rem;
  outline: none;
}
</style>
