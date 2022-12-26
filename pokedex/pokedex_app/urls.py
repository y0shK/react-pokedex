from django.urls import path

from . import views

# https://docs.djangoproject.com/en/4.1/intro/tutorial03/

urlpatterns = [
    path('', views.index, name='index'),
    path('pkmn_info', views.pokeapi_view, name='pkmn_info'),
]
