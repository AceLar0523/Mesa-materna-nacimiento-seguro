<template>
  <div class="pt-20 bg-gray-50 min-h-screen flex flex-col">
    <PageHero
      kicker="Sala de Prensa"
      title="Últimas Noticias"
      subtitle="Mantente informado sobre los avances, entregas y logros de la Mesa Nacional de Maternidad y Nacimiento Seguros en Bolivia."
      backgroundImage="/img/fondo10.jpg"
    />

    <section class="py-12 flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
      
      <div class="mb-16 bg-white rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-shadow duration-300 grid grid-cols-1 lg:grid-cols-2 group cursor-pointer border border-gray-100">
          <div class="h-64 lg:h-full bg-orange-50 relative overflow-hidden flex items-center justify-center">
          <div class="absolute inset-0 bg-[#F97316]/10 group-hover:bg-[#F97316]/0 transition-colors duration-500"></div>
          <img
            src="/img/fondo13.png"
            alt="Portada de noticias destacadas"
            class="h-full w-full object-cover group-hover:scale-105 transition-transform duration-700"
          />
        </div>
        <div class="p-8 md:p-12 flex flex-col justify-center">
          <div class="flex items-center gap-4 mb-4">
            <span class="bg-[#F97316] text-white text-xs font-bold px-3 py-1 rounded-full uppercase">Destacado</span>
            <span class="text-gray-400 text-sm font-medium flex items-center gap-1">
              <i class="pi pi-calendar text-xs"></i> 15 de Octubre, 2025
            </span>
          </div>
          <h2 class="text-3xl font-bold text-gray-900 mb-4 group-hover:text-[#F97316] transition-colors">
            La MNMNS y el Ministerio de Salud fortalecen la Mesa Nacional para reducir la mortalidad neonatal
          </h2>
          <p class="text-gray-600 mb-6 leading-relaxed text-lg">
            En un encuentro estratégico en La Paz, autoridades gubernamentales, agencias internacionales y la sociedad civil trazaron la nueva hoja de ruta SAFCI para garantizar que los centros de salud de primer nivel cuenten con el equipamiento necesario para partos seguros.
          </p>
          <div class="mt-auto">
            <span class="text-[#F97316] font-bold group-hover:underline flex items-center gap-2">
              Leer artículo completo <i class="pi pi-arrow-right text-sm"></i>
            </span>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <article v-for="noticia in listaNoticias" :key="noticia.id" class="bg-white rounded-2xl overflow-hidden shadow-sm border border-gray-100 hover:shadow-lg transition-all duration-300 group flex flex-col">
          <div class="h-48 bg-gray-100 relative overflow-hidden flex items-center justify-center">
             <img
               :src="noticia.imagen"
               :alt="noticia.titulo"
               class="h-full w-full object-cover group-hover:scale-105 transition-transform duration-700"
             />
          </div>
          <div class="p-6 flex flex-col flex-1">
            <div class="flex justify-between items-center mb-3">
              <span class="text-[#F97316] text-xs font-bold uppercase tracking-wider">{{ noticia.categoria }}</span>
              <span class="text-gray-400 text-xs font-medium">{{ noticia.fecha }}</span>
            </div>
            <h3 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-[#F97316] transition-colors line-clamp-2">
              {{ noticia.titulo }}
            </h3>
            <p class="text-gray-600 text-sm mb-6 line-clamp-3 flex-1">
              {{ noticia.resumen }}
            </p>
            <div class="mt-auto pt-4 border-t border-gray-50">
               <span class="text-gray-900 font-medium text-sm group-hover:text-[#F97316] transition-colors">
                Leer más &rarr;
              </span>
            </div>
          </div>
        </article>

      </div>
      
      <div class="mt-16 flex justify-center gap-2">
        <button class="w-10 h-10 rounded-full bg-white border border-gray-200 flex items-center justify-center text-gray-400 hover:text-[#F97316] hover:border-[#F97316] transition-colors">
          <i class="pi pi-angle-left"></i>
        </button>
        <button class="w-10 h-10 rounded-full bg-[#F97316] text-white font-bold shadow-md">1</button>
        <button class="w-10 h-10 rounded-full bg-white border border-gray-200 text-gray-600 hover:text-[#F97316] hover:border-[#F97316] font-medium transition-colors">2</button>
        <button class="w-10 h-10 rounded-full bg-white border border-gray-200 text-gray-600 hover:text-[#F97316] hover:border-[#F97316] font-medium transition-colors">3</button>
        <button class="w-10 h-10 rounded-full bg-white border border-gray-200 flex items-center justify-center text-gray-600 hover:text-[#F97316] hover:border-[#F97316] transition-colors">
          <i class="pi pi-angle-right"></i>
        </button>
      </div>

    </section>

    <Footer class="mt-auto" />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '../components/landing/Footer/Footer.vue';

// Datos estáticos realistas para la ONG (en el futuro esto vendría de una API o CMS)
const listaNoticias = [
  {
    id: 1,
    categoria: 'Equipamiento',
    fecha: '02 Nov, 2025',
    titulo: 'Entrega de 500 kits de nacimiento seguro en municipios rurales de Chuquisaca',
    resumen: 'La MNMNS entregó insumos médicos críticos a centros de salud de primer nivel, garantizando que el personal médico tenga las herramientas estériles necesarias para atender partos limpios y seguros.',
    imagen: '/img/fondo1.jpg'
  },
  {
    id: 2,
    categoria: 'Capacitación',
    fecha: '28 Oct, 2025',
    titulo: 'Integrando saberes: Capacitación a parteras tradicionales en Potosí',
    resumen: 'En el marco de la política SAFCI, se llevó a cabo un taller uniendo la medicina académica con los saberes ancestrales de las parteras locales para identificar señales de peligro durante el embarazo.',
    imagen: '/img/fondo2.jpg'
  },
  {
    id: 3,
    categoria: 'Reportes',
    fecha: '10 Oct, 2025',
    titulo: 'Nuevo informe revela avances en la reducción de mortalidad materna',
    resumen: 'El observatorio de la Mesa Nacional publicó los datos del último trimestre, mostrando una tendencia positiva gracias a la implementación de las Casas Maternas en áreas de difícil acceso.',
    imagen: '/img/fondo3.png'
  },
  {
    id: 4,
    categoria: 'Comunidad',
    fecha: '25 Sep, 2025',
    titulo: 'Lanzamiento de la campaña radial "Mi parto, mis derechos"',
    resumen: 'Se emitirán cuñas radiales en quechua, aymara y guaraní para informar a las mujeres embarazadas sobre su derecho a recibir atención médica gratuita y respetuosa en todo el país.',
    imagen: '/img/fondo4.jpg'
  },
  {
    id: 5,
    categoria: 'Institucional',
    fecha: '12 Sep, 2025',
    titulo: 'OPS/OMS se suma como aliado estratégico de la Mesa de Maternidad',
    resumen: 'La Organización Panamericana de la Salud firmó un convenio para brindar apoyo técnico y financiero a las iniciativas de salud perinatal promovidas por la MNMNS y el gobierno boliviano.',
    imagen: '/img/fondo5.jpg'
  },
  {
    id: 6,
    categoria: 'Salud Neonatal',
    fecha: '05 Sep, 2025',
    titulo: 'Inauguración de nueva sala de cuidados intensivos neonatales en El Alto',
    resumen: 'Con el apoyo de donantes internacionales, el Hospital del Norte cuenta ahora con 10 nuevas incubadoras de última generación para atender a bebés prematuros o con complicaciones.',
    imagen: '/img/fondo6.jpg'
  }
];

onMounted(() => {
  document.title = 'Últimas Noticias | MNMNS Bolivia';
  window.scrollTo(0, 0);
});
</script>