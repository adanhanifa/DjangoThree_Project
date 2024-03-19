from django.http import JsonResponse
from django.shortcuts import render
from myapplication.models import Employees
from myapplication.serializers import EmployeesSerializer


# Create your views here.
def employeesview(request):
    employee = Employees.objects.all()
    serializer = EmployeesSerializer(employee, many=True)
    return JsonResponse({"employee":serializer.data}, safe=False)
