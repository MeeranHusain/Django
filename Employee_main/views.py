
from django.http import HttpResponse


def home(request):
    # fetch data from the Employee tables
    return HttpResponse("Welcome to the Employee Dashboard!")