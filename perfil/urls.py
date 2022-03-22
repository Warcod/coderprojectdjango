"""miproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from perfil import views

urlpatterns = [
    path('movies/', views.movies, name='movies'),
    path('songs/', views.songs, name='songs'),
    path('series/', views.series, name='series'),
    path('form-movie/', views.formMovie, name='formMovie'),
    path('search-movie/', views.searchMovies, name='searchMovie'),
    path('form-serie/', views.formSeries , name='formSerie'),
    path('search-serie/', views.searchSeries, name='searchSerie'),
        path('form-song/', views.formSongs , name='formSong'),
    path('search-song/', views.searchSongs, name='searchSong')
    
]

