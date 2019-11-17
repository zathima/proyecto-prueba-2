from django.shortcuts import render, redirect
from django.views import generic
from .models import Pregunta, Persona
from .forms import PreguntaForm, PersonaForm

# Create your views here.
def eliminar_persona(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()

    return redirect(to="listar_persona")

def modificar_persona(request, id):
    persona = Persona.objects.get(id=id)
    data = {
        'form': PersonaForm(instance=persona)
    }
    if request.method =='POST':
        formulario = PersonaForm(data=request.POST, instance=persona)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Persona Modificada Correctamente"
            data['form'] = formulario
    return render(request,'modificar_persona.html', data)

def persona_list(request):
    preguntas = Pregunta.objects.all()
    data = {
        'preguntas':preguntas
    }
    return render(request, 'persona_list.html', data)

def nueva_pregunta(request):
    data = {
        'form':PreguntaForm()
    }
    if request.method == 'POST':
        formulario = PreguntaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Enviado Correctamente"
    return render(request, 'agregar_pre.html',data)

def modificar_pregunta(request, id):
    pregunta = Pregunta.objects.get(id=id)
    data = {
        'form': PreguntaForm(instance=pregunta)
    }
    if request.method =='POST':
        formulario = PreguntaForm(data=request.POST, instance=pregunta)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Pregunta Modificada Correctamente"
            data['form'] = formulario

    return render(request,'modificar_pre.html', data)

def eliminar_pregunta(request, id):
    pregunta = Pregunta.objects.get(id=id)
    pregunta.delete()

    return redirect(to="persona_list")

def nueva_persona(request):
    data = {
        'form':PersonaForm()

    }
    if request.method == 'POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']= "Guardado correctamente"

    return render(request, 'nueva_persona.html', data)

def home(request):

    return render(request, 'home.html')


def registro(request):
    return render(request, 'registro.html')


def login(request):
	return render(request, 'login.html')



def preguntasyrespuestas(request):    
    return render(request, 'preguntasyrespuestas.html')

def listar_persona(request):
    personas= Persona.objects.all()
    data = {
        'personas': personas
    }
    return render(request, 'listar_persona.html', data)

   	

class PersonaListView(generic.ListView):
	model = Persona
	
class PersonaDetailView(generic.DetailView):
	model = Persona
