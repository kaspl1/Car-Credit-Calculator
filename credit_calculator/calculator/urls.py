from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Главная страница калькулятора
    path('result/', views.loan_result, name='loan_result'),   # Страница с результатами
    path('loan_calculator/', views.loan_calculator, name='loan_calculator'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='calculator/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('history/', views.credit_history, name='history'),
]