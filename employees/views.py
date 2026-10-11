from django.shortcuts import get_object_or_404, redirect, render
from . models import Department, Employee
from . forms import EmployeeForm 

# Create your views here.

# View to display the details of a specific employee based on their ID. It retrieves the employee object from the database and renders the 'employee_detail.html' template with the employee's information. If the employee does not exist, it renders a 404 error page.
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
    
    
# Add Employee
def employee_add(request):
    # departments = Department.objects.all()
    # managers = Employee.objects.all()

    # context = {
    #     'departments': departments,
    #     'managers': managers,
    # }
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_detail', id=employee.id)
    
    else:
        form = EmployeeForm() 
            
    context = {
        'form': form,
        'page_title': 'Add Employee',
        'button_text': 'Add Employee',
    }  
    return render(request, 'employee_form.html', context)


# Edit Employee
def employee_edit(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES,instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_detail', id=employee.id)
    
    else:
        form = EmployeeForm(instance=employee)

    context = {
        'form': form,
        'employee': employee,
        'page_title': 'Edit Employee',
        'button_text': 'Save Changes',
    }

    return render(request, 'employee_form.html', context)
