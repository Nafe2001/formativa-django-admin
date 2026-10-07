from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Paquete(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    valor = models.IntegerField()
    cantidad = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

    