from django.contrib import admin
from .models import Carteira, Categoria

class CarteiraAdmin(admin.ModelAdmin):
    list_display = [
        'nome_carteira'
    ]
    search_fields = [
        'nome_carteira'
    ]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'carteira',
        'nome_categoria',
        'percentual_alocacao'
    ]
    list_filter = [
        'carteira',
    ]



# Register your models here.
admin.site.register(Carteira, CarteiraAdmin)
admin.site.register(Categoria, CategoriaAdmin)


