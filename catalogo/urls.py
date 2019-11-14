from django.urls import path 
from .views import home, registro, login, preguntasyrespuestas

urlpatterns = [ 
    path('', home, name="home"),
    path('registro.html', registro, name="registro"),
    path('home.html', home, name="home2"),
    path('iniciosesiom.html', login, name="login"),
    path('preguntasyrespuestas.html', preguntasyrespuestas, name="preguntasyrespuestas"),
] 