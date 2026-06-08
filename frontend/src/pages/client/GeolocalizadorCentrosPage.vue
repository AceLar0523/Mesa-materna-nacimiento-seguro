<template>
  <div class="min-h-screen overflow-hidden bg-[radial-gradient(circle_at_top,_rgba(20,184,166,0.16),_transparent_34%),linear-gradient(180deg,#effdfb_0%,#ffffff_54%,#fff7ed_100%)] pt-20 text-slate-900">
    <PageHero
      kicker="Sector público"
      title="Geolocalizador de centros de salud"
      subtitle="Detecta tu ubicación, calcula distancia con Haversine y filtra centros por nivel de complejidad con una vista interactiva tipo mapa."
      backgroundImage="/img/fondo14.avif"
    />

    <section class="mx-auto grid max-w-7xl gap-8 px-4 py-12 sm:px-6 lg:grid-cols-[0.95fr_1.05fr] lg:px-8">
      <div class="space-y-6">
        <div class="rounded-[2rem] border border-teal-100 bg-white/90 p-6 shadow-[0_25px_80px_-38px_rgba(20,184,166,0.55)] backdrop-blur">
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.3em] text-teal-600">Ubicación activa</p>
              <h2 class="mt-2 text-2xl font-black text-slate-900">Centros ordenados por distancia</h2>
            </div>
            <div class="rounded-2xl bg-teal-50 px-4 py-2 text-sm font-semibold text-teal-700">
              {{ currentPositionLabel }}
            </div>
          </div>

          <div class="mt-6 grid gap-4 md:grid-cols-3">
            <article class="rounded-3xl border border-teal-100 bg-gradient-to-br from-teal-50 to-white p-4">
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-teal-600">Centros cargados</p>
              <p class="mt-3 text-4xl font-black text-slate-900">{{ centers.length }}</p>
              <p class="mt-1 text-sm text-slate-600">Registros consumidos desde PostgreSQL</p>
            </article>
            <article class="rounded-3xl border border-orange-100 bg-gradient-to-br from-orange-50 to-white p-4">
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-orange-500">Filtrado</p>
              <p class="mt-3 text-4xl font-black text-slate-900">{{ visibleCenters.length }}</p>
              <p class="mt-1 text-sm text-slate-600">{{ activeLevelLabel }}</p>
            </article>
            <article class="rounded-3xl border border-rose-100 bg-gradient-to-br from-rose-50 to-white p-4">
              <p class="text-xs font-bold uppercase tracking-[0.25em] text-rose-500">Más cercano</p>
              <p class="mt-3 text-2xl font-black text-slate-900">{{ nearestCenter?.nombre ?? 'Sin datos' }}</p>
              <p class="mt-1 text-sm text-slate-600">{{ nearestCenter ? `${nearestCenter.distance.toFixed(1)} km` : 'Cargando distancias' }}</p>
            </article>
          </div>

          <div class="mt-6 space-y-3">
            <p class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Nivel de complejidad</p>
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
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Latitud manual</span>
              <input
                v-model="manualLatitude"
                type="number"
                step="0.000001"
                class="w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none transition focus:border-teal-500 focus:ring-4 focus:ring-teal-100"
              />
            </label>
            <label class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-[0.25em] text-slate-500">Longitud manual</span>
              <input
                v-model="manualLongitude"
                type="number"
                step="0.000001"
                class="w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none transition focus:border-teal-500 focus:ring-4 focus:ring-teal-100"
              />
            </label>
          </div>

          <div class="mt-6 flex flex-wrap gap-3">
            <button
              type="button"
              class="rounded-full bg-gradient-to-r from-[#0F766E] to-[#14B8A6] px-5 py-3 text-sm font-bold text-white shadow-lg shadow-teal-200 transition hover:-translate-y-0.5"
              @click="requestCurrentLocation"
            >
              Detectar mi ubicación
            </button>
            <button
              type="button"
              class="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 transition hover:border-teal-200 hover:text-teal-700"
              @click="applyManualPosition"
            >
              Usar coordenadas manuales
            </button>
          </div>

          <p class="mt-4 text-sm text-slate-500">{{ statusMessage }}</p>
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
                <p class="text-xs text-slate-500">desde tu posición</p>
              </div>
            </div>

            <div class="mt-4 flex flex-wrap gap-2 text-xs font-semibold text-slate-600">
              <span class="rounded-full bg-slate-100 px-3 py-1">{{ center.horario || 'Horario no cargado' }}</span>
              <span class="rounded-full bg-slate-100 px-3 py-1">{{ center.telefono }}</span>
              <span class="rounded-full bg-slate-100 px-3 py-1">
                {{ center.ambulancia_disponible ? 'Ambulancia disponible' : 'Sin ambulancia' }}
              </span>
            </div>
          </article>
        </div>
      </div>

      <aside class="space-y-6 lg:sticky lg:top-28 lg:self-start">
        <div class="overflow-hidden rounded-[2rem] border border-teal-100 bg-slate-950 p-4 text-white shadow-[0_35px_90px_-40px_rgba(15,23,42,0.95)]">
          <div class="rounded-[1.5rem] border border-white/10 bg-[radial-gradient(circle_at_top,_rgba(20,184,166,0.24),_transparent_32%),linear-gradient(180deg,rgba(15,118,110,0.92),rgba(15,23,42,0.96))] p-5">
            <div class="flex items-center justify-between gap-3">
              <div>
                <p class="text-xs font-bold uppercase tracking-[0.35em] text-teal-200">Mapa interactivo</p>
                <h2 class="mt-2 text-2xl font-black">Referencia visual de centros</h2>
              </div>
              <div class="rounded-2xl bg-white/10 px-3 py-2 text-xs font-semibold text-teal-100">
                {{ activeLevelLabel }}
              </div>
            </div>

            <div class="relative mt-6 h-[460px] overflow-hidden rounded-[1.6rem] border border-white/10 bg-[linear-gradient(transparent_1px,rgba(255,255,255,0.05)_1px),linear-gradient(90deg,transparent_1px,rgba(255,255,255,0.05)_1px)] bg-[size:40px_40px]">
              <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_45%,rgba(20,184,166,0.2),transparent_42%)]"></div>
              <button
                class="absolute z-20 flex h-16 w-16 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border-4 border-white bg-[#F97316] text-white shadow-[0_0_0_18px_rgba(249,115,22,0.2)] transition hover:scale-105"
                :style="markerStyle(currentPosition.latitude, currentPosition.longitude)"
                type="button"
              >
                <i class="pi pi-user text-xl"></i>
              </button>
              <button
                v-for="center in mapCenters"
                :key="center.id"
                type="button"
                class="absolute z-20 flex -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border border-white/80 text-xs font-bold text-white shadow-lg transition hover:scale-110"
                :class="activeCenter?.id === center.id ? 'h-16 w-16 bg-emerald-500 shadow-emerald-500/30' : 'h-12 w-12 bg-teal-500/90'"
                :style="markerStyle(center.latitude, center.longitude)"
                @click="activeCenter = center"
              >
                {{ center.nivel }}
              </button>
            </div>
          </div>
        </div>

        <div v-if="activeCenter" class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-lg">
          <p class="text-xs font-bold uppercase tracking-[0.3em] text-slate-500">Ficha rápida</p>
          <h3 class="mt-2 text-2xl font-black text-slate-900">{{ activeCenter.nombre }}</h3>
          <div class="mt-4 space-y-3 text-sm text-slate-600">
            <p><strong class="text-slate-800">Dirección:</strong> {{ activeCenter.direccion }}</p>
            <p><strong class="text-slate-800">Teléfono:</strong> {{ activeCenter.telefono }}</p>
            <p><strong class="text-slate-800">Emergencia:</strong> {{ activeCenter.telefono_emergencia || 'No registrado' }}</p>
            <p><strong class="text-slate-800">Ambulancia:</strong> {{ activeCenter.ambulancia_disponible ? 'Disponible' : 'No disponible' }}</p>
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
import { computed, onMounted, ref } from 'vue';
import Footer from '@/components/landing/Footer/Footer.vue';
import PageHero from '@/components/common/PageHero.vue';
import { apiUrl } from '@/utils/api';
import {
  calculateDistanceKm,
  type GeoPoint,
  type HealthCenter,
  type PublicSectorLevel,
  type PublicSectorLevelFilter,
  toNumber,
} from './public-sector';

