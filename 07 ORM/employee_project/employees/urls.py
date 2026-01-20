from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_employees),
    path('highsal/', views.high_salary_employees),
    path('avgsal/', views.avg_salary),
    path('salorname/', views.salary_or_name_contains),
    path('highestpaidemp/', views.high_paid_employees),
]