from django.contrib import admin
from django.utils.html import format_html
from . import models

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'costo',
        'img',
    ]
    search_fields = ['nombre']

    def foto(self,obj):
        return format_html('<img src={} width="100px" heigth="100px" />',obj.img.url)


class IngredientesAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'costo',
        'creado',
    ]
    search_fields = ['nombre']


class CantidadAdmin(admin.ModelAdmin):
    list_display = [
        'tipo',
        'cantidad',
    ]

admin.site.register(models.Ingrediente,IngredientesAdmin)
admin.site.register(models.Producto,ProductoAdmin)