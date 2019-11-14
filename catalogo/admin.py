from django.contrib import admin

# Register your models here.

from . models import Persona, Pregunta

admin.site.register(Persona)
admin.site.register(Pregunta)

