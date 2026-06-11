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
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
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
    CATEGORIA_NOTICIA = 'Noticia'
    CATEGORIA_PUBLICACION = 'Publicacion'

    CATEGORIAS = [
        (CATEGORIA_RECOMENDACION, 'Recomendacion Medica'),
        (CATEGORIA_TESTIMONIO, 'Testimonio de Vida'),
        (CATEGORIA_OPINION, 'Opinion'),
        (CATEGORIA_DUDA, 'Duda / Consulta'),
        (CATEGORIA_NOTICIA, 'Noticia'),
        (CATEGORIA_PUBLICACION, 'Publicacion'),
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


class HealthCenter(models.Model):
    NIVEL_I = 'I'
    NIVEL_II = 'II'
    NIVEL_III = 'III'

    LEVELS = [
        (NIVEL_I, 'Nivel I'),
        (NIVEL_II, 'Nivel II'),
        (NIVEL_III, 'Nivel III'),
    ]

    nombre = models.CharField(max_length=180)
    nivel = models.CharField(max_length=3, choices=LEVELS)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=120, default='')
    telefono = models.CharField(max_length=40)
    telefono_emergencia = models.CharField(max_length=40, blank=True, default='')
    horario = models.CharField(max_length=120, blank=True, default='')
    ambulancia_disponible = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nivel', 'nombre']

    def __str__(self):
        return self.nombre


class PanicAlert(models.Model):
    STATUS_OPEN = 'open'
    STATUS_ACKNOWLEDGED = 'acknowledged'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = [
        (STATUS_OPEN, 'Abierta'),
        (STATUS_ACKNOWLEDGED, 'Reconocida'),
        (STATUS_CLOSED, 'Cerrada'),
    ]

    session_token = models.CharField(max_length=64, db_index=True)
    symptom = models.CharField(max_length=120, blank=True, default='')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_OPEN)
    note = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Alerta {self.session_token[:8]}'


class AdolescentConsultation(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_ANSWERED = 'answered'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_ANSWERED, 'Respondida'),
        (STATUS_CLOSED, 'Cerrada'),
    ]

    TOPIC_CONTRACEPCION = 'contracepcion'
    TOPIC_PREVENCION = 'prevencion'
    TOPIC_CICLO = 'ciclo'
    TOPIC_OTRO = 'otro'

    TOPIC_CHOICES = [
        (TOPIC_CONTRACEPCION, 'Anticoncepción'),
        (TOPIC_PREVENCION, 'Prevención'),
        (TOPIC_CICLO, 'Ciclo menstrual'),
        (TOPIC_OTRO, 'Otra consulta'),
    ]

    session_token = models.CharField(max_length=64, db_index=True)
    topic = models.CharField(max_length=24, choices=TOPIC_CHOICES, default=TOPIC_OTRO)
    question = models.TextField()
    answer = models.TextField(blank=True, default='')
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_PENDING)
    responder_name = models.CharField(max_length=120, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    answered_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Consulta {self.session_token[:8]}'


class NearMissRecord(models.Model):
    CONDITION_CHOICES = [
        ('hemorrhage', 'Hemorragia severa'),
        ('hypertension', 'Trastorno hipertensivo severo (Preeclampsia/Eclampsia)'),
        ('sepsis', 'Infección sistémica severa / Sepsis'),
        ('other', 'Otra complicación severa'),
    ]

    patient_age = models.PositiveIntegerField()
    gestational_age = models.PositiveIntegerField(help_text="Edad gestacional en semanas")
    condition = models.CharField(max_length=24, choices=CONDITION_CHOICES)
    health_center = models.ForeignKey(HealthCenter, on_delete=models.SET_NULL, null=True, blank=True)
    
    # 3 Delays
    delay_1_decision = models.BooleanField(default=False, verbose_name="Demora 1: Decisión")
    delay_1_details = models.TextField(blank=True, default='', help_text="Demora en tomar la decisión de buscar ayuda (e.g. desconocimiento, barreras culturales)")
    
    delay_2_transport = models.BooleanField(default=False, verbose_name="Demora 2: Transporte")
    delay_2_details = models.TextField(blank=True, default='', help_text="Demora en llegar al centro de salud (e.g. distancia, falta de transporte, mal estado de vías)")
    
    delay_3_care = models.BooleanField(default=False, verbose_name="Demora 3: Atención")
    delay_3_details = models.TextField(blank=True, default='', help_text="Demora en recibir atención oportuna y de calidad (e.g. falta de personal, insumos, burocracia)")
    
    survival_status = models.CharField(max_length=24, choices=[('survived', 'Sobrevivió'), ('deceased', 'Falleció')], default='survived')
    notes = models.TextField(blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Registro Near-Miss'
        verbose_name_plural = 'Registros Near-Miss'

    def __str__(self):
        return f'Near-Miss {self.id} - {self.get_condition_display()} (Edad: {self.patient_age})'