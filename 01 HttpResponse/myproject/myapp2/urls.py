from django.urls import path
from . import views

urlpatterns = [
    path('morning/', views.morning_message),
    path('noon/', views.noon_message),
    path('evening/', views.evening_message),
    path('message/', views.message),
]
