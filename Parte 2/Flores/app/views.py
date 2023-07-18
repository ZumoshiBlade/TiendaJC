from django.contrib.auth import authenticate
from django.core import paginator
from django.db.models import query
from .forms import *
from django.shortcuts import redirect, render
from .models import *
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from rest_framework import viewsets
from .serializer import *
# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def login(request):
    return render(request, 'app/login.html')

def productos(request):
    productoAll = producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productoAll, 8)
        productoAll = paginator.page(page)
    except:
        raise Http404
    
    datos = {
        'lista' : productoAll,
        'paginator' : paginator
    }
    return render(request, 'app/productos.html', datos)

def lista_productos(request):
    productoAll = producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productoAll, 8)
        productoAll = paginator.page(page)
    except:
        raise Http404
    
    datos = {
        'lista' : productoAll,
        'paginator' : paginator
    }
    return render(request, 'app/lista_productos.html', datos)

@permission_required('app.add_producto')
def agregar(request):
    datos = {
        'form' : productoForm()
    }
    
    if request.method == 'POST':
        formulario = productoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "¡Producto añadido correctamente!"

        datos['form'] = formulario

    return render(request, 'app/agregar.html', datos)
@permission_required('app.change_producto')
def modificar(request, id):
    product = producto.objects.get(id=id)
    datos = {
        'form' : productoForm2(instance=product)
    }
    
    if request.method == 'POST':
        formulario = productoForm2(data=request.POST, instance=product, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "¡Producto Modificado!"
            datos['form'] = formulario 
        
    return render(request, 'app/modificar.html', datos)
@permission_required('app.delete_producto')
def eliminar(request, id):
    product = producto.objects.get(id=id)
    product.delete()
    
    return redirect(to="lista_productos")

def registro_usuario(request):
    
    datos = {
        'form' : SignUpForm()
    }

    if request.method == 'POST':
        formulario2 = SignUpForm(request.POST)
        if formulario2.is_valid():
            formulario2.save()
            usuario = authenticate(username=formulario2.cleaned_data["username"],password=formulario2.cleaned_data["password1"])
            return redirect(to='index')
        

    return render(request, 'registration/signup.html', datos)

@permission_required('app.add_suscripcion')
def lista_suscripcion(request):
    suscripcionAll = suscriptUser.objects.all()
    tipSuscripcionAll = suscripcion.objects.all()
    datos ={'listaUsuarios' : suscripcionAll, 'listaSuscripcion': tipSuscripcionAll}
    return render(request, 'app/lista_suscripcion.html', datos)
@permission_required('app.add_suscripcion')
def descuentos(request):
    tipSuscripcionAll = suscripcion.objects.all()
    
    datos ={'listaSuscripcion': tipSuscripcionAll}
    
    return render(request, 'app/descuentos.html', datos)
@permission_required('app.add_suscripcion')
def agregar_descuento(request):
    datos = {
        'formu' : DescuentoForm()
    }

    if request.method == 'POST':
        formulario = DescuentoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "¡Descuento añadido correctamente!"
            
        datos['formu'] = formulario
        
    return render(request, 'app/agregar_descuento.html', datos)
@permission_required('app.add_suscripcion')
def eliminar_descuento(request, id):
    descuentos = suscripcion.objects.get(id=id)
    descuentos.delete()
    
    return redirect(to="descuentos")
@permission_required('app.add_suscripcion')
def eliminar_suscriptor(request, id):
    suscriptor = suscriptUser.objects.get(id=id)
    suscriptor.delete()
    
    return redirect(to="lista_suscripcion")
@permission_required('app.add_suscripcion')
def modificar_suscripcion(request, id):
    Suscripcion = suscripcion.objects.get(id=id)
    datos = {
        'formu' : DescuentoForm(instance=Suscripcion)
    }

    if request.method == 'POST':
        formulario = DescuentoForm(data=request.POST, instance=Suscripcion)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "¡Descuento modificado correctamente!"
            datos['formu'] = formulario
        
    return render(request, 'app/modificar_suscripcion.html', datos)

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = suscriptUser.objects.all()
    serializer_class = SuscripcionSerializer
    
    def get_queryset(self):
        suscri = suscriptUser.objects.all()
        
        usuario = self.request.GET.get('usuario')

        if usuario:
            suscri = suscri.filter(usuario__contains=usuario)
        
        return suscri

def suscripcion_usuario(request):
    
    datos = {
        'formulario' : SuscriptForm()
    }
    
    if request.method == 'POST':
        formu = SuscriptForm(request.POST)
        if formu.is_valid():
            formu.save()
            datos['mensaje'] = "¡Te has suscrito con éxito!"
        
        datos['formulario'] = formu
    return render(request, 'app/suscripcion.html', datos)

def carrito(request):
    return render(request, 'app/carrito.html')