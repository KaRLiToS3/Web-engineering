from django.db import models

# Create your models here.
class Faccion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    faccion = models.ForeignKey(Faccion, related_name='personajes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre