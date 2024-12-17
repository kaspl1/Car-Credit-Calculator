
from .forms import LoanForm
from .calculations import calculate_loan_results
from .models import CreditHistory
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def loan_calculator(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            # Получение данных из формы
            amount = form.cleaned_data['amount']
            down_payment = form.cleaned_data['down_payment']
            residual_payment = form.cleaned_data['residual_payment']
            interest_rate = form.cleaned_data['interest_rate']
            term = form.cleaned_data['term']
            payment_type = form.cleaned_data['payment_type']

            # Выполнение расчета
            results = calculate_loan_results(
                amount, down_payment, residual_payment, interest_rate, term, payment_type
            )

            # Сохранение результатов в модели
            CreditHistory.objects.create(
                user=request.user,
                amount=amount,
                interest_rate=interest_rate,
                term=term,
                monthly_payment=results['annuity_payment'],
                total_payment=results['total_payment'],
                overpayment=results['overpayment']
            )

            return redirect(f"{reverse('loan_result')}?annuity_payment={results['annuity_payment']}&total_payment={results['total_payment']}&overpayment={results['overpayment']}&total_interest_percentage={results['total_interest_percentage']}")
    else:
        form = LoanForm()

    return render(request, 'calculator/loan_calculator.html', {'form': form})

def loan_result(request):
    # Извлекаем параметры из URL
    annuity_payment = request.GET.get('annuity_payment')
    total_payment = request.GET.get('total_payment')
    overpayment = request.GET.get('overpayment')
    total_interest_percentage = request.GET.get('total_interest_percentage')

    # Если данные не передаются, это может быть причиной
    print(
        f"Annuity: {annuity_payment}, Total: {total_payment}, Overpayment: {overpayment}, Percentage: {total_interest_percentage}")
    # Передаем данные в шаблон
    return render(request, 'calculator/loan_result.html', {
        'annuity_payment': annuity_payment,
        'total_payment': total_payment,
        'overpayment': overpayment,
        'total_interest_percentage': total_interest_percentage,
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('loan_calculator')  # перенаправление на домашнюю страницу
    else:
        form = AuthenticationForm()
    return render(request, 'calculator/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # перенаправление на страницу логина
    else:
        form = UserCreationForm()
    return render(request, 'calculator/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def credit_history(request):
    credit_list = CreditHistory.objects.filter(user=request.user)
    return render(request, 'calculator/credit_history.html', {'credit_list': credit_list})