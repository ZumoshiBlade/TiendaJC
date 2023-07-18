from .forms import *
from .models import *
from django.contrib import admin

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'tipo']
    search_fields = ['nombre']
    list_per_page = 4
    form = productoForm




admin.site.register(tipo_producto)
admin.site.register(producto, ProductoAdmin)
admin.site.register(suscripcion)
admin.site.register(suscriptUser)
