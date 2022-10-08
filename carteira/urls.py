from django.urls import path
from .views import ListaCarteiraView, CarteiraCreateView, CarteiraUpdateView, CarteiraDeleteView

urlpatterns = [
    path('', ListaCarteiraView.as_view(), name='carteira.index'),
    path('novo/', CarteiraCreateView.as_view(), name='carteira.novo'),
    path('editar/<int:pk>', CarteiraUpdateView.as_view(), name='carteira.editar'),
    path('remover/<int:pk>', CarteiraDeleteView.as_view(), name='carteira.remover'),
]