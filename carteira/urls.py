from django.urls import path
from .views import ListaCarteiraView, CarteiraCreateView, CarteiraUpdateView, CarteiraDeleteView
from . import views

urlpatterns = [
    path('', ListaCarteiraView.as_view(), name='carteira.index'),
    path('novo/', CarteiraCreateView.as_view(), name='carteira.novo'),
    path('<int:pk>/editar', CarteiraUpdateView.as_view(), name='carteira.editar'),
    path('<int:pk>/remover', CarteiraDeleteView.as_view(), name='carteira.remover'),
    path('<int:pk_carteira>/categorias', views.categorias, name='carteira.categorias'),
     path('<int:pk_carteira>/categoria/novo/',
         views.categoria_novo, name='categoria.novo'),
    path('<int:pk_carteira>/categoria/<int:pk>/editar',
         views.categoria_editar, name='categoria.editar'),
    path('<int:pk_carteira>/categoria/<int:pk>/remover',
         views.categoria_remover, name='categoria.remover'),
]