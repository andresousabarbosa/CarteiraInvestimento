from dataclasses import fields
from django import forms
from django import forms
from .models import Carteira

class CarteiraForm(forms.ModelForm):
    class Meta:
        model = Carteira
        fields = ['nome_carteira']
