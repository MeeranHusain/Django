from django.shortcuts import render

# Create your views here.

def employee_detail(request, id):
    return render(request, 'employee_detail.html', {'id': id})