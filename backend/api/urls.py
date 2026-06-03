from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Añadimos chat_materna a la línea de importación
from .views import BlogPostViewSet, ContactMessageViewSet, RegistroViewSet, blog_stream, chat_materna 

router = DefaultRouter()
router.register(r'registros', RegistroViewSet)
router.register(r'blog-posts', BlogPostViewSet, basename='blog-post')
router.register(r'contact-messages', ContactMessageViewSet, basename='contact-message')

urlpatterns = [
    path('blog/stream/', blog_stream, name='blog-stream'),
    path('chat/', chat_materna, name='chat-materna'), # <-- Tu nueva ruta del chatbot
    path('', include(router.urls)),
]