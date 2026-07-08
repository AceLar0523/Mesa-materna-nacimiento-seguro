<template>
  <div class="min-h-screen overflow-hidden bg-[radial-gradient(circle_at_top,_rgba(20,184,166,0.16),_transparent_34%),linear-gradient(180deg,#effdfb_0%,#ffffff_54%,#fff7ed_100%)] pt-20 text-slate-900">
    <PageHero
      :kicker="$t('geolocalizador_centros_page.kicker_public_sector')"
      :title="$t('geolocalizador_centros_page.title_health_center_geolocator')"
      :subtitle="$t('geolocalizador_centros_page.subtitle_geolocator')"
      backgroundImage="/img/fondo14.avif"
    />

    <section class="mx-auto grid max-w-7xl gap-8 px-4 py-12 sm:px-6 lg:grid-cols-[0.98fr_1.02fr] lg:px-8">
      <div class="space-y-6">
        <div class="rounded-[2.2rem] border border-teal-100 bg-white/92 p-6 shadow-[0_25px_80px_-38px_rgba(20,184,166,0.55)] backdrop-blur">
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.3em] text-teal-600">{{ $t('geolocalizador_centros_page.active_location') }}</p>
              <h2 class="mt-2 text-2xl font-black text-slate-900">{{ $t('geolocalizador_centros_page.centers_sorted_by_distance') }}</h2>
            </div>
            <div class="rounded-2xl bg-teal-50 px-4 py-2 text-sm font-semibold text-teal-700">
              {{ currentPositionLabel }}
            </div>
          </div>

          <div class="mt-6 grid gap-4 md:grid-cols-3">
            <article class="rounded-[1.8rem] border border-teal-100 bg-gradient-to-br from-teal-50 via-white to-white p-5 shadow-sm">
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-teal-600">{{ $t('geolocalizador_centros_page.centers') }}</p>
              <p class="mt-3 text-5xl font-black text-slate-900">{{ centers.length }}</p>
              <p class="mt-1 text-sm text-slate-600">{{ $t('geolocalizador_centros_page.description_centers') }}</p>
            </article>
            <article class="rounded-[1.8rem] border border-orange-100 bg-gradient-to-br from-orange-50 via-white to-white p-5 shadow-sm">
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-orange-500">{{ $t('geolocalizador_centros_page.filtered') }}</p>
              <p class="mt-3 text-5xl font-black text-slate-900">{{ visibleCenters.length }}</p>
              <p class="mt-1 text-sm text-slate-600">{{ activeLevelLabel }}</p>
            </article>
            <article class="rounded-[1.8rem] border border-rose-100 bg-gradient-to-br from-rose-50 via-white to-white p-5 shadow-sm">
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-rose-500">{{ $t('geolocalizador_centros_page.nearest') }}</p>
              <p class="mt-3 text-2xl font-black text-slate-900">{{ nearestCenter?.nombre ?? $t('geolocalizador_centros_page.zero_value') }}</p>
              <p class="mt-1 text-sm text-slate-600">{{ nearestCenter ? `${nearestCenter.distance.toFixed(1)} km` : $t('geolocalizador_centros_page.zero_km') }}</p>
            </article>
          </div>

          <div class="mt-6 space-y-3">
            <p class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">{{ $t('geolocalizador_centros_page.complexity_level') }}</p>
            <div class="flex flex-wrap gap-2">
              <button
                v-for="level in levelFilters"
                :key="level.key"
                type="button"
                class="rounded-full px-4 py-2 text-sm font-semibold transition"
                :class="activeLevel === level.key ? 'bg-slate-950 text-white shadow-lg' : 'bg-slate-100 text-slate-600 hover:bg-teal-50 hover:text-teal-700'"
                @click="activeLevel = level.key"
              >
                {{ level.label }}
              </button>
            </div>
          </div>

          <div class="mt-6 grid gap-4 md:grid-cols-2">
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">{{ $t('geolocalizador_centros_page.manual_latitude') }}</span>
              <input v-model="manualLatitude" type="number" step="0.000001" class="input-base" />
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">{{ $t('geolocalizador_centros_page.manual_longitude') }}</span>
              <input v-model="manualLongitude" type="number" step="0.000001" class="input-base" />
            </label>
          </div>

          <div class="mt-6 flex flex-wrap gap-3">
            <button
              type="button"
              class="rounded-full bg-gradient-to-r from-[#0F766E] to-[#14B8A6] px-5 py-3 text-sm font-bold text-white shadow-lg shadow-teal-200 transition hover:-translate-y-0.5"
              @click="requestCurrentLocation"
            >
              {{ $t('geolocalizador_centros_page.detect_my_location') }}
            </button>
            <button
              type="button"
              class="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 transition hover:border-teal-200 hover:text-teal-700"
              @click="applyManualPosition"
            >
              {{ $t('geolocalizador_centros_page.use_manual_coordinates') }}
            </button>
            <button
              type="button"
              class="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 transition hover:border-teal-200 hover:text-teal-700"
              @click="loadCenters"
            >
              {{ $t('geolocalizador_centros_page.update_centers') }}
            </button>
          </div>

          <p class="mt-4 text-sm text-slate-500">{{ statusMessage }}</p>
          <p class="mt-2 text-xs font-semibold uppercase tracking-[0.2em] text-slate-400">{{ $t('geolocalizador_centros_page.last_sync') }}: {{ lastSyncLabel }}</p>
        </div>

        <div class="space-y-4">
          <article
            v-for="center in sortedCenters"
            :key="center.id"
            class="group rounded-[1.75rem] border bg-white p-5 shadow-sm transition hover:-translate-y-1 hover:shadow-xl"
            :class="activeCenter?.id === center.id ? 'border-teal-300 ring-4 ring-teal-50' : 'border-slate-200'"
            @click="activeCenter = center"
          >
            <div class="flex flex-wrap items-start justify-between gap-4">
              <div>
                <div class="flex items-center gap-3">
                  <span class="rounded-full px-3 py-1 text-xs font-bold" :class="levelBadgeClass(center.nivel)">{{ center.nivel }}</span>
                  <h3 class="text-lg font-black text-slate-900">{{ center.nombre }}</h3>
                </div>
                <p class="mt-2 text-sm text-slate-600">{{ center.direccion }} · {{ center.ciudad }}</p>
              </div>
              <div class="text-right">
                <p class="text-sm font-bold text-teal-600">{{ center.distance.toFixed(1) }} km</p>
                <p class="text-xs text-slate-500">{{ $t('geolocalizador_centros_page.from_your_position') }}</p>
              </div>
            </div>

            <div class="mt-4 flex flex-wrap gap-2 text-xs font-semibold text-slate-600">
              <span class="rounded-full bg-slate-100 px-3 py-1">{{ center.horario || $t('geolocalizador_centros_page.schedule_not_loaded') }}</span>
              <span class="rounded-full bg-slate-100 px-3 py-1">{{ center.telefono }}</span>
              <span class="rounded-full bg-slate-100 px-3 py-1">{{ center.ambulancia_disponible ? $t('geolocalizador_centros_page.ambulance_available') : $t('geolocalizador_centros_page.no_ambulance') }}</span>
            </div>
          </article>
        </div>
      </div>

      <aside class="space-y-6 lg:sticky lg:top-28 lg:self-start">
        <div class="rounded-[2rem] border border-teal-100 bg-white p-4 shadow-[0_35px_90px_-40px_rgba(15,23,42,0.95)]">
          <div class="rounded-[1.65rem] border border-white/10 bg-[radial-gradient(circle_at_top,_rgba(20,184,166,0.24),_transparent_32%),linear-gradient(180deg,rgba(15,118,110,0.92),rgba(15,23,42,0.96))] p-5 text-white">
            <div class="flex items-center justify-between gap-3">
              <div>
                <p class="text-xs font-bold uppercase tracking-[0.35em] text-teal-200">{{ $t('geolocalizador_centros_page.interactive_map') }}</p>
                <h2 class="mt-2 text-2xl font-black">{{ $t('geolocalizador_centros_page.leaflet_realtime') }}</h2>
              </div>
              <div class="rounded-2xl bg-white/10 px-3 py-2 text-xs font-semibold text-teal-100">
                {{ activeLevelLabel }}
              </div>
            </div>

            <div ref="mapContainer" class="mt-6 h-[520px] overflow-hidden rounded-[1.5rem] border border-white/10"></div>
          </div>
        </div>

        <div v-if="activeCenter" class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-lg">
          <p class="text-xs font-bold uppercase tracking-[0.3em] text-slate-500">{{ $t('geolocalizador_centros_page.quick_sheet') }}</p>
          <h3 class="mt-2 text-2xl font-black text-slate-900">{{ activeCenter.nombre }}</h3>
          <div class="mt-4 space-y-3 text-sm text-slate-600">
            <p><strong class="text-slate-800">{{ $t('geolocalizador_centros_page.address') }}:</strong> {{ activeCenter.direccion }}</p>
            <p><strong class="text-slate-800">{{ $t('geolocalizador_centros_page.phone') }}:</strong> {{ activeCenter.telefono }}</p>
            <p><strong class="text-slate-800">{{ $t('geolocalizador_centros_page.emergency') }}:</strong> {{ activeCenter.telefono_emergencia || $t('geolocalizador_centros_page.not_registered') }}</p>
            <p><strong class="text-slate-800">{{ $t('geolocalizador_centros_page.ambulance') }}:</strong> {{ activeCenter.ambulancia_disponible ? $t('geolocalizador_centros_page.available') : $t('geolocalizador_centros_page.not_available') }}</p>
          </div>
        </div>

        <div v-if="errorMessage" class="rounded-[2rem] border border-rose-100 bg-rose-50 p-5 text-sm text-rose-700">
          {{ errorMessage }}
        </div>
      </aside>
    </section>

    <Footer class="mt-10" />
  </div>
