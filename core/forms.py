from django import forms
from .models import CreditCard

class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['name', 'credit_limit', 'interest_rate', 'current_debt', 'min_payment_percent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тинькофф, Сбер, Альфа...'}),
            'credit_limit': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'current_debt': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'min_payment_percent': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        labels = {
            'name': 'Название карты',
            'credit_limit': 'Кредитный лимит (₽)',
            'interest_rate': 'Годовая ставка (%)',
            'current_debt': 'Текущий долг (₽)',
            'min_payment_percent': 'Мин. платёж (% от долга)',
        }