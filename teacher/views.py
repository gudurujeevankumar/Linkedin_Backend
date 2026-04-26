from django.shortcuts import render, redirect, get_object_or_404
from .models import TeachDetails

def insert(request):
    if request.method == 'POST':
        empid = request.POST.get('empid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        TeachDetails.objects.create(
            empid=empid,
            name=name,
            email=email,
            subject=subject
        )
        return redirect('teacher:all_teachers')
    return render(request, 'teacher/insert.html')

def all_data(request):
    teachers = TeachDetails.objects.all()
    return render(request, 'teacher/data.html', {'teachers': teachers})

def update_teach(request, id):
    teacher = get_object_or_404(TeachDetails, id=id)
    if request.method == 'POST':
        teacher.empid = request.POST.get('empid')
        teacher.name = request.POST.get('name')
        teacher.email = request.POST.get('email')
        teacher.subject = request.POST.get('subject')
        teacher.save()
        return redirect('teacher:all_teachers')
    return render(request, 'teacher/update.html', {'teacher': teacher})

def delete_teach(request, id):
    teacher = get_object_or_404(TeachDetails, id=id)
    teacher.delete()
    return redirect('teacher:all_teachers')
