from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('albums/', views.albums, name='albums'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('profile/', views.profile, name='profile'),
    path('postar/', views.postar, name='postar'),
    path('editar/<int:album_id>/', views.editar_album, name='editar_album'),
    path('deletar/<int:album_id>/', views.deletar_album, name='deletar_album'),
    path('register/', views.register, name='register'),
]
