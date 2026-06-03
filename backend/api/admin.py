from django.contrib import admin
from .models import BlogPost, ContactMessage, RegistroMaternal


@admin.register(RegistroMaternal)
class RegistroMaternalAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'fecha')
	search_fields = ('nombre',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulo', 'autor', 'categoria', 'likes', 'created_at')
	list_filter = ('categoria', 'created_at')
	search_fields = ('titulo', 'autor', 'contenido')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'email', 'asunto', 'created_at')
	list_filter = ('asunto', 'created_at')
	search_fields = ('nombre', 'email', 'mensaje')