const demoCenters: HealthCenter[] = [
  {
    id: 1001,
    nombre: 'Centro de Salud San Martín',
    nivel: 'I',
    direccion: 'Av. Principal 123',
    ciudad: 'Cochabamba',
    telefono: '+591 4 444 1111',
    telefono_emergencia: '+591 4 444 1112',
    horario: 'Lun a sáb 08:00 - 20:00',
    ambulancia_disponible: true,
    latitude: '-17.3813',
    longitude: '-66.1568',
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  },
  {
    id: 1002,
    nombre: 'Hospital Materno Regional',
    nivel: 'II',
    direccion: 'Calle Salud y Vida 240',
    ciudad: 'La Paz',
    telefono: '+591 2 222 4200',
    telefono_emergencia: '+591 2 222 4201',
    horario: '24 horas',
    ambulancia_disponible: true,
    latitude: '-16.4897',
    longitude: '-68.1193',
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  },
  {
    id: 1003,
    nombre: 'Red Integrada Sur',
    nivel: 'III',
    direccion: 'Zona Sur, Manzano 4',
    ciudad: 'Santa Cruz',
    telefono: '+591 3 333 9080',
    telefono_emergencia: '+591 3 333 9081',
    horario: '24 horas',
    ambulancia_disponible: true,
    latitude: '-17.7833',
    longitude: '-63.1821',
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  },
];

