from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreditCardForm
from .models import CreditCard


def add_card(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = CreditCardForm()

    cards = CreditCard.objects.all()
    return render(request, 'core/card_form.html', {'form': form, 'cards': cards})

def delete_card(request, card_id):
    card = get_object_or_404(CreditCard, id=card_id)
    card.delete()
    return redirect('core:add_card')


def calculate(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_cards')

        if len(selected_ids) < 2 or len(selected_ids) > 5:

            return redirect('core:add_card')

        cards = CreditCard.objects.filter(id__in=selected_ids)

        # TODO: здесь будет логика расчёта переплаты и графика

        return render(request, 'core/result.html', {'cards': cards})

    return redirect('core:add_card')