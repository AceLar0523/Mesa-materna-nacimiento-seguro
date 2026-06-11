<template>
  <div class="p-6">
    <div class="mb-6 flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
      <div>
        <h1 class="text-2xl font-bold tracking-tight text-slate-900">Inteligencia Territorial</h1>
        <p class="text-slate-500">Mapas de calor y densidad de alertas basados en Kernel Density Estimation (KDE)</p>
      </div>
      <div class="flex gap-2">
        <button 
          class="rounded-lg bg-indigo-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          @click="loadHeatmapData"
        >
          <i class="pi pi-refresh mr-2"></i> Actualizar
        </button>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2">
        <div class="rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden">
          <div class="border-b border-slate-200 bg-slate-50 px-4 py-3">
            <h3 class="font-semibold text-slate-800">Mapa de Calor (Densidad)</h3>
          </div>
          <div ref="mapContainer" class="h-[600px] w-full relative z-0"></div>
        </div>
      </div>
      
      <div class="space-y-6">
        <div class="rounded-xl border border-slate-200 bg-white shadow-sm p-5">
          <h3 class="font-semibold text-slate-800 mb-4">Métricas de Análisis</h3>
          <div class="space-y-4">
            <div class="rounded-lg bg-red-50 p-4 border border-red-100">
              <p class="text-xs font-bold uppercase tracking-wider text-red-600 mb-1">Zonas Críticas</p>
              <p class="text-sm text-slate-700">Las zonas en rojo intenso indican alta concentración de alertas con síntomas graves como hemorragias o preeclampsia.</p>
            </div>
            
            <div class="rounded-lg bg-orange-50 p-4 border border-orange-100">
              <p class="text-xs font-bold uppercase tracking-wider text-orange-600 mb-1">Algoritmo</p>
              <p class="text-sm text-slate-700">Se utiliza <strong>Gaussian KDE</strong> (Kernel Density Estimation) procesado en el servidor para calcular la distribución de densidad probabilística.</p>
            </div>
          </div>
        </div>

        <div class="rounded-xl border border-slate-200 bg-white shadow-sm p-5">
          <h3 class="font-semibold text-slate-800 mb-4">Leyenda</h3>
          <div class="space-y-3">
            <div class="flex items-center gap-3">
              <div class="w-6 h-6 rounded-full bg-[#ef4444] opacity-80 border border-red-600"></div>
              <span class="text-sm font-medium text-slate-700">Densidad Alta (Casos Críticos)</span>
            </div>
            <div class="flex items-center gap-3">
              <div class="w-6 h-6 rounded-full bg-[#f97316] opacity-70 border border-orange-600"></div>
              <span class="text-sm font-medium text-slate-700">Densidad Media</span>
            </div>
            <div class="flex items-center gap-3">
              <div class="w-6 h-6 rounded-full bg-[#eab308] opacity-60 border border-yellow-600"></div>
              <span class="text-sm font-medium text-slate-700">Densidad Baja</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { apiUrl } from '@/utils/api';

const mapContainer = ref<HTMLDivElement | null>(null);
let mapInstance: L.Map | null = null;
let heatmapLayerGroup: L.LayerGroup | null = null;
const heatmapPoints = ref<Array<{lat: number, lng: number, density: number}>>([]);

function createMap() {
  if (!mapContainer.value || mapInstance) return;

  // Centro en Bolivia
  mapInstance = L.map(mapContainer.value).setView([-16.5, -68.15], 6);

  L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 20
  }).addTo(mapInstance);

  heatmapLayerGroup = L.layerGroup().addTo(mapInstance);
}

function getColor(density: number) {
  // Retorna color basado en la densidad (0 a 1)
  if (density > 0.7) return '#ef4444'; // Red-500
  if (density > 0.4) return '#f97316'; // Orange-500
  return '#eab308'; // Yellow-500
}

function getOpacity(density: number) {
  // Transparencia dinámica según la densidad
  if (density > 0.7) return 0.8;
  if (density > 0.4) return 0.6;
  return 0.4;
}

function renderHeatmap() {
  if (!mapInstance || !heatmapLayerGroup) return;

  heatmapLayerGroup.clearLayers();

  if (heatmapPoints.value.length === 0) return;

  const bounds: L.LatLngExpression[] = [];

  for (const point of heatmapPoints.value) {
    const lat = point.lat;
    const lng = point.lng;
    
    // Si la densidad es muy baja y no estamos devolviendo todos los puntos
    if (point.density <= 0.05) continue;

    const circle = L.circleMarker([lat, lng], {
      radius: 25, // Radio amplio para que se solapen y parezca heatmap
      color: 'transparent',
      weight: 0,
      fillColor: getColor(point.density),
      fillOpacity: getOpacity(point.density),
    });

    circle.bindPopup(`Densidad: ${(point.density * 100).toFixed(1)}%`);
    circle.addTo(heatmapLayerGroup);
    bounds.push([lat, lng]);
  }

  if (bounds.length > 0) {
    mapInstance.fitBounds(L.latLngBounds(bounds), { padding: [50, 50] });
  }
}

async function loadHeatmapData() {
  try {
    const response = await fetch(apiUrl('/heatmap/'));
    if (response.ok) {
      const data = await response.json();
      if (data && data.data) {
        heatmapPoints.value = data.data;
        renderHeatmap();
      }
    }
  } catch (error) {
    console.error('Error fetching heatmap data:', error);
  }
}

onMounted(() => {
  createMap();
  loadHeatmapData();
});

onBeforeUnmount(() => {
  if (mapInstance) {
    mapInstance.remove();
    mapInstance = null;
    heatmapLayerGroup = null;
  }
});
</script>

<style scoped>
/* Evitar problemas de z-index de leaflet con los popups y modales de la app */
:deep(.leaflet-pane) {
  z-index: 10;
}
:deep(.leaflet-top),
:deep(.leaflet-bottom) {
  z-index: 40;
}
</style>
