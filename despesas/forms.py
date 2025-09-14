from django import forms
from .models import Categoria, Despesa

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['descricao', 'valor', 'categoria', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        valor = cleaned_data.get("valor")
        if valor is None or valor <= 0:
            raise forms.ValidationError("O valor deve ser um número positivo.")
        return cleaned_data