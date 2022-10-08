from django.urls import path
from .views import ListaCarteiraView

urlpatterns = [
    path('', ListaCarteiraView.as_view(), name='carteira.index')
]