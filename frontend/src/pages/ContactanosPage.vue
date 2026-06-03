<template>
  <div class="pt-20 bg-[#f8fafc] min-h-screen flex flex-col">
    
    <PageHero
      kicker="Contacto"
      title="Estamos para Escucharte"
      subtitle="¿Tienes dudas, sugerencias o quieres formar parte de nuestra red de aliados? Escríbenos y nos pondremos en contacto contigo a la brevedad."
      backgroundImage="/img/fondo14.avif"
    />

    <section class="py-16 flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
        
        <div class="space-y-10 animate-fade-in-left">
          <div>
            <h2 class="text-2xl font-bold text-gray-900 mb-6">Información Oficial</h2>
            <div class="space-y-6">
              <div class="flex items-start gap-4">
                <div class="w-12 h-12 bg-orange-50 text-[#F97316] rounded-2xl flex items-center justify-center flex-shrink-0 shadow-sm">
                  <i class="pi pi-map-marker text-xl"></i>
                </div>
                <div>
                  <h4 class="font-bold text-gray-900">Oficina Central</h4>
                  <p class="text-gray-600 text-sm">Calle 20 de Octubre #123.<br>La Paz, Bolivia.</p>
                </div>
              </div>

              <div class="flex items-start gap-4">
                <div class="w-12 h-12 bg-green-50 text-[#00833D] rounded-2xl flex items-center justify-center flex-shrink-0 shadow-sm">
                  <i class="pi pi-phone text-xl"></i>
                </div>
                <div>
                  <h4 class="font-bold text-gray-900">Teléfonos de Atención</h4>
                  <p class="text-gray-600 text-sm">+591 (2) 2123456 - Interno 402<br>Lunes a Viernes (08:30 - 16:30)</p>
                </div>
              </div>

              <div class="flex items-start gap-4">
                <div class="w-12 h-12 bg-orange-50 text-orange-600 rounded-2xl flex items-center justify-center flex-shrink-0 shadow-sm">
                  <i class="pi pi-envelope text-xl"></i>
                </div>
                <div>
                  <h4 class="font-bold text-gray-900">Correo Electrónico</h4>
                  <p class="text-gray-600 text-sm">contacto@mnmns.org.bo<br>bolivia@mnmns.org.bo</p>
                </div>
              </div>
            </div>
          </div>

          <div>
            <h2 class="text-2xl font-bold text-gray-900 mb-6">Síguenos en Redes</h2>
            <div class="flex flex-wrap gap-4">
              <a href="#" class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-[#F97316] shadow-sm border border-gray-100 hover:bg-[#F97316] hover:text-white transition-all duration-300 transform hover:-translate-y-2 group">
                <i class="pi pi-facebook text-2xl"></i>
              </a>
              <a href="#" class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-[#F97316] shadow-sm border border-gray-100 hover:bg-[#F97316] hover:text-white transition-all duration-300 transform hover:-translate-y-2 group">
                <i class="pi pi-twitter text-2xl"></i>
              </a>
              <a href="#" class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-[#F97316] shadow-sm border border-gray-100 hover:bg-[#F97316] hover:text-white transition-all duration-300 transform hover:-translate-y-2 group">
                <i class="pi pi-instagram text-2xl"></i>
              </a>
              <a href="#" class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-[#F97316] shadow-sm border border-gray-100 hover:bg-[#F97316] hover:text-white transition-all duration-300 transform hover:-translate-y-2 group">
                <i class="pi pi-youtube text-2xl"></i>
              </a>
              <a href="#" class="w-14 h-14 bg-[#25D366] rounded-2xl flex items-center justify-center text-white shadow-md hover:scale-110 transition-transform duration-300">
                <i class="pi pi-whatsapp text-2xl font-bold"></i>
              </a>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-3xl p-8 md:p-10 shadow-xl border border-gray-100 animate-fade-in-right">
          <h2 class="text-2xl font-bold text-gray-900 mb-2">Envíanos un Mensaje</h2>
          <p class="text-gray-500 mb-8">Completa los datos y cuéntanos cómo podemos ayudarte.</p>

          <form @submit.prevent="enviarMensaje" class="space-y-5">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
              <div class="space-y-2">
                <label class="text-sm font-bold text-gray-700 ml-1">Nombre Completo</label>
                <input v-model="formData.nombre" type="text" placeholder="Tu nombre..." required
                       class="contact-field w-full px-5 py-4 bg-gray-50 border border-gray-200 rounded-2xl text-gray-900 placeholder:text-gray-400 caret-gray-900 focus:ring-4 focus:ring-[#F97316]/10 focus:border-[#F97316] outline-none transition-all">
              </div>
              <div class="space-y-2">
                <label class="text-sm font-bold text-gray-700 ml-1">Correo Electrónico</label>
                <input v-model="formData.email" type="email" placeholder="ejemplo@correo.com" required
                       class="contact-field w-full px-5 py-4 bg-gray-50 border border-gray-200 rounded-2xl text-gray-900 placeholder:text-gray-400 caret-gray-900 focus:ring-4 focus:ring-[#F97316]/10 focus:border-[#F97316] outline-none transition-all">
              </div>
            </div>

            <div class="space-y-2">
              <label class="text-sm font-bold text-gray-700 ml-1">Asunto</label>
              <select v-model="formData.asunto" class="contact-field w-full px-5 py-4 bg-gray-50 border border-gray-200 rounded-2xl text-gray-900 caret-gray-900 focus:ring-4 focus:ring-[#F97316]/10 focus:border-[#F97316] outline-none transition-all appearance-none cursor-pointer">
                <option value="General">Consulta General</option>
                <option value="Aliado">Quiero ser Institución Aliada</option>
                <option value="Prensa">Contacto de Prensa</option>
                <option value="Denuncia">Reporte / Sugerencia</option>
              </select>
            </div>

            <div class="space-y-2">
              <label class="text-sm font-bold text-gray-700 ml-1">Mensaje</label>
              <textarea v-model="formData.mensaje" rows="5" placeholder="Escribe tu mensaje aquí..." required
                        class="contact-field w-full px-5 py-4 bg-gray-50 border border-gray-200 rounded-2xl text-gray-900 placeholder:text-gray-400 caret-gray-900 focus:ring-4 focus:ring-[#F97316]/10 focus:border-[#F97316] outline-none transition-all resize-none"></textarea>
            </div>

            <button type="submit" :disabled="loading"
                    class="w-full py-4 bg-[#F97316] text-white font-bold rounded-2xl shadow-lg hover:shadow-[#F97316]/30 hover:bg-[#EA580C] transition-all flex justify-center items-center gap-3 disabled:opacity-70 group overflow-hidden relative">
              <span v-if="!loading" class="flex items-center gap-2">
                Enviar Mensaje <i class="pi pi-send group-hover:translate-x-2 transition-transform"></i>
              </span>
              <i v-else class="pi pi-spinner animate-spin text-xl"></i>
            </button>
          </form>

          <div v-if="errorMensaje" class="mt-6 p-4 bg-red-50 border border-red-100 rounded-2xl text-red-700 flex items-center gap-3">
            <i class="pi pi-exclamation-circle text-xl"></i>
            <span class="font-semibold">{{ errorMensaje }}</span>
          </div>

          <div v-if="enviado" class="mt-6 p-4 bg-green-50 border border-green-100 rounded-2xl text-green-700 flex items-center gap-3 animate-bounce">
            <i class="pi pi-check-circle text-xl"></i>
            <span class="font-bold">¡Mensaje enviado con éxito! Te responderemos pronto.</span>
          </div>
        </div>
      </div>
    </section>

    <div class="h-48 bg-gray-200 w-full relative overflow-hidden flex items-center justify-center grayscale opacity-50">
       <span class="text-gray-400 font-bold uppercase tracking-widest text-lg">Mapa de Ubicación Interactivo</span>
      <div class="absolute inset-0 bg-orange-900/5"></div>
    </div>

    <Footer class="mt-auto" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '../components/landing/Footer/Footer.vue';
import { apiUrl } from '@/utils/api';

const loading = ref(false);
const enviado = ref(false);
const errorMensaje = ref('');

const formData = ref({
  nombre: '',
  email: '',
  asunto: 'General',
  mensaje: ''
});

const enviarMensaje = async () => {
  loading.value = true;
  errorMensaje.value = '';

  try {
    const response = await fetch(apiUrl('/contact-messages/'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData.value)
    });

    if (!response.ok) {
      throw new Error('No se pudo enviar el mensaje. Verifica tus datos e intenta otra vez.');
    }

    loading.value = false;
    enviado.value = true;

    formData.value = {
      nombre: '',
      email: '',
      asunto: 'General',
      mensaje: ''
    };

    setTimeout(() => { enviado.value = false; }, 5000);
  } catch (error) {
    errorMensaje.value = error instanceof Error ? error.message : 'Error inesperado al enviar el mensaje.';
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  document.title = 'Contáctanos | Mesa de Maternidad Bolivia';
  window.scrollTo(0, 0);
});
</script>

<style scoped>
@keyframes fadeInLeft {
  from { opacity: 0; transform: translateX(-40px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes fadeInRight {
  from { opacity: 0; transform: translateX(40px); }
  to { opacity: 1; transform: translateX(0); }
}

.animate-fade-in-left {
  animation: fadeInLeft 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.animate-fade-in-right {
  animation: fadeInRight 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.contact-field {
  color: #111827;
}

.contact-field::placeholder {
  color: #9ca3af;
}

.contact-field option {
  color: #111827;
  background-color: #ffffff;
}
</style>