from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TeachDetails

# Create your views here.


def teacher_details(request):
    empid = "EMP001"
    name = "Dr. John Smith"
    email = "john.smith@school.edu"

    data = f"Employee ID: {empid}, Name: {name}, Email: {email}"

    return HttpResponse(data)


def insert(request):
    if request.method == 'POST':
        empid = request.POST.get('empid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        teacher = TeachDetails(empid=empid, name=name, email=email, subject=subject)
        teacher.save()
        return redirect('all_teachers')
    return render(request, 'teacher/insert.html')


def all_data(request):
    teachers = TeachDetails.objects.all()
    return render(request, 'teacher/data.html', {'teachers': teachers})
