import { createI18n } from 'vue-i18n';
import es from './locales/es.json';
import ay from './locales/ay.json';
import qu from './locales/qu.json';

const i18n = createI18n({
  legacy: false, // Usar la API de Composición de Vue 3
  globalInjection: true, // Permitir el uso de $t en todos los templates
  locale: 'es', // Idioma por defecto
  fallbackLocale: 'es',
  messages: {
    es,
    ay,
    qu,
  },
});

export default i18n;
