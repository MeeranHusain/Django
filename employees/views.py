from django.shortcuts import get_object_or_404, render
from . models import Employee

# Create your views here.

def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    print(employee)  # for debugging purposes, It's output will be displayed in the console where the Django server is running. it is also called queryset. A queryset is a collection of database queries that can be filtered, ordered, and manipulated to retrieve specific data from the database. In this case, the queryset is used to retrieve the employee object with the specified id from the Employee model.
    context = {
        'employee': employee,
    }
    
    return render(request, 'employee_detail.html', context)