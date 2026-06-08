import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/pages/LandingPage.vue';
import ConocenosPage from '@/pages/ConocenosPage.vue';
import NoticiasPage from '@/pages/NoticiasPage.vue';
import DatosPage from '@/pages/DatosPage.vue';
import BlogPage from '@/pages/BlogPage.vue';
import InstitucionesPage from '@/pages/InstitucionesPage.vue';
import ContactanosPage from '@/pages/ContactanosPage.vue';
import QueHacemosPage from '@/pages/QueHacemosPage.vue';
import PoliticasPublicasPage from '@/pages/PoliticasPublicasPage.vue';
import AccesoCalidadServiciosPage from '@/pages/AccesoCalidadServiciosPage.vue';
import TransformacionNormasPage from '@/pages/TransformacionNormasPage.vue';
import ComunidadPage from '@/pages/ComunidadPage.vue';
import PublicacionesPage from '@/pages/PublicacionesPage.vue';
import CampanasPage from '@/pages/CampanasPage.vue';
import MultimediaPage from '@/pages/MultimediaPage.vue';
import DonamePage from '@/pages/DonamePage.vue';
import AsistenteObstetricoPage from '@/pages/client/AsistenteObstetricoPage.vue';
import GeolocalizadorCentrosPage from '@/pages/client/GeolocalizadorCentrosPage.vue';
import AlarmaPanicoPage from '@/pages/client/AlarmaPanicoPage.vue';
import SaludAdolescentePage from '@/pages/client/SaludAdolescentePage.vue';
import SectorPublicoAdminHome from '@/pages/admin/SectorPublicoAdminHome.vue';
import AdminCentrosSaludPage from '@/pages/admin/AdminCentrosSaludPage.vue';
import AdminAlertasPanicoPage from '@/pages/admin/AdminAlertasPanicoPage.vue';
import AdminConsultasAdolescentesPage from '@/pages/admin/AdminConsultasAdolescentesPage.vue';
import UnfpaBoliviaPage from '@/pages/UnfpaBoliviaPage.vue';
import RepresentantePage from '@/pages/RepresentantePage.vue';
import UnfpaLacPage from '@/pages/UnfpaLacPage.vue';
import UnfpaGlobalPage from '@/pages/UnfpaGlobalPage.vue';
import CategoryPage from '@/pages/CategoryPage.vue';
import FavoritesPage from '@/pages/FavoritesPage.vue';
import CategoryLayout from '@/components/layouts/CategoryLayout.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LandingPage
    },
    {
      path: '/conocenos',
      name: 'Conocenos',
      component: ConocenosPage
    },
    {
      path: '/nuestra-labor',
      name: 'NuestraLabor',
      component: ConocenosPage
    },
    {
      path: '/nuestra-labor/mnmns-en-bolivia',
      name: 'UnfpaBolivia',
      component: UnfpaBoliviaPage
    },
    {
      path: '/nuestra-labor/representante',
      name: 'Representante',
      component: RepresentantePage
    },
    {
      path: '/nuestra-labor/mnmns-america-latina-caribe',
      name: 'UnfpaLac',
      component: UnfpaLacPage
    },
    {
      path: '/nuestra-labor/mnmns-global',
      name: 'UnfpaGlobal',
      component: UnfpaGlobalPage
    },
    {
      path: '/que-hacemos',
      name: 'QueHacemos',
      component: QueHacemosPage
    },
    {
      path: '/que-hacemos/politicas-publicas-rendicion-cuentas',
      name: 'PoliticasPublicas',
      component: PoliticasPublicasPage
    },
    {
      path: '/que-hacemos/acceso-calidad-servicios-atencion',
      name: 'AccesoCalidadServicios',
      component: AccesoCalidadServiciosPage
    },
    {
      path: '/que-hacemos/transformacion-normas-sociales-genero',
      name: 'TransformacionNormas',
      component: TransformacionNormasPage
    },
    {
      path: '/comunidad',
      name: 'Comunidad',
      component: ComunidadPage
    },
    {
      path: '/comunidad/publicaciones',
      name: 'Publicaciones',
      component: PublicacionesPage
    },
    {
      path: '/comunidad/campanas',
      name: 'Campanas',
      component: CampanasPage
    },
    {
      path: '/comunidad/multimedia',
      name: 'Multimedia',
      component: MultimediaPage
    },
    {
      path: '/noticias',
      name: 'Noticias',
      component: NoticiasPage
    },
    {
      path: '/datos',
      name: 'Datos',
      component: DatosPage
    },
    {
      path: '/blog',
      name: 'Blog',
      component: BlogPage
    },
    {
      path: '/instituciones',
      name: 'Instituciones',
      component: InstitucionesPage
    },
    {
      path: '/contactanos',
      name: 'Contactanos',
      component: ContactanosPage
    },
    {
      path: '/doname',
      name: 'Doname',
      component: DonamePage
    },
    {
      path: '/sector-publico/asistente-obstetrico',
      name: 'AsistenteObstetrico',
      component: AsistenteObstetricoPage
    },
    {
      path: '/sector-publico/geolocalizador',
      name: 'GeolocalizadorCentros',
      component: GeolocalizadorCentrosPage
    },
    {
      path: '/sector-publico/alarma-panico',
      name: 'AlarmaPanico',
      component: AlarmaPanicoPage
    },
    {
      path: '/sector-publico/salud-adolescente',
      name: 'SaludAdolescente',
      component: SaludAdolescentePage
    },
    {
      path: '/admin/sector-publico',
      name: 'PublicSectorAdmin',
      meta: { hideHeader: true },
      component: SectorPublicoAdminHome
    },
    {
      path: '/admin/sector-publico/centros',
      name: 'AdminCentrosSalud',
      meta: { hideHeader: true },
      component: AdminCentrosSaludPage
    },
    {
      path: '/admin/sector-publico/alertas',
      name: 'AdminAlertasPanico',
      meta: { hideHeader: true },
      component: AdminAlertasPanicoPage
    },
    {
      path: '/admin/sector-publico/consultas',
      name: 'AdminConsultasAdolescentes',
      meta: { hideHeader: true },
      component: AdminConsultasAdolescentesPage
    },
    {
      path: '/:category/:subcategory',
      meta: { hideHeader: true },
      component: CategoryLayout,
      children: [
        {
          path: '',
          name: 'category',
          component: CategoryPage
        }
      ]
    },
    {
      path: '/favorites',
      name: 'favorites',
      meta: { hideHeader: true },
      component: FavoritesPage
    }
  ]
});

export default router;
