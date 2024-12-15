class LoanCalculator:
    def __init__(self, amount, down_payment, residual_payment, interest_rate, term, payment_type):
        self.amount = amount  # Сумма кредита
        self.down_payment = down_payment  # Первоначальный взнос
        self.residual_payment = residual_payment  # Остаточный платеж
        self.interest_rate = interest_rate  # Процентная ставка
        self.term = term  # Срок кредита (в месяцах)
        self.payment_type = payment_type  # Тип платежей: аннуитетные или дифференцированные

        # Сумма кредита после первоначального взноса
        self.loan_amount = self.amount - self.down_payment - self.residual_payment

    def calculate_annuity_payment(self):
        """Расчет аннуитетного ежемесячного платежа"""
        r = self.interest_rate / 100 / 12  # Месячная процентная ставка
        n = self.term  # Количество месяцев

        # Формула для аннуитетного платежа
        if r != 0:
            annuity_payment = self.loan_amount * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
        else:
            annuity_payment = self.loan_amount / n  # Без процентов, если ставка 0%
        
        return annuity_payment

    def calculate_total_payment(self):
        """Общая сумма выплат, исключая остаточный платеж"""
        annuity_payment = self.calculate_annuity_payment()
        total_payment = annuity_payment * self.term  # Общая сумма выплат (без остаточного платежа)
        return total_payment

    def calculate_total_with_residual(self):
        """Общая сумма выплат с учетом остаточного платежа"""
        total_payment = self.calculate_total_payment() + self.residual_payment
        return total_payment

    def calculate_overpayment(self):
        """Расчет переплаты"""
        total_with_residual = self.calculate_total_with_residual()
        overpayment = total_with_residual - self.loan_amount
        return overpayment

    def calculate_total_interest(self):
        """Расчет общей суммы процентов"""
        total_payment = self.calculate_total_payment()
        total_interest = total_payment - self.loan_amount  # Сумма процентов = общая сумма выплат - сумма кредита
        return total_interest

    def get_results(self):
        """Получаем все результаты расчёта"""
        annuity_payment = self.calculate_annuity_payment()
        total_payment = self.calculate_total_payment()
        overpayment = self.calculate_overpayment()
        total_interest = self.calculate_total_interest()

        # Округляем результаты до двух знаков после запятой
        annuity_payment = round(annuity_payment, 2)
        total_payment = round(total_payment, 2)
        overpayment = round(overpayment, 2)
        total_interest = round(total_interest, 2)

        return {
            "annuity_payment": annuity_payment,
            "total_payment": total_payment,
            "overpayment": overpayment,
            "total_interest": total_interest
        }
