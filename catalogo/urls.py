from django.urls import path 
from .views import home, registro, login, preguntasyrespuestas, persona_list, nueva_pregunta, modificar_pregunta, eliminar_pregunta, nueva_persona, listar_persona, modificar_persona, eliminar_persona
from . import views

urlpatterns = [ 
    path('', home, name="home"),
    path('registro.html', registro, name="registro"),
    path('home.html', home, name="home2"),
    path('iniciosesiom.html', login, name="login"),
    path('preguntasyrespuestas.html', preguntasyrespuestas, name="preguntasyrespuestas"),
    path('persona_list', persona_list, name="persona_list"),
    path('persona/', views.PersonaListView.as_view(), name='persona') ,
	path('persona/<int:pk>', views.PersonaDetailView.as_view(), name='persona-detail'),
    path('agregar_pre.html', nueva_pregunta, name="nueva_pregunta"),
    path('modificar_pre.html<id>/', modificar_pregunta, name="modificar_pregunta"),
    path('eliminar_pre/<id>/', eliminar_pregunta, name="eliminar_pre"),
    path('nueva_persona.html', nueva_persona, name="nueva_persona"),
    path('listar_persona', listar_persona, name="listar_persona"),
    path('modificar_persona/<id>/', modificar_persona, name="modificar_persona"),
    path('eliminar_per/<id>/',eliminar_persona, name="eliminar_per"),

] 

