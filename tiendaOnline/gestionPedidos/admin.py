from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono")
    search_fields = ("nombre", "telefono", "direccion")


class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("nombre", "seccion", "precio")
    search_fields = ("nombre", "seccion", "precio")
    list_display = ("nombre", "seccion", "precio")


class pedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")
    search_fields = ("fecha",)
    list_filter = ("fecha",)
    date_hierarchy = "fecha"


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, pedidosAdmin)
