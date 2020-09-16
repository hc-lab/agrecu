from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()

    def __str__(self):
        return "producto: {} precio: s/{}".format(self.nombre, self.precio)
