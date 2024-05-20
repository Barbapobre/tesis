from django.db import models

class Ingrediente(models.Model):
    creado = models.DateField(auto_now=True)
    nombre = models.CharField(max_length=40)
    costo = models.IntegerField(null=False)
    cantidad = models.IntegerField()
    
    
    def __str__(self) -> str:
        return f'{self.nombre}'
    
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    costo = models.IntegerField(null=False)
    ganancia = models.IntegerField()
    img = models.ImageField(
        upload_to='C:\\Users\\Little Thing\\Documents\\pizzamoji\\static\\',
        unique=True,
       blank=True,
       default=""
    )
    
    def __str__(self) -> str:
        return f'{self.nombre}'
    
    
class CantidadTotal(models.Model):
    tipo = models.CharField(max_length=100)
    cantidad = models.IntegerField()