from django.contrib import admin
from .models import AdolescentConsultation, BlogPost, ContactMessage, HealthCenter, PanicAlert, RegistroMaternal, NearMissRecord
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import BlogPost, ContactMessage, RegistroMaternal, User, NearMissRecord


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


@admin.register(HealthCenter)
class HealthCenterAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'nivel', 'ciudad', 'telefono', 'ambulancia_disponible', 'updated_at')
	list_filter = ('nivel', 'ciudad', 'ambulancia_disponible')
	search_fields = ('nombre', 'direccion', 'telefono', 'telefono_emergencia')


@admin.register(PanicAlert)
class PanicAlertAdmin(admin.ModelAdmin):
	list_display = ('id', 'session_token', 'symptom', 'status', 'latitude', 'longitude', 'created_at')
	list_filter = ('status', 'created_at')
	search_fields = ('session_token', 'symptom', 'note')


@admin.register(AdolescentConsultation)
class AdolescentConsultationAdmin(admin.ModelAdmin):
	list_display = ('id', 'session_token', 'topic', 'status', 'responder_name', 'created_at', 'answered_at')
	list_filter = ('topic', 'status', 'created_at')
	search_fields = ('session_token', 'question', 'answer', 'responder_name')


@admin.register(NearMissRecord)
class NearMissRecordAdmin(admin.ModelAdmin):
	list_display = ('id', 'condition', 'patient_age', 'gestational_age', 'health_center', 'survival_status', 'created_at')
	list_filter = ('condition', 'survival_status', 'delay_1_decision', 'delay_2_transport', 'delay_3_care', 'created_at')
	search_fields = ('condition', 'delay_1_details', 'delay_2_details', 'delay_3_details', 'notes')
