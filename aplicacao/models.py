from django.db import models
from datetime import datetime

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    salario = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
    dia_pagamento = models.CharField(max_length=2)
    
    
class Gasto(models.Model):
    class Meta:
        ordering = ('data',)
        
    pessoa = models.ForeignKey('Pessoa')
    descricao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
    data = models.DateField(blank=True, default=datetime.today())
