const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL as string | undefined)?.trim() || 'http://127.0.0.1:8000/api';

function normalizePath(path: string): string {
  if (!path.startsWith('/')) {
    return `/${path}`;
  }
  return path;
}

export function apiUrl(path: string): string {
  return `${API_BASE_URL}${normalizePath(path)}`;
}

export { API_BASE_URL };
