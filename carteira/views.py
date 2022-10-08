from django.shortcuts import render
from django.views.generic import ListView
from .models import Carteira

class ListaCarteiraView(ListView):
    model = Carteira
    queryset = Carteira.objects.all().order_by('nome_carteira')