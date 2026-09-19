from django.contrib import admin
from .models import Department, Employee

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("dept_name", "dept_location")
    search_fields = ("dept_name",)
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "full_name", "email", "designation", "salary", "joining_date", "is_active", "department", "manager"]
    search_fields = ["first_name", "last_name", "email", "designation"]
    list_filter = ["is_active", "department", "manager"]
    list_editable = ["is_active"]
    list_display_links = ["id", "first_name", "last_name"]
    ordering = ["-id"]
        
