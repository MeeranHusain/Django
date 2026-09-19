
from django.http import HttpResponse
from employees.models import Employee
from django.shortcuts import render

def home(request):
    # fetch data from the Employee tables
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    # print(employees)   # for debugging purposes, It's output will be displayed in the console where the Django server is running.
    return render(request, 'home.html', context)
