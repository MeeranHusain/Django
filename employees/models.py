from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=30)
    dept_location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.dept_name} - {self.dept_location}"
    
    
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    manager = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
        
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.designation})"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
