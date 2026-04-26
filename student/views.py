from django.shortcuts import render, redirect, get_object_or_404
from .models import StuDetails

def home(request):
    return render(request, 'home.html')

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

def update_stu(request, id):
    student = get_object_or_404(StuDetails, id=id)
    if request.method == 'POST':
        student.roll = request.POST.get('roll')
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.branch = request.POST.get('branch')
        student.save()
        return redirect('all_data')
    return render(request, 'update.html', {'student': student})

def delete_stu(request, id):
    student = get_object_or_404(StuDetails, id=id)
    student.delete()
    return redirect('all_data')
