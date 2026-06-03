from django.db import models


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