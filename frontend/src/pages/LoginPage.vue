<template>
  <div class="min-h-screen overflow-hidden bg-gradient-to-br from-orange-50 via-white to-pink-50">
    <!-- Parallax Background -->
    <div class="fixed inset-0 overflow-hidden">
      <!-- Blob 1 -->
      <div
        class="absolute -top-40 -left-40 h-80 w-80 rounded-full bg-gradient-to-br from-[#F97316]/20 to-[#991a73]/10 blur-3xl"
        :style="{ transform: `translateY(${parallaxOffset * 0.5}px)` }"
      ></div>
      <!-- Blob 2 -->
      <div
        class="absolute -bottom-40 -right-40 h-96 w-96 rounded-full bg-gradient-to-br from-[#991a73]/20 to-[#F97316]/10 blur-3xl"
        :style="{ transform: `translateY(${-parallaxOffset * 0.3}px)` }"
      ></div>
      <!-- Blob 3 -->
      <div
        class="absolute top-1/2 left-1/2 h-64 w-64 rounded-full bg-gradient-to-br from-pink-200/10 to-orange-200/5 blur-3xl"
        :style="{ transform: `translate(calc(-50% + ${parallaxOffset * 0.2}px), -50%)` }"
      ></div>
    </div>

    <!-- Content -->
    <div class="relative z-10 flex min-h-screen items-center justify-center px-4">
      <div class="w-full max-w-md">
        <!-- Logo & Welcome -->
        <div class="mb-8 text-center">
          <div class="mb-4 flex items-center justify-center gap-3">
            <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-white p-2 shadow-lg ring-2 ring-[#F97316]/20">
              <img src="/img/logo1.jpg" alt="MNMNS Bolivia" class="h-full w-full object-contain" />
            </div>
          </div>
          <h1 class="mb-2 text-3xl font-bold bg-gradient-to-r from-[#F97316] to-[#991a73] bg-clip-text text-transparent">
            Bienvenida
          </h1>
          <p class="text-gray-600">Accede a tu panel de gestión</p>
        </div>

        <!-- Form Card -->
        <div class="backdrop-blur-xl rounded-3xl border border-white/40 bg-white/95 p-8 shadow-2xl text-gray-900">
          <!-- Tabs -->
          <div class="mb-8 flex gap-2 rounded-full bg-gray-100 p-1">
            <button
              @click="activeTab = 'login'"
              :class="[
                'flex-1 rounded-full py-2 px-4 font-semibold transition-all duration-300',
                activeTab === 'login'
                  ? 'bg-gradient-to-r from-[#F97316] to-[#991a73] text-white shadow-lg'
                  : 'text-gray-600 hover:text-gray-900'
              ]"
            >
              Login
            </button>
            <button
              @click="activeTab = 'register'"
              :class="[
                'flex-1 rounded-full py-2 px-4 font-semibold transition-all duration-300',
                activeTab === 'register'
                  ? 'bg-gradient-to-r from-[#F97316] to-[#991a73] text-white shadow-lg'
                  : 'text-gray-600 hover:text-gray-900'
              ]"
            >
              Registro
            </button>
          </div>

          <!-- Login Form -->
          <form v-if="activeTab === 'login'" @submit.prevent="handleLogin" class="space-y-5">
            <div>
              <label class="mb-2 block text-sm font-semibold text-gray-700">Email</label>
              <input
                v-model="loginForm.email"
                type="email"
                placeholder="tu@email.com"
                class="w-full rounded-xl border border-black-200 bg-white px-4 py-3 text-sm font-semibold text-gray-900 placeholder-gray-500 transition-all focus:border-[#F97316] focus:outline-none focus:ring-2 focus:ring-[#F97316]/20"
                required
              />
            </div>

            <div>
              <label class="mb-2 block text-sm font-semibold text-gray-700">Contraseña</label>
              <input
                v-model="loginForm.password"
                type="password"
                placeholder="••••••••"
                class="w-full rounded-xl border border-black-200 bg-white px-4 py-3 text-sm font-semibold text-gray-900 placeholder-gray-500 transition-all focus:border-[#F97316] focus:outline-none focus:ring-2 focus:ring-[#F97316]/20"
                required
              />
            </div>

            <div class="flex items-center justify-between">
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="checkbox" class="rounded border-gray-300 text-[#F97316]" />
                <span class="text-sm text-gray-600">Recuérdame</span>
              </label>
              <a href="#" class="text-sm font-semibold text-[#F97316] hover:text-[#991a73] transition-colors">
                ¿Olvidaste tu contraseña?
              </a>
            </div>

            <button
              type="submit"
              :disabled="isLoading"
              class="w-full rounded-xl bg-gradient-to-r from-[#F97316] to-[#991a73] py-3 font-bold text-white shadow-lg transition-all hover:from-[#EA580C] hover:to-[#7d155f] disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {{ isLoading ? 'Iniciando sesión...' : 'Iniciar Sesión' }}
            </button>
          </form>

          <!-- Register Form -->
          <form v-else @submit.prevent="handleRegister" class="space-y-5">
            <div>
              <label class="mb-2 block text-sm font-semibold text-gray-700">Nombre Completo</label>
              <input
                v-model="registerForm.fullName"
                type="text"
                placeholder="Tu nombre"
                class="w-full rounded-xl border border-gray-200 bg-white px-4 py-3 text-sm font-semibold text-gray-900 placeholder-gray-500 transition-all focus:border-[#F97316] focus:outline-none focus:ring-2 focus:ring-[#F97316]/20"
                required
              />
            </div>

            <div>
              <label class="mb-2 block text-sm font-semibold text-gray-700">Email</label>
              <input
                v-model="registerForm.email"
                type="email"
                placeholder="tu@email.com"
                class="w-full rounded-xl border border-gray-200 bg-white px-4 py-3 text-sm font-semibold text-gray-900 placeholder-gray-500 transition-all focus:border-[#F97316] focus:outline-none focus:ring-2 focus:ring-[#F97316]/20"
                required
              />
            </div>

            <div>
              <label class="mb-2 block text-sm font-semibold text-gray-700">Contraseña</label>
              <input
                v-model="registerForm.password"
                type="password"
                placeholder="••••••••"
                class="w-full rounded-xl border border-gray-200 bg-white px-4 py-3 text-sm font-semibold text-gray-900 placeholder-gray-500 transition-all focus:border-[#F97316] focus:outline-none focus:ring-2 focus:ring-[#F97316]/20"
                required
              />
            </div>

            <div>
              <label class="mb-2 block text-sm font-semibold text-gray-700">Confirmar Contraseña</label>
              <input
                v-model="registerForm.confirmPassword"
                type="password"
                placeholder="••••••••"
                class="w-full rounded-xl border border-gray-200 bg-white px-4 py-3 text-sm font-semibold text-gray-900 placeholder-gray-500 transition-all focus:border-[#F97316] focus:outline-none focus:ring-2 focus:ring-[#F97316]/20"
                required
              />
            </div>

            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" required class="rounded border-gray-300 text-[#F97316]" />
              <span class="text-sm text-gray-600">
                Acepto los
                <a href="#" class="font-semibold text-[#F97316] hover:text-[#991a73] transition-colors">
                  términos y condiciones
                </a>
              </span>
            </label>

            <button
              type="submit"
              :disabled="isLoading"
              class="w-full rounded-xl bg-gradient-to-r from-[#F97316] to-[#991a73] py-3 font-bold text-white shadow-lg transition-all hover:from-[#EA580C] hover:to-[#7d155f] disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {{ isLoading ? 'Creando cuenta...' : 'Crear Cuenta' }}
            </button>
          </form>

          <!-- Divider -->
          <div class="my-6 flex items-center gap-3">
            <div class="h-px flex-1 bg-gray-200"></div>
            <span class="text-sm text-gray-500">o continúa con</span>
            <div class="h-px flex-1 bg-gray-200"></div>
          </div>

          <!-- Social Login -->
          <div class="flex gap-3">
            <button
              class="flex-1 rounded-xl border-2 border-gray-200 py-3 font-semibold text-gray-700 transition-all hover:border-[#F97316] hover:bg-orange-50"
            >
              <i class="pi pi-google text-lg"></i>
            </button>
            <button
              class="flex-1 rounded-xl border-2 border-gray-200 py-3 font-semibold text-gray-700 transition-all hover:border-[#F97316] hover:bg-orange-50"
            >
              <i class="pi pi-github text-lg"></i>
            </button>
          </div>
        </div>

        <!-- Back Link -->
        <div class="mt-6 text-center">
          <router-link
            to="/"
            class="inline-flex items-center gap-2 text-sm font-semibold text-[#F97316] transition-colors hover:text-[#991a73]"
          >
            <i class="pi pi-arrow-left text-xs"></i>
            Volver al inicio
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useToast } from 'primevue/usetoast';
import { useAuth } from '@/composables/useAuth';

