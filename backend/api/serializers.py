from rest_framework import serializers
from .models import AdolescentConsultation, BlogPost, ContactMessage, HealthCenter, PanicAlert, RegistroMaternal

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroMaternal
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'autor',
            'categoria',
            'titulo',
            'contenido',
            'likes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'likes', 'created_at', 'updated_at']

    def validate_autor(self, value):
        autor = (value or '').strip()
        return autor or 'Anonimo'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'nombre', 'email', 'asunto', 'mensaje', 'created_at']
        read_only_fields = ['id', 'created_at']


class HealthCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCenter
        fields = [
            'id',
            'nombre',
            'nivel',
            'direccion',
            'ciudad',
            'telefono',
            'telefono_emergencia',
            'horario',
            'ambulancia_disponible',
            'latitude',
            'longitude',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class PanicAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanicAlert
        fields = [
            'id',
            'session_token',
            'symptom',
            'latitude',
            'longitude',
            'status',
            'note',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AdolescentConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdolescentConsultation
        fields = [
            'id',
            'session_token',
            'topic',
            'question',
            'answer',
            'status',
            'responder_name',
            'created_at',
            'answered_at',
        ]
        read_only_fields = ['id', 'created_at', 'answered_at']