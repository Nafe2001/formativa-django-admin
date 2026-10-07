from django.contrib import admin
from .models import Destino, Paquete

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'pais', 'descripcion', )
    list_filter = ( 'pais', )
    search_fields = ( 'nombre', 'descripcion' )

@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'destino', 'edad' )
    list_filter = ( 'destino', )
    search_fields = ( 'nombre', )

