from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, EmailField, IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class tipo_producto(models.Model):
    tipo = models.CharField(max_length=80)
    
    def __str__(self):
        return self.tipo
        
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    tipo = models.ForeignKey(tipo_producto, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)
    
    
    def __str__(self):
        return self.nombre
    
class suscripcion(models.Model):
    descripcion = CharField(max_length=200)
    descuento = IntegerField()
    duracion = IntegerField()
    
    def __str__(self):
        return self.descripcion

class suscriptUser(models.Model):
    usuario = CharField(max_length=200)
    email = EmailField(max_length=200)
    descripcion = ForeignKey(suscripcion, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario

#python manage.py makemigrations --> CREA ARCHIVO MIGRATIONS
#python manage.py migrate --> ENVIA EL ARCHIVO A LA BD
#python manage.py createsuperuser --> CREA EL ADMIN DE LA WEB