</template>

<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import Footer from '@/components/landing/Footer/Footer.vue';
import PageHero from '@/components/common/PageHero.vue';
import { apiUrl } from '@/utils/api';
import { calculateDistanceKm, toApiList, type GeoPoint, type HealthCenter, type PublicSectorLevel, type PublicSectorLevelFilter, toNumber } from './public-sector';
import { useI18n } from 'vue-i18n'; // Import useI18n

const { t } = useI18n(); // Initialize useI18n

type CenterWithDistance = HealthCenter & { distance: number };

const demoCenters: HealthCenter[] = [
  { id: 1001, nombre: 'Hospital Municipal La Paz', nivel: 'II', direccion: 'Av. 16 de Julio 1234', ciudad: 'La Paz', telefono: '+591 2 222 1111', telefono_emergencia: '+591 2 222 1112', horario: '24 horas', ambulancia_disponible: true, latitude: '-16.4990', longitude: '-68.1330', created_at: new Date().toISOString(), updated_at: new Date().toISOString() },
  { id: 1002, nombre: 'Hospital de Clínicas', nivel: 'III', direccion: 'Calle Ingavi y Potosí', ciudad: 'La Paz', telefono: '+591 2 220 1000', telefono_emergencia: '+591 2 220 1001', horario: '24 horas', ambulancia_disponible: true, latitude: '-16.5137', longitude: '-68.1193', created_at: new Date().toISOString(), updated_at: new Date().toISOString() },
  { id: 1003, nombre: 'Hospital Municipal Cochabamba', nivel: 'II', direccion: 'Av. Aniceto Arce 100', ciudad: 'Cochabamba', telefono: '+591 4 444 2100', telefono_emergencia: '+591 4 444 2101', horario: '24 horas', ambulancia_disponible: true, latitude: '-17.3934', longitude: '-66.1570', created_at: new Date().toISOString(), updated_at: new Date().toISOString() },
  { id: 1004, nombre: 'Centro de Salud Sur', nivel: 'I', direccion: 'Zona Sur, Av. Oquendo', ciudad: 'Cochabamba', telefono: '+591 4 444 1120', telefono_emergencia: '+591 4 444 1121', horario: 'Lun a sáb 08:00 - 20:00', ambulancia_disponible: false, latitude: '-17.4150', longitude: '-66.1590', created_at: new Date().toISOString(), updated_at: new Date().toISOString() },
  { id: 1005, nombre: 'Hospital Municipal Santa Cruz', nivel: 'II', direccion: 'Barrio Equipetrol Norte', ciudad: 'Santa Cruz', telefono: '+591 3 333 2200', telefono_emergencia: '+591 3 333 2201', horario: '24 horas', ambulancia_disponible: true, latitude: '-17.7817', longitude: '-63.1810', created_at: new Date().toISOString(), updated_at: new Date().toISOString() },
  { id: 1006, nombre: 'Centro Integral de Salud Warnes', nivel: 'I', direccion: 'Av. Principal 450', ciudad: 'Warnes', telefono: '+591 3 333 7780', telefono_emergencia: '+591 3 333 7781', horario: 'Lun a dom 07:00 - 22:00', ambulancia_disponible: false, latitude: '-17.5070', longitude: '-63.1670', created_at: new Date().toISOString(), updated_at: new Date().toISOString() },
  { id: 1007, nombre: 'Hospital de la Mujer', nivel: 'III', direccion: 'Av. América y Pando', ciudad: 'Cochabamba', telefono: '+591 4 401 0000', telefono_emergencia: '+591 4 401 0001', horario: '24 horas', ambulancia_disponible: true, latitude: '-17.3846', longitude: '-66.1694', created_at: new Date().toISOString(), updated_at: new Date().toISOString() },
];