const centers = ref<HealthCenter[]>([]);
const loading = ref(true);
const errorMessage = ref('');
const activeLevel = ref<PublicSectorLevelFilter>('all');
const activeCenter = ref<(HealthCenter & { distance: number }) | null>(null);
const currentPosition = ref<GeoPoint>({ latitude: -16.5, longitude: -68.15 });
const manualLatitude = ref('-16.500000');
const manualLongitude = ref('-68.150000');
const statusMessage = ref('Preparando geolocalización y consulta de centros...');

const levelFilters: Array<{ key: PublicSectorLevelFilter; label: string }> = [
  { key: 'all', label: 'Todos' },
  { key: 'I', label: 'Nivel I' },
  { key: 'II', label: 'Nivel II' },
  { key: 'III', label: 'Nivel III' },
];

const activeLevelLabel = computed(() => levelFilters.find((item) => item.key === activeLevel.value)?.label ?? 'Todos');

const currentPositionLabel = computed(() => `${currentPosition.value.latitude.toFixed(4)}, ${currentPosition.value.longitude.toFixed(4)}`);

const visibleCenters = computed(() => {
  const filtered = activeLevel.value === 'all' ? centers.value : centers.value.filter((center) => center.nivel === activeLevel.value);

  return filtered
    .map((center) => ({
      ...center,
      distance: calculateDistanceKm(currentPosition.value, {
        latitude: toNumber(center.latitude),
        longitude: toNumber(center.longitude),
      }),
    }))
    .sort((a, b) => a.distance - b.distance);
});

const sortedCenters = computed(() => visibleCenters.value);
const mapCenters = computed(() => visibleCenters.value.slice(0, 12));
const nearestCenter = computed(() => sortedCenters.value[0] ?? null);

