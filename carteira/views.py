from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Carteira
from .forms import CarteiraForm

class ListaCarteiraView(ListView):
    model = Carteira
    queryset = Carteira.objects.all().order_by('nome_carteira')

class CarteiraCreateView(CreateView):
    model = Carteira
    form_class = CarteiraForm
    success_url = '/carteiras/'