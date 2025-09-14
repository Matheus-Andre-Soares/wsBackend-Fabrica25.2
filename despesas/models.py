from decimal import Decimal
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Despesa(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    data = models.DateField()

    def valor_em_moeda(self, moeda):
        taxa = TaxaDeCambio.objects.filter(moeda=moeda).first()
        if taxa:
            taxa_decimal = Decimal(taxa.taxa)
            return self.valor * taxa_decimal
        return self.valor

class TaxaDeCambio(models.Model):
    moeda = models.CharField(max_length=10)
    taxa = models.DecimalField(max_digits=12, decimal_places=8)
    data = models.DateField()