const mapBounds = computed(() => {
  const points = [...mapCenters.value, { latitude: currentPosition.value.latitude, longitude: currentPosition.value.longitude }].map(
    (point) => ({ latitude: toNumber(point.latitude), longitude: toNumber(point.longitude) })
  );

  const latitudes = points.map((point) => point.latitude);
  const longitudes = points.map((point) => point.longitude);

  const minLatitude = Math.min(...latitudes) - 0.25;
  const maxLatitude = Math.max(...latitudes) + 0.25;
  const minLongitude = Math.min(...longitudes) - 0.25;
  const maxLongitude = Math.max(...longitudes) + 0.25;

  return { minLatitude, maxLatitude, minLongitude, maxLongitude };
});

function markerStyle(latitude: number | string, longitude: number | string): Record<string, string> {
  const lat = toNumber(latitude);
  const lng = toNumber(longitude);
  const widthPercent = 92;
  const heightPercent = 86;
  const normalizedX = (lng - mapBounds.value.minLongitude) / (mapBounds.value.maxLongitude - mapBounds.value.minLongitude || 1);
  const normalizedY = (lat - mapBounds.value.minLatitude) / (mapBounds.value.maxLatitude - mapBounds.value.minLatitude || 1);

  return {
    left: `${Math.min(96, Math.max(4, normalizedX * widthPercent + 4))}%`,
    top: `${Math.min(96, Math.max(4, heightPercent - normalizedY * heightPercent + 4))}%`,
  };
}

function levelBadgeClass(level: PublicSectorLevel): string {
  if (level === 'I') {
    return 'bg-emerald-50 text-emerald-700';
  }
  if (level === 'II') {
    return 'bg-teal-50 text-teal-700';
  }
  return 'bg-orange-50 text-[#EA580C]';
}

async function loadCenters(): Promise<void> {
  try {
    const response = await fetch(apiUrl('/health-centers/'));
    if (!response.ok) {
      throw new Error('No fue posible cargar los centros desde la API.');
    }

    const data = (await response.json()) as HealthCenter[];
    centers.value = data.length > 0 ? data : demoCenters;
    statusMessage.value = data.length > 0 ? 'Centros sincronizados desde PostgreSQL.' : 'Usando centros de demostración hasta que la tabla tenga registros.';
  } catch (error) {
    centers.value = demoCenters;
    statusMessage.value = 'No se pudo leer la API. Se activó un mapa de demostración para mantener la vista funcional.';
    errorMessage.value = error instanceof Error ? error.message : 'Error inesperado al cargar centros.';
  } finally {
    loading.value = false;
    activeCenter.value = visibleCenters.value[0] ?? null;
  }
}

function applyManualPosition(): void {
  const latitude = Number.parseFloat(manualLatitude.value);
  const longitude = Number.parseFloat(manualLongitude.value);

  if (Number.isNaN(latitude) || Number.isNaN(longitude)) {
    statusMessage.value = 'Ingresa coordenadas válidas para actualizar la posición.';
    return;
  }

  currentPosition.value = { latitude, longitude };
  statusMessage.value = 'Posición actualizada manualmente.';
}

function requestCurrentLocation(): void {
  if (!navigator.geolocation) {
    statusMessage.value = 'Tu navegador no permite geolocalización. Usa las coordenadas manuales.';
    return;
  }

  navigator.geolocation.getCurrentPosition(
    (position) => {
      currentPosition.value = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude,
      };
      manualLatitude.value = position.coords.latitude.toFixed(6);
      manualLongitude.value = position.coords.longitude.toFixed(6);
      statusMessage.value = 'Ubicación obtenida desde el navegador.';
    },
    () => {
      statusMessage.value = 'No se pudo obtener GPS. Usa la posición manual como respaldo.';
    },
    { enableHighAccuracy: true, timeout: 12000, maximumAge: 120000 }
  );
}

onMounted(async () => {
  document.title = 'Geolocalizador de centros | Mesa de Maternidad';
  await loadCenters();
  requestCurrentLocation();
});
</script>
