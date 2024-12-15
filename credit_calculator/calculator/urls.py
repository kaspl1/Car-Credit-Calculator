from django.urls import path
from . import views

urlpatterns = [
    path('', views.loan_calculator, name='loan_calculator'),  # Главная страница калькулятора
    path('result/', views.loan_result, name='loan_result'),   # Страница с результатами
]