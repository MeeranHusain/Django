from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {

            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name',
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address',
            }),

            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter designation',
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),

            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary',
                'min': '0',
                'step': '0.01',
            }),

            'joining_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),

            'department': forms.Select(attrs={
                'class': 'form-control',
            }),

            'manager': forms.Select(attrs={
                'class': 'form-control',
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-checkbox',
            }),
        }