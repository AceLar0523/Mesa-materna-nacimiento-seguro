from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Añadimos chat_materna a la línea de importación
from .views import (
    AdolescentConsultationViewSet,
    BlogPostViewSet,
    ContactMessageViewSet,
    HealthCenterViewSet,
    PanicAlertViewSet,
    RegistroViewSet,
    blog_stream,
    chat_materna,
    heatmap_data,
    NearMissRecordViewSet,
)

router = DefaultRouter()
router.register(r'registros', RegistroViewSet)
router.register(r'blog-posts', BlogPostViewSet, basename='blog-post')
router.register(r'contact-messages', ContactMessageViewSet, basename='contact-message')
router.register(r'health-centers', HealthCenterViewSet, basename='health-center')
router.register(r'panic-alerts', PanicAlertViewSet, basename='panic-alert')
router.register(r'adolescent-consultations', AdolescentConsultationViewSet, basename='adolescent-consultation')
router.register(r'near-miss', NearMissRecordViewSet, basename='near-miss')

urlpatterns = [
    path('auth/', include('api.modules.auth.urls')),
    path('blog/stream/', blog_stream, name='blog-stream'),
    path('chat/', chat_materna, name='chat-materna'), # <-- Tu nueva ruta del chatbot
    path('heatmap/', heatmap_data, name='heatmap-data'),
    path('', include(router.urls)),
]