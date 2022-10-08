from django.http import HttpResponse, Http404
from django.http.response import HttpResponseNotAllowed
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Carteira, Categoria
from .forms import CarteiraForm, CategoriaForm

class ListaCarteiraView(ListView):
    model = Carteira
    queryset = Carteira.objects.all().order_by('nome_carteira')

class CarteiraCreateView(CreateView):
    model = Carteira
    form_class = CarteiraForm
    success_url = '/carteiras/'

class CarteiraUpdateView(UpdateView):
    model = Carteira
    form_class = CarteiraForm
    success_url = '/carteiras/'    

class CarteiraDeleteView(DeleteView):
    model = Carteira
    success_url = '/carteiras/'

def categorias(request, pk_carteira):
    categorias = Categoria.objects.filter(carteira=pk_carteira)
    return render(request, 'categoria/categoria_list.html', {'categorias': categorias, 'pk_carteira': pk_carteira})

def categoria_novo(request, pk_carteira):
    form = CategoriaForm()
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.carteira_id = pk_carteira;
            return redirect(reverse('carteira.categorias', args=[pk_carteira]))
    return render(request, 'categoria/categoria_form.html', {'form': form})

def categoria_editar(request, pk_carteira, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(instance=categoria)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect(reverse('carteira.categorias', args=[pk_carteira]))

    return render(request, 'categoria/categoria_form.html', {'form': form})

def categoria_remover(request, pk_carteirao, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect(reverse('pessoa.contatos', args=[pk_carteirao]))    