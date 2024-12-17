from django.db import models
from django.contrib.auth.models import User

class CreditHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term = models.IntegerField()
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    overpayment = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Кредит для {self.user.username} на сумму {self.amount}"
