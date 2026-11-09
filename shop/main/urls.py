from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('register-data/', views.register_data, name='register_data'),
]