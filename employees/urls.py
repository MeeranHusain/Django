from django.urls import include, path
from . import views 


# Decided which URL patterns to include in the employees app
# Created URL pattern in the main urls.py, and forwarded the request to the employees app's urls.py
# Created the view in the employees app to handle the request and render the employee_detail.html template
# Created the template to display the employee details

urlpatterns = [
    path('<int:id>/', views.employee_detail, name = 'employee_detail'),
    path('add/', views.employee_add, name = 'employee_add'),
]
