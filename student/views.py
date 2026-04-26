from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StuDetails

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

        StuDetails.objects.create(
            roll=roll,
            name=name,
            age=age,
            email=email,
            branch=branch
        )

        return redirect('all_data')
    
    return render(request, 'insert.html')



def all_data(request):

    students = StuDetails.objects.all()

    return render(request, 'data.html', {'students': students})