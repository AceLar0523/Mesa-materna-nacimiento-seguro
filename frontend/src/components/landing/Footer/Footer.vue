<template>
  <footer class="bg-white border-t border-gray-200 pt-16 pb-8 mt-auto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-12">
        
        <div class="lg:col-span-1">
          <router-link to="/" class="flex items-center gap-3 mb-4 group">
            <div class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-2xl bg-white p-1.5 shadow-sm ring-1 ring-gray-100 group-hover:scale-110 transition-transform">
              <img src="/img/logo1.jpg" alt="MNMNS Bolivia" class="h-full w-full object-contain" />
            </div>
            <div class="flex flex-col">
              <span class="font-bold text-[#F97316] text-lg leading-tight">MNMNS Bolivia</span>
              <span class="text-xs text-gray-500 font-medium">Mesa Nacional de Maternidad y Nacimiento Seguros</span>
            </div>
          </router-link>
          <p class="text-gray-500 text-sm leading-relaxed mb-6">
            Trabajamos de manera articulada para garantizar que cada embarazo y nacimiento en Bolivia sea una experiencia segura, respetada y llena de vida.
          </p>
          
          <div class="flex gap-3">
            <a href="#" aria-label="Facebook" class="w-9 h-9 rounded-full bg-orange-50 text-[#F97316] flex items-center justify-center hover:bg-[#991a73] hover:text-white hover:-translate-y-1 transition-all">
              <i class="pi pi-facebook"></i>
            </a>
            <a href="#" aria-label="Twitter" class="w-9 h-9 rounded-full bg-orange-50 text-[#F97316] flex items-center justify-center hover:bg-[#991a73] hover:text-white hover:-translate-y-1 transition-all">
              <i class="pi pi-twitter"></i>
            </a>
            <a href="#" aria-label="Instagram" class="w-9 h-9 rounded-full bg-orange-50 text-[#F97316] flex items-center justify-center hover:bg-[#991a73] hover:text-white hover:-translate-y-1 transition-all">
              <i class="pi pi-instagram"></i>
            </a>
            <a href="#" aria-label="YouTube" class="w-9 h-9 rounded-full bg-orange-50 text-[#F97316] flex items-center justify-center hover:bg-[#991a73] hover:text-white hover:-translate-y-1 transition-all">
              <i class="pi pi-youtube"></i>
            </a>
          </div>
        </div>

        <div>
          <h3 class="font-bold text-gray-900 mb-5 uppercase tracking-wider text-sm">Navegación</h3>
          <ul class="space-y-3">
            <li><router-link to="/" class="text-gray-500 hover:text-[#F97316] transition-colors text-sm flex items-center gap-2"><i class="pi pi-angle-right text-xs"></i> Inicio</router-link></li>
            <li><router-link to="/conocenos" class="text-gray-500 hover:text-[#F97316] transition-colors text-sm flex items-center gap-2"><i class="pi pi-angle-right text-xs"></i> Conócenos</router-link></li>
            <li><router-link to="/datos" class="text-gray-500 hover:text-[#F97316] transition-colors text-sm flex items-center gap-2"><i class="pi pi-angle-right text-xs"></i> Datos e Impacto</router-link></li>
            <li><router-link to="/instituciones" class="text-gray-500 hover:text-[#F97316] transition-colors text-sm flex items-center gap-2"><i class="pi pi-angle-right text-xs"></i> Instituciones Aliadas</router-link></li>
          </ul>
        </div>

        <div>
          <h3 class="font-bold text-gray-900 mb-5 uppercase tracking-wider text-sm">Comunidad</h3>
          <ul class="space-y-3">
            <li><router-link to="/blog" class="text-gray-500 hover:text-[#F97316] transition-colors text-sm flex items-center gap-2"><i class="pi pi-angle-right text-xs"></i> Blog y Testimonios</router-link></li>
            <li><router-link to="/noticias" class="text-gray-500 hover:text-[#F97316] transition-colors text-sm flex items-center gap-2"><i class="pi pi-angle-right text-xs"></i> Últimas Noticias</router-link></li>
            <li><router-link to="/contactanos" class="text-gray-500 hover:text-[#F97316] transition-colors text-sm flex items-center gap-2"><i class="pi pi-angle-right text-xs"></i> Contáctanos</router-link></li>
            <li><a href="#" class="text-gray-500 hover:text-[#F97316] transition-colors text-sm flex items-center gap-2"><i class="pi pi-angle-right text-xs"></i> Portal de Transparencia</a></li>
          </ul>
        </div>

        <div>
          <h3 class="font-bold text-gray-900 mb-5 uppercase tracking-wider text-sm">Contacto Oficial</h3>
          <ul class="space-y-4">
            <li class="flex items-start gap-3 text-sm text-gray-500">
              <i class="pi pi-map-marker text-[#F97316] mt-1 flex-shrink-0"></i>
              <span>Calle 20 de Octubre #123.<br>La Paz, Bolivia.</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-gray-500">
              <i class="pi pi-phone text-[#F97316] flex-shrink-0"></i>
              <span>+591 (2) 2123456</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-gray-500">
              <i class="pi pi-envelope text-[#F97316] flex-shrink-0"></i>
              <span>contacto@mnmns.org.bo</span>
            </li>
          </ul>
        </div>

      </div>

      <div class="pt-8 border-t border-gray-100 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="text-sm text-gray-400 text-center md:text-left">
          &copy; {{ new Date().getFullYear() }} Mesa Nacional de Maternidad y Nacimiento Seguros Bolivia. <br class="md:hidden"> Todos los derechos reservados.
        </p>
        <div class="flex gap-6 text-sm font-medium text-gray-400">
          <a href="#" class="hover:text-[#991a73] transition-colors">Políticas de Privacidad</a>
          <a href="#" class="hover:text-[#991a73] transition-colors">Términos de Uso</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
// Footer actualizado usando clases utilitarias de TailwindCSS para sincronizar con el Navbar
</script>

<style scoped>
/* Hemos eliminado la necesidad del archivo Footer.css al migrar todo a Tailwind CSS */
</style>