from django.shortcuts import get_object_or_404, render
from . models import Department, Employee
from . forms import EmployeeForm 

# Create your views here.

def employee_detail(request, id):
    try:
        # employee = get_object_or_404(Employee, id=id)
        employee = Employee.objects.get(id=id)
        # print(employee)  # for debugging purposes, It's output will be displayed in the console where the Django server is running. it is also called queryset. A queryset is a collection of database queries that can be filtered, ordered, and manipulated to retrieve specific data from the database. In this case, the queryset is used to retrieve the employee object with the specified id from the Employee model.
        context = {
            'employee': employee,
        }
        
        return render(request, 'employee_detail.html', context)
    
    except Employee.DoesNotExist:
        return render(request, '404.html', status=404)
    

def employee_add(request):
    # departments = Department.objects.all()
    # managers = Employee.objects.all()

    # context = {
    #     'departments': departments,
    #     'managers': managers,
    # }
    form = EmployeeForm()
    # print(form)  # for debugging purposes, It's output will be displayed in the console where the Django server is running. it is also called queryset. A queryset is a collection of database queries that can be filtered, ordered, and manipulated to retrieve specific data from the database. In this case, the queryset is used to retrieve the employee object with the specified id from the Employee model.  
    context = {
        'form': form,
    }  
    return render(request, 'employee_add.html', context)