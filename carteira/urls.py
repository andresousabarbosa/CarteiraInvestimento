from django.urls import path
from .views import ListaCarteiraView, CarteiraCreateView

urlpatterns = [
    path('', ListaCarteiraView.as_view(), name='carteira.index'),
    path('novo/', CarteiraCreateView.as_view(), name='carteira.novo')
]