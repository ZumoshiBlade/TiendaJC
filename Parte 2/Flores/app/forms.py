from django import forms
from django.contrib.auth import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields, widgets
from .models import *
from django.contrib.auth.forms import UserChangeForm, UserCreationForm        
from django.contrib.auth.models import User
from .validators import TamañoMaximoValidator

class productoForm(ModelForm):
    
    nombre = forms.CharField(min_length=3,max_length=200)
    precio = forms.IntegerField(min_value=1, max_value=100000)
    imagen = forms.ImageField(validators=[TamañoMaximoValidator(maxfile=4)],required=False)
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        existe = producto.objects.filter(nombre__iexact=nombre).exists()
        if existe:
            raise ValidationError("Este artículo ya existe.")
        return nombre
    
    class Meta:
        model = producto
        #fields = ['nombre', 'precio', 'tipo', 'imagen']
        fields = '__all__'
        
class productoForm2(ModelForm):
    
    nombre = forms.CharField(min_length=3,max_length=200)
    precio = forms.IntegerField(min_value=1, max_value=100000)
    imagen = forms.ImageField(validators=[TamañoMaximoValidator(maxfile=4)],required=False)
    
    class Meta:
        model = producto
        fields = '__all__'

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class SuscriptForm(ModelForm):
    usuario = forms.CharField(min_length=3, max_length=200)
    email = forms.EmailField(max_length=200)
    
    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        existe = suscriptUser.objects.filter(usuario__iexact=usuario).exists()
        if existe: 
            raise ValidationError("¡Este usuario ya esta suscrito!")
        return usuario
    
    def clean_email(self):
        email = self.cleaned_data['email']
        existe = suscriptUser.objects.filter(email__iexact=email).exists()
        
        if existe:
            raise ValidationError('¡Ya tienes suscripción!')
        
        return email

    class Meta:
        model = suscriptUser
        fields = '__all__'

class DescuentoForm(ModelForm):
    descripcion = forms.CharField(min_length=5, max_length=200)
    descuento = forms.IntegerField()
    duracion = forms.IntegerField()
    
    class Meta:
        model = suscripcion
        fields = '__all__'
