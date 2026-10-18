from django.shortcuts import get_object_or_404, redirect, render
from . models import Department, Employee
from . forms import EmployeeForm 
from django.http import JsonResponse
from django.views.decorators.http import require_POST


# Create your views here.

# View to display the details of a specific employee based on their ID. It retrieves the employee object from the database and renders the 'employee_detail.html' template with the employee's information. If the employee does not exist, it renders a 404 error page.
def employee_detail(request, id):
    # try:
    employee = get_object_or_404(Employee, id=id, is_deleted=False)  # Fetch the employee object with the given ID, ensuring it is not marked as deleted.
    
    # employee = Employee.objects.get(id=id)
    # print(employee)  # for debugging purposes, It's output will be displayed in the console where the Django server is running. it is also called queryset. A queryset is a collection of database queries that can be filtered, ordered, and manipulated to retrieve specific data from the database. In this case, the queryset is used to retrieve the employee object with the specified id from the Employee model.
    context = {
        'employee': employee,
    }
    
    return render(request, 'employee_detail.html', context)
    
    # except Employee.DoesNotExist:
    #     return render(request, '404.html', status=404)
    
    
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
    employee = get_object_or_404(Employee, id=id, is_deleted=False)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)

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


# Soft Delete Employee
# def employee_delete(request, id):
#     employee = get_object_or_404(Employee, id=id, is_deleted=False)

#     if request.method == 'POST':
#         employee.is_deleted = True
#         employee.save(update_fields=['is_deleted'])
#         return redirect('home')

#     return render(request,'employee_confirm_delete.html',{'employee': employee})



# Soft Delete Employee using AJAX
@require_POST
def employee_delete(request, id):

    employee = get_object_or_404(Employee, id=id, is_deleted=False)
    employee.is_deleted = True
    employee.save(update_fields=['is_deleted'])

    return JsonResponse({
        'success': True,
        'message': 'Employee deleted successfully.'
    })
    
