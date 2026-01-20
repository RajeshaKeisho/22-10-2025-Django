from django.shortcuts import render
from django.db.models import Avg, Count
from django.db.models import Q
from .models import Employee, Department
from django.db import connection

# Create your views here.
def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/all.html', {"employees":employees})

def high_salary_employees(request):
    high_salary_employees = Employee.objects.filter(salary__gt=55000)
    return render(request, 'employees/high_salary_employees.html', {'high_salary_employees': high_salary_employees})

def avg_salary(request):
    avg_salary = Employee.objects.aggregate(avg_salary=Avg('salary'))
    return render(request, 'employees/avg_salary.html', {'avg_salary': avg_salary})


def salary_or_name_contains(request):
    employees = Employee.objects.filter(Q(name__icontains='John') | Q(salary__gte=50000))
    return render(request, 'employees/employee_list.html', {'employees': employees})

def high_paid_employees(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, name, salary
            FROM employees_employee
            WHERE salary >= 50000
        """)
        columns = [col[0] for col in cursor.description]
        employee_objects = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return render(request, 'employees/highest_paid_employees.html', {
        'employee_objects': employee_objects
    })