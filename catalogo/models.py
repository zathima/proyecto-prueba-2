from django.db import models
from django.urls import reverse
import uuid



# Create your models here.
class Persona(models.Model):

	field_name = models.CharField(max_length=200)
	field_last_name = models.CharField(max_length=200)
	field_password =models.CharField(max_length=200)
	field_email =models.EmailField(blank=True)
	field_age =models.IntegerField(default=18)
	field_phone =models.CharField(max_length=200)
	field_image =models.ImageField(null=True, blank=True)



	class Meta:
		ordering = ['field_last_name' , 'field_name' ]

	def get_absolute_url(self):
		return reverse('Persona-detail', args=[str(self.id)])

	def __str__(self):
		return f'{self.field_name}'


class Pregunta(models.Model):
	field_context =models.TextField()
	field_sender =models.ForeignKey('Persona', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.field_context

	def get_absolute_url(self):
		return reverse('Pregunta-detail', args=[str(self.id)])	


