from rest_framework import serializers
from .models import BlogPost, ContactMessage, RegistroMaternal

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