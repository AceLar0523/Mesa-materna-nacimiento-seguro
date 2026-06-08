from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Modelo personalizado de usuario que extiende AbstractUser de Django.
    Permite futuras extensiones y personalizaciones específicas del sistema.
    """
    
    ROLE_CHOICES = [
        ('user', 'Usuario Regular'),
        ('moderator', 'Moderador'),
        ('admin', 'Administrador'),
    ]
    
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user',
        help_text='Rol del usuario en el sistema'
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"
    
    def has_permission(self, permission):
        """Verificar si el usuario tiene un permiso específico"""
        if self.is_superuser:
            return True
        return self.user_permissions.filter(codename=permission).exists()


class RegistroMaternal(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class BlogPost(models.Model):
    CATEGORIA_RECOMENDACION = 'Recomendacion'
    CATEGORIA_TESTIMONIO = 'Testimonio'
    CATEGORIA_OPINION = 'Opinion'
    CATEGORIA_DUDA = 'Duda'

    CATEGORIAS = [
        (CATEGORIA_RECOMENDACION, 'Recomendacion Medica'),
        (CATEGORIA_TESTIMONIO, 'Testimonio de Vida'),
        (CATEGORIA_OPINION, 'Opinion'),
        (CATEGORIA_DUDA, 'Duda / Consulta'),
    ]

    autor = models.CharField(max_length=120, default='Anonimo')
    categoria = models.CharField(max_length=32, choices=CATEGORIAS, default=CATEGORIA_TESTIMONIO)
    titulo = models.CharField(max_length=180)
    contenido = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titulo


class ContactMessage(models.Model):
    ASUNTO_GENERAL = 'General'
    ASUNTO_ALIADO = 'Aliado'
    ASUNTO_PRENSA = 'Prensa'
    ASUNTO_DENUNCIA = 'Denuncia'

    ASUNTOS = [
        (ASUNTO_GENERAL, 'Consulta General'),
        (ASUNTO_ALIADO, 'Quiero ser Institucion Aliada'),
        (ASUNTO_PRENSA, 'Contacto de Prensa'),
        (ASUNTO_DENUNCIA, 'Reporte / Sugerencia'),
    ]

    nombre = models.CharField(max_length=120)
    email = models.EmailField()
    asunto = models.CharField(max_length=24, choices=ASUNTOS, default=ASUNTO_GENERAL)
    mensaje = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.nombre} - {self.asunto}'