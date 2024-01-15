from django.db import models
from polls.choices import categorias

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    categoria = models.CharField(max_length=200, choices=categorias, default="")
    

    def __str__(self):
        return self.nombre
    
