from django.db import models

class Carteira(models.Model):
    nome_carteira = models.CharField(max_length=256)
    