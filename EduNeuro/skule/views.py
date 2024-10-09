from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Course, Enrollment
from .forms import UserRegistrationForm, EnrollmentForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'skule/course_list.html', {'courses': courses})

def enroll(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.user = request.user
            enrollment.save()
            return redirect('course_list')
    else:
        form = EnrollmentForm()
    return render(request, 'skule/enroll.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'skule/register.html', {'form': form})

