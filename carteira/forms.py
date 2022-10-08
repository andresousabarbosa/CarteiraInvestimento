from dataclasses import fields
from django import forms
from django import forms
from .models import Carteira, Categoria

class CarteiraForm(forms.ModelForm):
    class Meta:
        model = Carteira
        fields = ['nome_carteira']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome_categoria', 'percentual_alocacao']
