from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('home/', home, name='home'),
    path('conciertos/', conciertos, name='conciertos'),
    path('contact/', contacto, name='contact'),
    path('api/', api, name='api'),
    path('about/', about, name='about'),
    path('infomacion/<str:concierto_id>', informacion, name='informacion'),
]