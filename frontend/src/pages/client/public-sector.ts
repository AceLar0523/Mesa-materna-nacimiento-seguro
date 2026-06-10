export type PublicSectorLevel = 'I' | 'II' | 'III';
export type PublicSectorLevelFilter = PublicSectorLevel | 'all';

export interface HealthCenter {
  id: number;
  nombre: string;
  nivel: PublicSectorLevel;
  direccion: string;
  ciudad: string;
  telefono: string;
  telefono_emergencia: string;
  horario: string;
  ambulancia_disponible: boolean;
  latitude: number | string;
  longitude: number | string;
  created_at: string;
  updated_at: string;
}

export interface PanicAlert {
  id: number;
  session_token: string;
  symptom: string;
  latitude: number | string;
  longitude: number | string;
  status: 'open' | 'acknowledged' | 'closed';
  note: string;
  created_at: string;
  updated_at: string;
}

export interface AdolescentConsultation {
  id: number;
  session_token: string;
  topic: 'contracepcion' | 'prevencion' | 'ciclo' | 'otro';
  question: string;
  answer: string;
  status: 'pending' | 'answered' | 'closed';
  responder_name: string;
  created_at: string;
  answered_at: string | null;
}

export interface GeoPoint {
  latitude: number;
  longitude: number;
}

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export const PUBLIC_SECTOR_TOKEN_KEY = 'mesa-public-sector-token';

export const moduleCards = [
  {
    key: 'obstetrico',
    path: '/sector-publico/asistente-obstetrico',
    label: 'Asistente obstétrico',
    icon: 'pi-calendar',
    accent: 'from-[#F97316] to-[#FB7185]'
  },
  {
    key: 'geolocalizador',
    path: '/sector-publico/geolocalizador',
    label: 'Geolocalizador de centros',
    icon: 'pi-map-marker',
    accent: 'from-[#0F766E] to-[#14B8A6]'
  },
  {
    key: 'alarmas',
    path: '/sector-publico/alarma-panico',
    label: 'Señales de alarma',
    icon: 'pi-bell',
    accent: 'from-[#991B1B] to-[#F97316]'
  },
  {
    key: 'adolescente',
    path: '/sector-publico/salud-adolescente',
    label: 'Salud adolescente',
    icon: 'pi-comments',
    accent: 'from-[#7C3AED] to-[#F97316]'
  }
] as const;

export function ensureSessionToken(): string {
  if (typeof window === 'undefined') {
    return '';
  }

  const storedToken = window.localStorage.getItem(PUBLIC_SECTOR_TOKEN_KEY);
  if (storedToken && storedToken.length === 64) {
    return storedToken;
  }

  const bytes = new Uint8Array(32);
  window.crypto.getRandomValues(bytes);
  const token = Array.from(bytes, (byte) => byte.toString(16).padStart(2, '0')).join('');
  window.localStorage.setItem(PUBLIC_SECTOR_TOKEN_KEY, token);
  return token;
}

export function getStoredSessionToken(): string {
  if (typeof window === 'undefined') {
    return '';
  }

  return window.localStorage.getItem(PUBLIC_SECTOR_TOKEN_KEY) ?? '';
}

export function calculateDistanceKm(origin: GeoPoint, target: GeoPoint): number {
  const earthRadiusKm = 6371;
  const toRadians = (value: number): number => (value * Math.PI) / 180;
  const deltaLat = toRadians(target.latitude - origin.latitude);
  const deltaLng = toRadians(target.longitude - origin.longitude);
  const lat1 = toRadians(origin.latitude);
  const lat2 = toRadians(target.latitude);

  const a =
    Math.sin(deltaLat / 2) * Math.sin(deltaLat / 2) +
    Math.sin(deltaLng / 2) * Math.sin(deltaLng / 2) * Math.cos(lat1) * Math.cos(lat2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

  return earthRadiusKm * c;
}

export function formatLevel(level: PublicSectorLevel): string {
  return `Nivel ${level}`;
}

export function toNumber(value: number | string): number {
  return typeof value === 'number' ? value : Number.parseFloat(value);
}

export function toApiList<T>(payload: unknown): T[] {
  if (Array.isArray(payload)) {
    return payload as T[];
  }

  if (payload && typeof payload === 'object' && Array.isArray((payload as PaginatedResponse<T>).results)) {
    return (payload as PaginatedResponse<T>).results;
  }

  return [];
}
