from unittest.util import _MAX_LENGTH
from django.db import models

class Carteira(models.Model):
    nome_carteira = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nome_carteira

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=256)
    percentual_alocacao = models.FloatField()
    carteira = models.ForeignKey(Carteira, related_name='categorias', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome_categoria

    