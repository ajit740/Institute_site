from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EnrollmentForm
from .models import Enrollment  # If saving in DB

def enroll_course(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            Enrollment.objects.create(
                course_name=form.cleaned_data['course_name'],
                student_name=form.cleaned_data['student_name'],
                student_email=form.cleaned_data['student_email'],
                student_phone=form.cleaned_data['student_phone'],
            )
            messages.success(request, f"Successfully enrolled in {form.cleaned_data['course_name']}!")
            return redirect('courses:courses')  # ✅ FIXED
        else:
            messages.error(request, "Please correct the errors below.")
    return redirect('courses:courses')  # ✅ FIXED


from django.shortcuts import render

def courses_home(request):
    return render(request, 'courses/courses.html')
