<template>
    <div class="pt-20 bg-gray-50 min-h-screen flex flex-col">

        <PageHero
            kicker="Red de Aliados"
            title="Instituciones Miembro"
            subtitle="La Mesa Nacional de Maternidad y Nacimiento Seguros es un esfuerzo conjunto. Conoce a las organizaciones que aportan recursos, conocimiento y trabajo de campo para salvar vidas en Bolivia."
            backgroundImage="/img/fondo13.png"
        />

        <section class="py-16 flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">

            <div class="flex flex-wrap justify-center gap-3 mb-12 animate-fade-in">
                <button
                    class="px-6 py-2 rounded-full bg-[#F97316] text-white font-bold shadow-md text-sm transition-transform hover:-translate-y-1">Todas</button>
                <button
                    class="px-6 py-2 rounded-full bg-white text-gray-600 border border-gray-200 font-medium hover:border-[#F97316] hover:text-[#F97316] text-sm transition-all">Gubernamentales</button>
                <button
                    class="px-6 py-2 rounded-full bg-white text-gray-600 border border-gray-200 font-medium hover:border-[#F97316] hover:text-[#F97316] text-sm transition-all">Internacionales</button>
                <button
                    class="px-6 py-2 rounded-full bg-white text-gray-600 border border-gray-200 font-medium hover:border-[#F97316] hover:text-[#F97316] text-sm transition-all">Sociedad
                    Civil</button>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

                <article v-for="(inst, index) in instituciones" :key="inst.id"
                    class="bg-white rounded-3xl p-8 border border-gray-100 shadow-sm hover:shadow-xl transition-all duration-300 group flex flex-col items-center text-center animate-slide-up opacity-0"
                    :style="{ animationDelay: `${index * 100}ms`, animationFillMode: 'forwards' }">

                    <div
                        class="w-full h-28 rounded-2xl bg-gray-50 border border-gray-100 shadow-sm flex items-center justify-center mb-6 overflow-hidden group-hover:scale-[1.02] transition-transform duration-300">
                        <img
                            v-if="!logoErrored[inst.id]"
                            :src="inst.logo"
                            :alt="inst.nombre"
                            class="h-full w-full object-contain p-4"
                            @error="logoErrored[inst.id] = true"
                        >
                        <div v-else class="h-full w-full flex items-center justify-center bg-gradient-to-br from-orange-50 to-white text-[#F97316]">
                            <div class="text-center">
                                <div class="text-2xl font-black tracking-wider">{{ inst.iniciales }}</div>
                                <div class="mt-1 text-[10px] font-bold uppercase tracking-[0.2em] text-gray-400">Logo</div>
                            </div>
                        </div>
                    </div>

                    <div class="mb-4">
                        <span :class="[
                            'text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider',
                            inst.tipo === 'Gubernamental' ? 'bg-green-50 text-green-600' :
                                inst.tipo === 'Internacional' ? 'bg-orange-50 text-[#F97316]' :
                                    'bg-orange-50 text-orange-600'
                        ]">
                            {{ inst.tipo }}
                        </span>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-[#F97316] transition-colors">{{
                        inst.nombre }}</h3>
                    <p class="text-gray-600 text-sm leading-relaxed flex-1 mb-6">
                        {{ inst.descripcion }}
                    </p>

                    <div class="mt-auto w-full pt-6 border-t border-gray-100">
                        <a href="#"
                            class="text-gray-400 hover:text-[#F97316] font-medium text-sm flex items-center justify-center gap-2 transition-colors">
                            Visitar sitio web <i class="pi pi-external-link text-xs"></i>
                        </a>
                    </div>
                </article>

            </div>
        </section>

        <section class="bg-[#F97316] py-16">
            <div class="max-w-4xl mx-auto px-4 text-center">
                <h2 class="text-3xl font-bold text-white mb-4">¿Tu organización quiere sumarse?</h2>
                <p class="text-orange-50 mb-8 text-lg">
                    La reducción de la mortalidad materna requiere del esfuerzo de todos. Si tu institución trabaja en
                    salud, derechos humanos o desarrollo social, contáctanos.
                </p>
                <router-link to="/contactanos"
                    class="inline-block px-8 py-4 bg-white text-[#F97316] font-bold rounded-full shadow-lg hover:shadow-xl hover:scale-105 transition-all">
                    Escríbenos para formar una alianza
                </router-link>
            </div>
        </section>

        <Footer class="mt-auto" />
    </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { ref } from 'vue';
import PageHero from '@/components/common/PageHero.vue';
import Footer from '../components/landing/Footer/Footer.vue';

// Datos de las instituciones aliadas (Reales o basadas en la estructura de la Mesa)
const instituciones = [
    {
        id: 1,
        nombre: 'Ministerio de Salud y Deportes',
        tipo: 'Gubernamental',
        iniciales: 'MSD',
        logo: 'https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=1152507556919524',
        descripcion: 'Ente rector que define las políticas públicas, como la estrategia SAFCI y los lineamientos nacionales para la reducción de mortalidad materna.'
    },
    {
        id: 2,
        nombre: 'UNFPA Bolivia',
        tipo: 'Internacional',
        iniciales: 'UNFPA',
        logo: 'https://bolivia.unfpa.org/themes/custom/unfpa_offices/logo.png',
        descripcion: 'Agencia de las Naciones Unidas enfocada en garantizar el equipamiento neonatal, el cumplimiento de derechos y la supervivencia infantil.'
    },
    {
        id: 3,
        nombre: 'OPS / OMS',
        tipo: 'Internacional',
        iniciales: 'OPS',
        logo: 'https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100019381703054',
        descripcion: 'Organización Panamericana de la Salud que brinda asistencia técnica y científica para asegurar prácticas médicas basadas en evidencia.'
    },
    {
        id: 4,
        nombre: 'Mesa Nacional de Maternidad y Nacimiento Seguros',
        tipo: 'Internacional',
        iniciales: 'MNMNS',
        logo: '/img/logo1.jpg',
        descripcion: 'Fondo de Población de las Naciones Unidas, especializado en salud sexual y reproductiva, y prevención de embarazos de alto riesgo.'
    },
    {
        id: 5,
        nombre: 'Sociedad Boliviana de Obstetricia y Ginecología',
        tipo: 'Sociedad Civil',
        iniciales: 'SBOG',
        logo: 'https://gastroenterologia.colegiomedicodebolivia.org/wp-content/uploads/2024/07/LOGO-GINECOLOGIA.png',
        descripcion: 'Agrupa a los especialistas del país, encargándose de la capacitación continua y la elaboración de guías clínicas de atención.'
    },
    {
        id: 6,
        nombre: 'Confederación de Mujeres Campesinas Bartolina Sisa',
        tipo: 'Sociedad Civil',
        iniciales: 'BS',
        logo: 'https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100069179680677',
        descripcion: 'Aporta la visión intercultural y el trabajo comunitario, asegurando que las Casas Maternas respeten los saberes ancestrales.'
    }
];

const logoErrored = ref<Record<number, boolean>>({});

onMounted(() => {
    document.title = 'Instituciones y Aliados | Mesa de Maternidad Bolivia';
    window.scrollTo(0, 0);
});
</script>

<style scoped>
/* Animaciones simples de entrada */
@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.animate-slide-up {
    animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.animate-fade-in {
    animation: fadeIn 1s ease-in-out;
}
</style>