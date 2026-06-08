from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError as DjangoValidationError
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer para el modelo de User"""
    
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'created_at']
        read_only_fields = ['id', 'created_at']


class UserDetailSerializer(serializers.ModelSerializer):
    """Serializer detallado del usuario con más información"""
    
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'full_name', 'role', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def get_full_name(self, obj):
        return obj.get_full_name()


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer para registrar nuevos usuarios"""
    
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'password_confirm']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                'password': 'Las contraseñas no coinciden.'
            })
        
        # Verificar que el email no exista
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({
                'email': 'Este email ya está registrado.'
            })
        
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        
        user = User.objects.create_user(
            username=validated_data['email'],  # Usar email como username
            **validated_data
        )
        user.set_password(password)
        user.save()
        
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer para login con email y contraseña"""
    
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        # Buscar usuario por email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                'email': 'Usuario no encontrado.'
            })
        
        # Autenticar con el usuario encontrado
        authenticated_user = authenticate(username=user.username, password=password)
        
        if not authenticated_user:
            raise serializers.ValidationError({
                'password': 'Contraseña incorrecta.'
            })
        
        if not authenticated_user.is_active:
            raise serializers.ValidationError({
                'email': 'Esta cuenta ha sido desactivada.'
            })
        
        attrs['user'] = authenticated_user
        return attrs
