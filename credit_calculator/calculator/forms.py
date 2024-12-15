from django import forms

class LoanForm(forms.Form):
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
    down_payment = forms.DecimalField(max_digits=12, decimal_places=2)
    residual_payment = forms.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = forms.DecimalField(max_digits=5, decimal_places=2)
    term = forms.IntegerField(min_value=1)
    payment_type = forms.ChoiceField(choices=[('annuity', 'Аннуитетные'), ('differentiated', 'Дифференцированные')])
