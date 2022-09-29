from django.contrib import admin
from .models import Provincia, Distrito,Gestante

@admin.register(Gestante)
class GestanteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone')
    search_fields = ('name', 'email')
    list_filter = ('gender',)

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cod_prov','desc_prov')

@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cod_dist','desc_dist')