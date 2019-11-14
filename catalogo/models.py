from django.db import models
from django.urls import reverse
import uuid



# Create your models here.
class Persona(models.Model):

	field_name = models.CharField(max_length=200, help_text='Nombre de la Persona')
	field_last_name = models.CharField(max_length=200, help_text='Apellido de la Persona')
	field_password =models.CharField(max_length=200, help_text='Contraseña' )
	field_email =models.EmailField(blank=True)
	field_age =models.IntegerField(help_text='edad de la Persona', default=18)
	field_phone =models.CharField(max_length=200, help_text='Numero de telefono')



	class Meta:
		ordering = ['field_last_name' , 'field_name' ]

	def get_absolute_url(self):
		return reverse('Persona-detail', args=[str(self.id)])

	def __str__(self):
		return f'{self.field_last_name}, {self.field_name}, {self.field_age}'


class Pregunta(models.Model):
	field_context =models.TextField(help_text='Contenido de la pregunta')
	field_sender =models.ForeignKey('Persona', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.field_context

	def get_absolute_url(self):
		return reverse('Preguna-detail', args=[str(self.id)])	