const centers = ref<HealthCenter[]>([]);
const errorMessage = ref('');
const activeLevel = ref<PublicSectorLevelFilter>('all');
const activeCenter = ref<CenterWithDistance | null>(null);
const currentPosition = ref<GeoPoint>({ latitude: -16.5, longitude: -68.15 });
const manualLatitude = ref('-16.500000');
const manualLongitude = ref('-68.150000');
const statusMessage = ref(t('geolocalizador_centros_page.status_loading_centers'));
const lastSyncAt = ref<Date | null>(null);
const mapContainer = ref<HTMLDivElement | null>(null);

let mapInstance: L.Map | null = null;
let currentPositionLayer: L.CircleMarker | null = null;
let centerLayerGroup: L.LayerGroup | null = null;
let watchId: number | null = null;
let refreshIntervalId: number | null = null;

const levelFilters: Array<{ key: PublicSectorLevelFilter; label: string }> = [
  { key: 'all', label: t('geolocalizador_centros_page.filter_all') },
  { key: 'I', label: t('geolocalizador_centros_page.filter_level_i') },
  { key: 'II', label: t('geolocalizador_centros_page.filter_level_ii') },
  { key: 'III', label: t('geolocalizador_centros_page.filter_level_iii') },
];

const activeLevelLabel = computed(() => levelFilters.find((item) => item.key === activeLevel.value)?.label ?? t('geolocalizador_centros_page.filter_all'));
const currentPositionLabel = computed(() => `${currentPosition.value.latitude.toFixed(4)}, ${currentPosition.value.longitude.toFixed(4)}`);
const lastSyncLabel = computed(() => {
  if (!lastSyncAt.value) {
    return t('geolocalizador_centros_page.not_synced');
  }

  return lastSyncAt.value.toLocaleTimeString('es-BO', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  });
});

