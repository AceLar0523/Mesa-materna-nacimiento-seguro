from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('me/', views.me_view, name='me'),
    path('profile/', views.update_profile_view, name='update_profile'),
]
