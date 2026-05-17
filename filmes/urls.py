from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views

app_name = 'filmes'

urlpatterns = [
    path('lista/', views.lista_de_filmes, name='lista_de_filmes'),
    path('detalhes/', views.detalhes_do_filme, name='detalhes_do_filme'),
]

