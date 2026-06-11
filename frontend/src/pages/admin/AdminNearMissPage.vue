<template>
  <div class="admin-page">
    <div class="admin-page-header">
      <div>
        <h1 class="admin-page-title">Morbilidad Materna Extrema (Near-Miss)</h1>
        <p class="admin-page-subtitle">Registro y análisis bajo el enfoque de las "3 Demoras"</p>
      </div>
      <button class="btn btn-primary" @click="openNewModal">
        <i class="pi pi-plus"></i> Nuevo Registro
      </button>
    </div>

    <!-- Data Table -->
    <div class="admin-card">
      <div v-if="loading" class="loading-state">
        <i class="pi pi-spin pi-spinner" style="font-size: 2rem"></i>
        <p>Cargando registros...</p>
      </div>
      <div v-else-if="records.length === 0" class="empty-state">
        <i class="pi pi-folder-open"></i>
        <p>No hay registros de Near-Miss aún.</p>
        <button class="btn btn-outline" @click="openNewModal">Crear el primero</button>
      </div>
      <div v-else class="table-responsive">
        <table class="admin-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Condición</th>
              <th>Edad (Sem)</th>
              <th>Demoras Identificadas</th>
              <th>Estado</th>
              <th>Fecha</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="record in records" :key="record.id">
              <td>#{{ record.id }}</td>
              <td>{{ getConditionLabel(record.condition) }}</td>
              <td>{{ record.patient_age }} ({{ record.gestational_age }} sem)</td>
              <td>
                <div class="delay-badges">
                  <span class="badge" :class="record.delay_1_decision ? 'badge-danger' : 'badge-success'" title="Demora 1: Decisión">D1</span>
                  <span class="badge" :class="record.delay_2_transport ? 'badge-danger' : 'badge-success'" title="Demora 2: Transporte">D2</span>
                  <span class="badge" :class="record.delay_3_care ? 'badge-danger' : 'badge-success'" title="Demora 3: Atención">D3</span>
                </div>
              </td>
              <td>
                <span class="status-badge" :class="record.survival_status === 'survived' ? 'success' : 'danger'">
                  {{ record.survival_status === 'survived' ? 'Sobrevivió' : 'Falleció' }}
                </span>
              </td>
              <td>{{ formatDate(record.created_at) }}</td>
              <td>
                <div class="action-buttons">
                  <button class="btn-icon text-primary" @click="viewRecord(record)" title="Ver detalles">
                    <i class="pi pi-eye"></i>
                  </button>
                  <button class="btn-icon text-danger" @click="confirmDelete(record.id)" title="Eliminar">
                    <i class="pi pi-trash"></i>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Modal Formulario Near-Miss -->
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content large-modal">
        <div class="modal-header">
          <h2>{{ isEditing ? 'Ver/Editar Registro Near-Miss' : 'Nuevo Registro Near-Miss' }}</h2>
          <button class="modal-close" @click="closeModal"><i class="pi pi-times"></i></button>
        </div>
        
        <form @submit.prevent="saveRecord" class="modal-body">
          <!-- Paciente y Condición -->
          <div class="form-section">
            <h3 class="section-title"><i class="pi pi-user"></i> Datos Clínicos Básicos</h3>
            <div class="form-row">
              <div class="form-group">
                <label>Edad de la Paciente</label>
                <input type="number" v-model="formData.patient_age" required min="10" max="60" class="form-control" />
              </div>
              <div class="form-group">
                <label>Edad Gestacional (Semanas)</label>
                <input type="number" v-model="formData.gestational_age" required min="0" max="42" class="form-control" />
              </div>
            </div>
            
            <div class="form-row">
              <div class="form-group">
                <label>Condición Principal (Complicación Severa)</label>
                <select v-model="formData.condition" required class="form-control">
                  <option value="hemorrhage">Hemorragia severa</option>
                  <option value="hypertension">Trastorno hipertensivo severo (Preeclampsia/Eclampsia)</option>
                  <option value="sepsis">Infección sistémica severa / Sepsis</option>
                  <option value="other">Otra complicación severa</option>
                </select>
              </div>
              <div class="form-group">
                <label>Estado de Supervivencia</label>
                <select v-model="formData.survival_status" required class="form-control">
                  <option value="survived">Sobrevivió</option>
                  <option value="deceased">Falleció</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Análisis de las 3 Demoras -->
          <div class="form-section highlight-section">
            <h3 class="section-title"><i class="pi pi-exclamation-triangle"></i> Análisis: Las 3 Demoras</h3>
            <p class="section-desc">Identifique en qué punto(s) se produjo un retraso crítico.</p>
            
            <!-- Demora 1 -->
            <div class="delay-card" :class="{ 'active-delay': formData.delay_1_decision }">
              <div class="delay-header">
                <label class="toggle-switch">
                  <input type="checkbox" v-model="formData.delay_1_decision">
                  <span class="slider round"></span>
                </label>
                <div class="delay-title">
                  <h4>Demora 1: Decisión</h4>
                  <span>Retraso en tomar la decisión de buscar atención médica.</span>
                </div>
              </div>
              <div v-if="formData.delay_1_decision" class="delay-body">
                <label>Detalles de la Demora 1</label>
                <textarea v-model="formData.delay_1_details" rows="2" class="form-control" placeholder="Ej. Falta de conocimiento de señales de peligro, barreras socioculturales, miedo..."></textarea>
              </div>
            </div>

            <!-- Demora 2 -->
            <div class="delay-card" :class="{ 'active-delay': formData.delay_2_transport }">
              <div class="delay-header">
                <label class="toggle-switch">
                  <input type="checkbox" v-model="formData.delay_2_transport">
                  <span class="slider round"></span>
                </label>
                <div class="delay-title">
                  <h4>Demora 2: Transporte</h4>
                  <span>Retraso en llegar a una instalación de salud adecuada.</span>
                </div>
              </div>
              <div v-if="formData.delay_2_transport" class="delay-body">
                <label>Detalles de la Demora 2</label>
                <textarea v-model="formData.delay_2_details" rows="2" class="form-control" placeholder="Ej. Distancia larga, falta de transporte, mal estado de caminos, problemas económicos..."></textarea>
              </div>
            </div>

            <!-- Demora 3 -->
            <div class="delay-card" :class="{ 'active-delay': formData.delay_3_care }">
              <div class="delay-header">
                <label class="toggle-switch">
                  <input type="checkbox" v-model="formData.delay_3_care">
                  <span class="slider round"></span>
                </label>
                <div class="delay-title">
                  <h4>Demora 3: Atención</h4>
                  <span>Retraso en recibir atención adecuada y oportuna en el centro de salud.</span>
                </div>
              </div>
              <div v-if="formData.delay_3_care" class="delay-body">
                <label>Detalles de la Demora 3</label>
                <textarea v-model="formData.delay_3_details" rows="2" class="form-control" placeholder="Ej. Falta de insumos, personal no disponible, mala referencia, demoras administrativas..."></textarea>
              </div>
            </div>
          </div>

          <div class="form-section">
            <h3 class="section-title"><i class="pi pi-pencil"></i> Notas Adicionales</h3>
            <textarea v-model="formData.notes" rows="3" class="form-control" placeholder="Observaciones generales sobre el caso..."></textarea>
          </div>

          <div class="modal-footer">
            <button type="button" class="btn btn-outline" @click="closeModal">Cancelar</button>
            <button type="submit" class="btn btn-primary" :disabled="saving">
              <i class="pi pi-save" v-if="!saving"></i>
              <i class="pi pi-spin pi-spinner" v-else></i>
              {{ saving ? 'Guardando...' : 'Guardar Registro' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

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
    const res = await fetch(`${API_URL}/api/near-miss/`);
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
      ? `${API_URL}/api/near-miss/${formData.value.id}/` 
      : `${API_URL}/api/near-miss/`;
      
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
      const res = await fetch(`${API_URL}/api/near-miss/${id}/`, {
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
    hemorrhage: 'Hemorragia',
    hypertension: 'Trast. Hipertensivo',
    sepsis: 'Sepsis',
    other: 'Otra'
  };
  return map[val] || val;
};

const formatDate = (dateString?: string) => {
  if (!dateString) return '';
  return new Date(dateString).toLocaleDateString('es-ES');
};
</script>

<style scoped>
.large-modal {
  max-width: 800px;
  width: 90%;
}

.form-section {
  background-color: #f8fafc;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  border: 1px solid #e2e8f0;
}

.highlight-section {
  background-color: #fffaf0;
  border-color: #fbd38d;
}

.section-title {
  margin-top: 0;
  margin-bottom: 0.5rem;
  color: #1e293b;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.25rem;
}

.section-desc {
  color: #64748b;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
}

.form-row {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1rem;
}
.form-row .form-group {
  flex: 1;
}

.delay-card {
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
}

.active-delay {
  border-color: #f6ad55;
  box-shadow: 0 4px 6px -1px rgba(237, 137, 54, 0.1);
}

.delay-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.delay-title h4 {
  margin: 0 0 0.25rem 0;
  color: #2d3748;
}

.delay-title span {
  font-size: 0.85rem;
  color: #718096;
}

.delay-body {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px dashed #e2e8f0;
  animation: slideDown 0.3s ease-out;
}

.delay-badges {
  display: flex;
  gap: 0.5rem;
}

.badge {
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
}

.badge-success {
  background-color: #c6f6d5;
  color: #22543d;
}

.badge-danger {
  background-color: #fed7d7;
  color: #742a2a;
}

/* Toggle Switch Styles */
.toggle-switch {
  position: relative;
  display: inline-block;
  width: 46px;
  height: 24px;
  flex-shrink: 0;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #cbd5e0;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .4s;
}

input:checked + .slider {
  background-color: #ed8936;
}

input:focus + .slider {
  box-shadow: 0 0 1px #ed8936;
}

input:checked + .slider:before {
  transform: translateX(22px);
}

.slider.round {
  border-radius: 24px;
}

.slider.round:before {
  border-radius: 50%;
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
  .form-row {
    flex-direction: column;
    gap: 0;
  }
}
</style>
