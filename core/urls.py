from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('home/', home, name='home'),
    path('conciertos/', conciertos, name='conciertos'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]