from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('plant/<int:plant_id>/', views.plant_dashboard, name='plant_dashboard'),
    path('plant/<int:plant_id>/history/', views.plant_history, name='plant_history'),
]
