from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoanForm
from .calculations import calculate_loan_results

def loan_calculator(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            down_payment = form.cleaned_data['down_payment']
            residual_payment = form.cleaned_data['residual_payment']
            interest_rate = form.cleaned_data['interest_rate']
            term = form.cleaned_data['term']
            payment_type = form.cleaned_data['payment_type']

            # Расчет результатов
            results = calculate_loan_results(
                amount, down_payment, residual_payment, interest_rate, term, payment_type
            )
            
            # Перенаправление на страницу с результатами
            return redirect(reverse('loan_result') + f"?annuity_payment={results['annuity_payment']}&total_payment={results['total_payment']}&overpayment={results['overpayment']}&total_interest_percentage={results['total_interest_percentage']}")
    else:
        form = LoanForm()

    return render(request, 'calculator/loan_calculator.html', {'form': form})

def loan_result(request):
    # Извлекаем параметры из URL
    annuity_payment = request.GET.get('annuity_payment')
    total_payment = request.GET.get('total_payment')
    overpayment = request.GET.get('overpayment')
    total_interest_percentage = request.GET.get('total_interest_percentage')

    return render(request, 'calculator/loan_result.html', {
        'annuity_payment': annuity_payment,
        'total_payment': total_payment,
        'overpayment': overpayment,
        'total_interest_percentage': total_interest_percentage,
    })
