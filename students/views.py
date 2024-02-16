import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm
from .models import Students

def index(request):
    students = Students.objects.all()
    return render(request, 'students/index.html', {'students': students})

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
        
    return render(request, 'students/add.html', {
        'form': form
    })

def view_student(request, id):
    student = Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def edit(request, id):
    student = get_object_or_404(Students, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            # Check if a new profile picture is provided
            if 'profile_picture' in request.FILES:
                # Delete the previous profile picture if it exists
                if student.profile_picture:
                    old_picture_path = os.path.join(settings.MEDIA_ROOT, str(student.profile_picture))
                    if os.path.exists(old_picture_path):
                        os.remove(old_picture_path)
                # Save the new profile picture
                student.profile_picture = request.FILES['profile_picture']
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        student = Students.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))