from django.db import models

class Carteira(models.Model):
    nome_carteira = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nome_carteira
    