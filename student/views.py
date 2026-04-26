from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def stu_details(request):
    roll = "22P11A0534"
    name = "Jeevan Kumar"
    age = 21

    data = f"Roll: {roll}, Name: {name}, Age: {age}"

    return HttpResponse(data)