const visibleCenters = computed<CenterWithDistance[]>(() => {
  const filtered = activeLevel.value === 'all' ? centers.value : centers.value.filter((center) => center.nivel === activeLevel.value);

  return filtered
    .map((center) => ({
      ...center,
      distance: calculateDistanceKm(currentPosition.value, { latitude: toNumber(center.latitude), longitude: toNumber(center.longitude) }),
    }))
    .sort((a, b) => a.distance - b.distance);
});

const sortedCenters = computed(() => visibleCenters.value);
const nearestCenter = computed(() => sortedCenters.value[0] ?? null);

function levelBadgeClass(level: PublicSectorLevel): string {
  if (level === 'I') return 'bg-emerald-50 text-emerald-700';
  if (level === 'II') return 'bg-teal-50 text-teal-700';
  return 'bg-orange-50 text-[#EA580C]';
}

function createMap(): void {
  if (!mapContainer.value || mapInstance) {
    return;
  }

  mapInstance = L.map(mapContainer.value, { zoomControl: true, scrollWheelZoom: true }).setView([currentPosition.value.latitude, currentPosition.value.longitude], 12);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors',
    maxZoom: 18,
  }).addTo(mapInstance);

  centerLayerGroup = L.layerGroup().addTo(mapInstance);
  currentPositionLayer = L.circleMarker([currentPosition.value.latitude, currentPosition.value.longitude], {
    radius: 10,
    color: '#ffffff',
    weight: 3,
    fillColor: '#F97316',
    fillOpacity: 1,
  }).addTo(mapInstance);

  currentPositionLayer.bindPopup(t('geolocalizador_centros_page.your_current_location'));
  renderMapLayers();
}

function renderMapLayers(): void {
  if (!mapInstance || !centerLayerGroup || !currentPositionLayer) {
    return;
  }

  centerLayerGroup.clearLayers();
  currentPositionLayer.setLatLng([currentPosition.value.latitude, currentPosition.value.longitude]);

  const bounds: L.LatLngExpression[] = [[currentPosition.value.latitude, currentPosition.value.longitude]];

  for (const center of visibleCenters.value) {
    const latitude = toNumber(center.latitude);
    const longitude = toNumber(center.longitude);
    const circle = L.circleMarker([latitude, longitude], {
      radius: center.nivel === 'III' ? 11 : center.nivel === 'II' ? 10 : 9,
      color: '#ffffff',
      weight: 2,
      fillColor: center.nivel === 'III' ? '#FB7185' : center.nivel === 'II' ? '#14B8A6' : '#0F766E',
      fillOpacity: 0.95,
    });

    circle.bindPopup(`
      <div style="min-width: 180px">
        <strong>${center.nombre}</strong><br />
        <span>${center.direccion}</span><br />
        <span>${center.ciudad}</span><br />
        <span>${center.distance.toFixed(1)} km</span>
      </div>
    `);

    circle.addTo(centerLayerGroup);
    bounds.push([latitude, longitude]);
  }

  mapInstance.fitBounds(L.latLngBounds(bounds), { padding: [30, 30], maxZoom: 14 });

  if (!activeCenter.value) {
    activeCenter.value = visibleCenters.value[0] ?? null;
  }
}

