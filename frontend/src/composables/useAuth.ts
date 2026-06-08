import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

interface User {
  id: string;
  email: string;
  fullName: string;
  role: 'admin' | 'user' | 'moderator';
}

const user = ref<User | null>(null);
const token = ref<string | null>(null);
const isLoading = ref(false);
const error = ref<string | null>(null);

export const useAuth = () => {
  const router = useRouter();

  // Cargar token del localStorage al iniciar
  const initAuth = () => {
    const savedToken = localStorage.getItem('token');
    if (savedToken) {
      token.value = savedToken;
      // TODO: Verificar si el token sigue siendo válido
      loadUserProfile();
    }
  };

  // Verificar si está autenticado
  const isAuthenticated = computed(() => !!token.value && !!user.value);

  // Login
  const login = async (email: string, password: string) => {
    isLoading.value = true;
    error.value = null;
    try {
      const response = await fetch('http://localhost:8000/api/auth/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Credenciales inválidas');
      }

      const data = await response.json();
      token.value = data.token;
      
      // Guardar token y cargar perfil del usuario
      localStorage.setItem('token', data.token);
      await loadUserProfile();
      
      return true;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Error en el login';
      return false;
    } finally {
      isLoading.value = false;
    }
  };

  // Registro
  const register = async (email: string, password: string, fullName: string) => {
    isLoading.value = true;
    error.value = null;
    try {
      const response = await fetch('http://localhost:8000/api/auth/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          email, 
          password, 
          first_name: fullName.split(' ')[0],
          last_name: fullName.split(' ').slice(1).join(' ')
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        const errorMessage = Object.values(errorData).flat().join(', ');
        throw new Error(errorMessage || 'Error al crear la cuenta');
      }

      const data = await response.json();
      token.value = data.token;
      localStorage.setItem('token', data.token);
      
      // Cargar perfil del usuario después del registro
      await loadUserProfile();
      
      return true;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Error en el registro';
      return false;
    } finally {
      isLoading.value = false;
    }
  };

  // Logout
  const logout = () => {
    token.value = null;
    user.value = null;
    error.value = null;
    localStorage.removeItem('token');
    router.push('/');
  };

  // Cargar perfil del usuario
  const loadUserProfile = async () => {
    if (!token.value) return;

    try {
      const response = await fetch('http://localhost:8000/api/auth/me/', {
        headers: {
          'Authorization': `Token ${token.value}`,
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        const data = await response.json();
        user.value = {
          id: data.id,
          email: data.email,
          fullName: `${data.first_name} ${data.last_name}`.trim(),
          role: data.role
        };
      } else {
        logout();
      }
    } catch (err) {
      console.error('Error loading user profile:', err);
      logout();
    }
  };

  // Verificar si tiene un rol específico
  const hasRole = (role: string | string[]) => {
    if (!user.value) return false;
    if (typeof role === 'string') {
      return user.value.role === role;
    }
    return role.includes(user.value.role);
  };

  return {
    user,
    token,
    isLoading,
    error,
    isAuthenticated,
    initAuth,
    login,
    register,
    logout,
    loadUserProfile,
    hasRole
  };
};
