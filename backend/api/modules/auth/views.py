from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from api.models import User
from .serializers import (
    UserSerializer,
    UserDetailSerializer,
    RegisterSerializer,
    LoginSerializer
)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    Endpoint para registrar un nuevo usuario
    POST /api/auth/register/
    """
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Crear token para el nuevo usuario
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'message': 'Usuario registrado exitosamente',
            'token': token.key,
            'user': UserDetailSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    Endpoint para iniciar sesión
    POST /api/auth/login/
    Body: { "email": "user@example.com", "password": "password" }
    """
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        # Obtener o crear token
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'message': 'Sesión iniciada exitosamente',
            'token': token.key,
            'user': UserDetailSerializer(user).data
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    """
    Endpoint para obtener datos del usuario autenticado
    GET /api/auth/me/
    """
    serializer = UserDetailSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    Endpoint para cerrar sesión
    POST /api/auth/logout/
    """
    # Eliminar el token del usuario
    request.user.auth_token.delete()
    
    return Response({
        'message': 'Sesión cerrada exitosamente'
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile_view(request):
    """
    Endpoint para actualizar el perfil del usuario
    PUT /api/auth/profile/
    """
    user = request.user
    
    # Actualizar campos permitidos
    if 'first_name' in request.data:
        user.first_name = request.data['first_name']
    if 'last_name' in request.data:
        user.last_name = request.data['last_name']
    
    user.save()
    
    return Response({
        'message': 'Perfil actualizado exitosamente',
        'user': UserDetailSerializer(user).data
    }, status=status.HTTP_200_OK)