async function loadCenters(): Promise<void> {
  try {
    const response = await fetch(apiUrl('/health-centers/'), {
      cache: 'no-store',
    });
    if (!response.ok) {
      throw new Error('No fue posible cargar los centros desde la API.');
    }

    const payload = (await response.json()) as unknown;
    const data = toApiList<HealthCenter>(payload);
    centers.value = data.length > 0 ? data : demoCenters;
    statusMessage.value = data.length > 0 ? t('geolocalizador_centros_page.status_synced') : t('geolocalizador_centros_page.status_no_centers_demo');
    lastSyncAt.value = new Date();
  } catch (error) {
    centers.value = demoCenters;
    statusMessage.value = t('geolocalizador_centros_page.status_api_error_demo');
    errorMessage.value = error instanceof Error ? error.message : t('geolocalizador_centros_page.error_unexpected_load_centers');
    lastSyncAt.value = new Date();
  }
}

function applyManualPosition(): void {
  const latitude = Number.parseFloat(manualLatitude.value);
  const longitude = Number.parseFloat(manualLongitude.value);

  if (Number.isNaN(latitude) || Number.isNaN(longitude)) {
    statusMessage.value = t('geolocalizador_centros_page.status_enter_valid_coordinates');
    return;
  }

  currentPosition.value = { latitude, longitude };
  statusMessage.value = t('geolocalizador_centros_page.status_manual_position_updated');
}

async function fallbackByIp(): Promise<void> {
  try {
    const response = await fetch('https://ipwho.is/?fields=success,latitude,longitude,message');
    const data = (await response.json()) as { success: boolean; latitude?: number; longitude?: number; message?: string };

    if (data.success && typeof data.latitude === 'number' && typeof data.longitude === 'number') {
      currentPosition.value = { latitude: data.latitude, longitude: data.longitude };
      manualLatitude.value = data.latitude.toFixed(6);
      manualLongitude.value = data.longitude.toFixed(6);
      statusMessage.value = t('geolocalizador_centros_page.status_gps_not_available_ip_fallback');
      return;
    }
  } catch {
    // Fallback silencioso; se mantiene la posición manual por defecto.
  }

  statusMessage.value = t('geolocalizador_centros_page.status_cannot_get_auto_location');
}

function requestCurrentLocation(): void {
  if (!navigator.geolocation) {
    void fallbackByIp();
    return;
  }

  watchId = navigator.geolocation.watchPosition(
    (position) => {
      currentPosition.value = { latitude: position.coords.latitude, longitude: position.coords.longitude };
      manualLatitude.value = position.coords.latitude.toFixed(6);
      manualLongitude.value = position.coords.longitude.toFixed(6);
      statusMessage.value = t('geolocalizador_centros_page.status_location_updated_realtime');
    },
    () => {
      void fallbackByIp();
    },
    { enableHighAccuracy: true, timeout: 12000, maximumAge: 60000 }
  );
}

watch([visibleCenters, currentPosition], () => {
  renderMapLayers();
  activeCenter.value = visibleCenters.value[0] ?? null;
}, { deep: true });

onMounted(async () => {
  document.title = t('geolocalizador_centros_page.document_title');
  await loadCenters();
  await nextTick();
  createMap();
  requestCurrentLocation();
  refreshIntervalId = window.setInterval(() => {
    void loadCenters();
  }, 10000);
});

onBeforeUnmount(() => {
  if (watchId !== null && navigator.geolocation) {
    navigator.geolocation.clearWatch(watchId);
  }

  mapInstance?.remove();
  mapInstance = null;
  centerLayerGroup = null;
  currentPositionLayer = null;

  if (refreshIntervalId !== null) {
    window.clearInterval(refreshIntervalId);
  }
});
</script>

<style scoped>
.input-base {
  width: 100%;
  border-radius: 1.25rem;
  border: 1px solid rgb(226 232 240);
  background: rgb(248 250 252);
  padding: 0.75rem 1rem;
  color: rgb(15 23 42);
  outline: none;
  transition: all 0.2s ease;
}

.input-base:focus {
  border-color: rgb(20 184 166);
  box-shadow: 0 0 0 4px rgba(20, 184, 166, 0.12);
}
</style>