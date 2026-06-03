<template>
  <div class="pt-20 bg-[#f8fafc] min-h-screen">
    <PageHero
      kicker="Indicadores"
      title="Visualización de Impacto"
      subtitle="Monitoreo en tiempo real de los indicadores de salud materna y neonatal en Bolivia. Datos oficiales procesados por la Mesa Nacional de Maternidad y Nacimiento Seguros."
      backgroundImage="/img/fondo8.jpg"
    />

    <section class="py-12 -mt-10 relative z-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div v-for="(stat, index) in stats" :key="index" 
               class="bg-white p-8 rounded-3xl shadow-sm border border-gray-100 hover:shadow-xl transition-all duration-500 transform hover:-translate-y-2">
            <div class="text-[#F97316] mb-4">
              <i :class="['pi text-3xl', stat.icon]"></i>
            </div>
            <div class="text-4xl font-black text-gray-900 mb-2">
              {{ stat.current.toLocaleString() }}{{ stat.suffix }}
            </div>
            <div class="text-sm font-bold text-gray-400 uppercase tracking-widest">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        
        <div class="bg-white p-10 rounded-3xl shadow-sm border border-gray-100 animate-fade-in-up">
          <div class="flex justify-between items-center mb-10">
            <h3 class="text-2xl font-bold text-gray-900">Cobertura de Parto Institucional</h3>
            <span class="text-green-500 font-bold bg-green-50 px-3 py-1 rounded-full text-xs">+12% vs 2020</span>
          </div>
          <div class="relative h-64 w-full">
            <svg viewBox="0 0 1000 400" class="w-full h-full">
              <defs>
                <linearGradient id="grad" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" style="stop-color:#F97316;stop-opacity:0.3" />
                  <stop offset="100%" style="stop-color:#F97316;stop-opacity:0" />
                </linearGradient>
              </defs>
              <path d="M0,350 Q150,300 300,280 T600,180 T1000,100 L1000,400 L0,400 Z" fill="url(#grad)" />
              <path d="M0,350 Q150,300 300,280 T600,180 T1000,100" fill="none" stroke="#F97316" stroke-width="8" class="animate-draw-path" />
              <circle cx="1000" cy="100" r="10" fill="#F97316" class="animate-pulse" />
            </svg>
            <div class="flex justify-between mt-4 text-xs font-bold text-gray-400">
              <span>2021</span><span>2022</span><span>2023</span><span>2024</span><span>2025 (PROY)</span>
            </div>
          </div>
          <p class="mt-8 text-sm text-gray-500 italic">
            * El incremento refleja el éxito de la política SAFCI en comunidades rurales de difícil acceso.
          </p>
        </div>

        <div class="bg-white p-10 rounded-3xl shadow-sm border border-gray-100 animate-fade-in-up delay-200">
          <h3 class="text-2xl font-bold text-gray-900 mb-10">Distribución de Kits Médicos</h3>
          <div class="space-y-6">
            <div v-for="dept in departamentos" :key="dept.name">
              <div class="flex justify-between text-sm font-bold mb-2">
                <span class="text-gray-700">{{ dept.name }}</span>
                <span class="text-[#F97316]">{{ dept.value }}%</span>
              </div>
              <div class="w-full bg-gray-100 h-3 rounded-full overflow-hidden">
                 <div class="bg-[#F97316] h-full rounded-full transition-all duration-1000 ease-out" 
                     :style="{ width: animateBars ? dept.value + '%' : '0%' }"></div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-3xl shadow-sm border border-gray-100 overflow-hidden">
        <div class="p-8 border-b border-gray-100 flex items-center gap-4">
          <div class="w-12 h-12 bg-orange-50 text-[#F97316] rounded-2xl flex items-center justify-center">
            <i class="pi pi-table text-xl"></i>
          </div>
          <h3 class="text-2xl font-bold text-gray-900">Detalle de Inversión Interinstitucional</h3>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left">
            <thead class="bg-gray-50 text-gray-500 text-xs font-bold uppercase tracking-wider">
              <tr>
                <th class="px-8 py-6">Programa</th>
                <th class="px-8 py-6">Institución</th>
                <th class="px-8 py-6">Inversión (USD)</th>
                <th class="px-8 py-6">Estado</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100">
              <tr v-for="item in inversionData" :key="item.id" class="hover:bg-gray-50/50 transition-colors">
                <td class="px-8 py-6 font-bold text-gray-800">{{ item.programa }}</td>
                <td class="px-8 py-6 text-gray-600">
                  <span class="bg-orange-50 text-[#F97316] px-3 py-1 rounded-full text-xs font-bold">{{ item.institucion }}</span>
                </td>
                <td class="px-8 py-6 text-gray-900 font-mono font-bold">${{ item.monto.toLocaleString() }}</td>
                <td class="px-8 py-6">
                  <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-green-500"></span>
                    <span class="text-sm font-medium text-gray-700">{{ item.estado }}</span>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '../components/landing/Footer/Footer.vue';

const animateBars = ref(false);

const stats = ref([
  { label: 'Kits Entregados', current: 12540, suffix: '', icon: 'pi-box' },
  { label: 'Partos Seguros', current: 85, suffix: '%', icon: 'pi-heart-fill' },
  { label: 'Personal Capacitado', current: 3200, suffix: '+', icon: 'pi-users' },
  { label: 'Centros Equipados', current: 412, suffix: '', icon: 'pi-building' }
]);

const departamentos = [
  { name: 'La Paz', value: 92 },
  { name: 'Santa Cruz', value: 88 },
  { name: 'Potosí', value: 65 },
  { name: 'Beni', value: 45 },
  { name: 'Chuquisaca', value: 78 }
];

const inversionData = [
  { id: 1, programa: 'Equipamiento Neonatal', institucion: 'MNMNS', monto: 1250000, estado: 'Ejecutado' },
  { id: 2, programa: 'Fortalecimiento Casas Maternas', institucion: 'MNMNS', monto: 850000, estado: 'En curso' },
  { id: 3, programa: 'Kits de Parto Limpio', institucion: 'MNMNS', monto: 420000, estado: 'Ejecutado' },
  { id: 4, programa: 'Capacitación Intercultural', institucion: 'Ministerio de Salud', monto: 310000, estado: 'En curso' }
];

onMounted(() => {
  document.title = 'Datos y Estadísticas | MNMNS Bolivia';
  window.scrollTo(0, 0);
  
  // Disparar animación de barras después de un pequeño delay
  setTimeout(() => {
    animateBars.value = true;
  }, 500);
});
</script>

<style scoped>
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes drawPath {
  from { stroke-dasharray: 0, 1500; }
  to { stroke-dasharray: 1500, 1500; }
}

.animate-fade-in-up {
  animation: fadeInUp 0.8s ease-out forwards;
}

.animate-draw-path {
  stroke-dasharray: 1500;
  animation: drawPath 2s ease-out forwards;
}

.delay-200 { animation-delay: 0.2s; }

/* Para evitar que las celdas de la tabla se rompan en móvil */
.overflow-x-auto {
  -webkit-overflow-scrolling: touch;
}
</style>