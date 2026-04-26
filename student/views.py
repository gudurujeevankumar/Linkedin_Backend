from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def stu_details(request):
    roll = "22P11A0534"
    name = "Jeevan Kumar"
    age = 21

    data = f"Roll: {roll}, Name: {name}, Age: {age}"

    return HttpResponse(data)

def insert(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        branch = request.POST.get('branch')

        return HttpResponse(
            f"Received -> Roll: {roll}, Name: {name}, Age: {age}, Email: {email}, Branch: {branch}"
        )

    return render(request, 'insert.html')