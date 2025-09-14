from django import template
from despesas.models import TaxaDeCambio
from django.utils import timezone
from decimal import Decimal

register = template.Library()

@register.filter
def valor_em_moeda(valor, moeda_alvo):
    try:
        taxa = TaxaDeCambio.objects.get(moeda=moeda_alvo)
        return valor * taxa.taxa
    except TaxaDeCambio.DoesNotExist:
        return valor