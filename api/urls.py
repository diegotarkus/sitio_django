from django.urls import path
from .views import *

urlpatterns = [
    path('crud/conciertos/', lista_concert),
    path('crud/conciertos/<str:videogame_id>', concierto_info),
"""     path('crud/artistas/', lista_artista), """
]