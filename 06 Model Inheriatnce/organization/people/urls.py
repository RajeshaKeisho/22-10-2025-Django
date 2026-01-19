from django.urls import path
from .views import EmployeeListView, CustomerListView

urlpatterns = [
    path('employees/', EmployeeListView.as_view()),
    path('customers/', CustomerListView.as_view()),
]