const router = useRouter();
const toast = useToast();
const { login, register, isLoading } = useAuth();

const activeTab = ref<'login' | 'register'>('login');
const parallaxOffset = ref(0);

const loginForm = ref({
  email: '',
  password: ''
});

const registerForm = ref({
  fullName: '',
  email: '',
  password: '',
  confirmPassword: ''
});

// Parallax effect
const handleMouseMove = (e: MouseEvent) => {
  const scrollY = window.scrollY || document.documentElement.scrollTop;
  parallaxOffset.value = scrollY;
};

window.addEventListener('scroll', handleMouseMove);

const handleLogin = async () => {
  if (!loginForm.value.email || !loginForm.value.password) {
    toast.add({
      severity: 'warn',
      summary: 'Campos vacíos',
      detail: 'Por favor completa todos los campos',
      life: 3000
    });
    return;
  }

  const success = await login(loginForm.value.email, loginForm.value.password);
  
  if (success) {
    toast.add({
      severity: 'success',
      summary: 'Éxito',
      detail: 'Sesión iniciada correctamente',
      life: 2000
    });
    setTimeout(() => {
      router.push('/dashboard');
    }, 500);
  } else {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'No pudimos iniciar sesión. Verifica tus credenciales',
      life: 3000
    });
  }
};

const handleRegister = async () => {
  if (registerForm.value.password !== registerForm.value.confirmPassword) {
    toast.add({
      severity: 'warn',
      summary: 'Contraseñas no coinciden',
      detail: 'Las contraseñas deben ser iguales',
      life: 3000
    });
    return;
  }

  if (registerForm.value.password.length < 8) {
    toast.add({
      severity: 'warn',
      summary: 'Contraseña débil',
      detail: 'La contraseña debe tener al menos 8 caracteres',
      life: 3000
    });
    return;
  }

  const success = await register(
    registerForm.value.email,
    registerForm.value.password,
    registerForm.value.fullName
  );

  if (success) {
    toast.add({
      severity: 'success',
      summary: 'Éxito',
      detail: 'Cuenta creada correctamente. Ahora inicia sesión',
      life: 2000
    });
    activeTab.value = 'login';
    registerForm.value = {
      fullName: '',
      email: '',
      password: '',
      confirmPassword: ''
    };
  } else {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'No pudimos crear tu cuenta',
      life: 3000
    });
  }
};
</script>

<style scoped>
/* Smooth transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
