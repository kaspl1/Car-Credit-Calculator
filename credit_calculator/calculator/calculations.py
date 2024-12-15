def calculate_loan_results(amount, down_payment, residual_payment, interest_rate, term, payment_type):
    # Расчет основной суммы кредита
    principal = amount - down_payment - residual_payment
    monthly_interest_rate = interest_rate / 100 / 12
    
    if payment_type == 'annuity':
        # Аннуитетные платежи
        annuity_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -term)
        total_payment = annuity_payment * term
        overpayment = total_payment - principal
    else:  # Дифференцированные платежи
        # Дифференцированные платежи
        annuity_payment = principal / term + (principal * monthly_interest_rate)
        total_payment = annuity_payment * term
        overpayment = total_payment - principal

    # Общие проценты в % от суммы кредита
    total_interest = overpayment
    total_interest_percentage = (total_interest / principal) * 100

    return {
        'annuity_payment': round(annuity_payment, 2),
        'total_payment': round(total_payment, 2),
        'overpayment': round(overpayment, 2),
        'total_interest_percentage': round(total_interest_percentage, 2),
    }
