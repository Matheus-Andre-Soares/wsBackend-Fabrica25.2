from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Despesa
from .forms import CategoriaForm, DespesaForm
from django.http import JsonResponse
from django.utils import timezone
from .models import TaxaDeCambio
import requests

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'despesas/categoria_list.html', {'categorias': categorias})

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'despesas/categoria_form.html', {'form': form})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'despesas/categoria_form.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'despesas/categoria_confirm_delete.html', {'categoria': categoria})

def despesa_list(request):
    moeda = request.GET.get('moeda', 'USD').upper()  # Usa USD como padrão
    despesas = Despesa.objects.all()

    for despesa in despesas:
        despesa.valor_convertido = despesa.valor_em_moeda(moeda)

    return render(request, 'despesas/despesa_list.html', {'despesas': despesas, 'moeda': moeda})

def despesa_create(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.save()
            return redirect('despesa_list')
    else:
        form = DespesaForm()
    return render(request, 'despesas/despesa_form.html', {'form': form})

def despesa_update(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk)
    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return redirect('despesa_list')
    else:
        form = DespesaForm(instance=despesa)
    return render(request, 'despesas/despesa_form.html', {'form': form})

def despesa_delete(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk)
    if request.method == 'POST':
        despesa.delete()
        return redirect('despesa_list')
    return render(request, 'despesas/despesa_confirm_delete.html', {'despesa': despesa})

def importar_taxas(request):
    url = 'https://open.er-api.com/v6/latest/USD'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        taxas = dados.get('rates', {})
        data_atual = timezone.now().date()

        for moeda, taxa in taxas.items():
            TaxaDeCambio.objects.update_or_create(
                moeda=moeda,
                data=data_atual,
                defaults={'taxa': taxa}
            )

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Failed to retrieve data from API'})

def index(request):
    return render(request, 'despesas/index.html')