from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import BlogPost, ContactMessage, RegistroMaternal, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
	list_display = ('id', 'email', 'first_name', 'last_name', 'role', 'is_active', 'created_at')
	list_filter = ('role', 'is_active', 'created_at')
	search_fields = ('email', 'first_name', 'last_name')
	fieldsets = BaseUserAdmin.fieldsets + (
		('Información Adicional', {'fields': ('role', 'created_at', 'updated_at')}),
	)
	readonly_fields = ('created_at', 'updated_at')


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
