import json
import time

from django.http import StreamingHttpResponse
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import AdolescentConsultation, BlogPost, ContactMessage, HealthCenter, PanicAlert, RegistroMaternal
from .serializers import (
    AdolescentConsultationSerializer,
    BlogPostSerializer,
    ContactMessageSerializer,
    HealthCenterSerializer,
    PanicAlertSerializer,
    RegistroSerializer,
)

# --- NUEVO IMPORT PARA EL CHATBOT ---
from ai_service.chat_core import get_maternal_chatbot_response

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = RegistroMaternal.objects.all()
    serializer_class = RegistroSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes += 1
        post.save(update_fields=['likes', 'updated_at'])
        return Response(self.get_serializer(post).data, status=status.HTTP_200_OK)

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'delete', 'head', 'options']


class HealthCenterViewSet(viewsets.ModelViewSet):
    queryset = HealthCenter.objects.all()
    serializer_class = HealthCenterSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'patch', 'head', 'options']

    def get_queryset(self):
        queryset = super().get_queryset()
        nivel = self.request.query_params.get('nivel')
        if nivel:
            queryset = queryset.filter(nivel=nivel)
        return queryset


class PanicAlertViewSet(viewsets.ModelViewSet):
    queryset = PanicAlert.objects.all()
    serializer_class = PanicAlertSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'patch', 'head', 'options']

    def get_queryset(self):
        queryset = super().get_queryset()
        session_token = self.request.query_params.get('session_token')
        if session_token:
            queryset = queryset.filter(session_token=session_token)
        return queryset


class AdolescentConsultationViewSet(viewsets.ModelViewSet):
    queryset = AdolescentConsultation.objects.all()
    serializer_class = AdolescentConsultationSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'patch', 'head', 'options']

    def get_queryset(self):
        queryset = super().get_queryset()
        session_token = self.request.query_params.get('session_token')
        status_filter = self.request.query_params.get('status')

        if session_token:
            queryset = queryset.filter(session_token=session_token)

        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset

@api_view(['GET'])
@permission_classes([AllowAny])
def blog_stream(request):
    def event_stream():
        last_seen = None

        while True:
            latest = BlogPost.objects.order_by('-updated_at').values_list('updated_at', flat=True).first()
            latest_key = latest.isoformat() if latest else 'empty'

            if latest_key != last_seen:
                last_seen = latest_key
                payload = BlogPostSerializer(BlogPost.objects.all()[:50], many=True).data
                yield f"data: {json.dumps(payload)}\n\n"
            else:
                heartbeat = {'heartbeat': timezone.now().isoformat()}
                yield f": keep-alive {json.dumps(heartbeat)}\n\n"

            time.sleep(2)

    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    response['X-Accel-Buffering'] = 'no'
    return response

# --- NUEVA VISTA PARA EL CHATBOT ---
@api_view(['POST'])
@permission_classes([AllowAny])
def chat_materna(request):
    mensaje_usuario = request.data.get('mensaje')
    
    if not mensaje_usuario:
        return Response({'error': 'El mensaje está vacío'}, status=400)
    
    try:
        # Llamamos a nuestro motor LangChain / Gemini
        respuesta_bot = get_maternal_chatbot_response(mensaje_usuario)
        return Response({'respuesta': respuesta_bot}, status=200)
    except Exception as e:
        # Si Gemini o LangChain fallan, enviamos el error exacto a la consola para depurar
        print(f"Error en RAG: {str(e)}") 
        return Response({'respuesta': 'Lo siento, no pude procesar tu consulta en este momento. Intenta de nuevo.'}, status=500)