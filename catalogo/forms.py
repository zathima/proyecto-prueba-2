from django import forms
from django.forms import ModelForm
from .models import Persona, Pregunta
from django.contrib.auth.forms import UserCreationForm



class PreguntaForm(ModelForm):
	class Meta:
		model = Pregunta
		fields = ['field_context', 'field_sender']

class PersonaForm(ModelForm):
	
	class  Meta: 
		model = Persona
		fields = ['field_name', 'field_last_name', 'field_password', 'field_email', 'field_age', 'field_phone' ]
			


class CustomUserForm(UserCreationForm):
	pass