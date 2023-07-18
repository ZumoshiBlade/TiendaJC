from django.db import router
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('suscripcion', SuscripcionViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('login/', login, name="login"),
    path('productos/', productos, name="productos"),
    path('lista_productos/', lista_productos, name="lista_productos"),    
    path('agregar/', agregar, name="agregar"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('registro_usuario/', registro_usuario, name="registro_usuario"),
    path('suscripcion/', suscripcion_usuario, name="suscripcion"),
    path('lista_suscripcion/', lista_suscripcion, name="lista_suscripcion"),
    path('eliminar_suscriptor/<id>/', eliminar_suscriptor, name="eliminar_suscriptor"),
    path('eliminar_descuento/<id>/', eliminar_descuento, name="eliminar_descuento"),
    path('modificar_suscripcion/<id>/', modificar_suscripcion, name="modificar_suscripcion"),
    path('agregar_descuento/', agregar_descuento, name="agregar_descuento"),
    path('descuentos/', descuentos, name="descuentos"),
    path('api/', include(router.urls)),
    path('carrito/', carrito, name="carrito")
]