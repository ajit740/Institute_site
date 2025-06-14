# home/views.py
from django.shortcuts import render
from datetime import datetime

def index(request):
    blog_posts = [
        {
            'title': 'AI Revolutionizing Healthcare Diagnostics',
            'slug': 'ai-revolutionizing-healthcare-diagnostics',
            'published_date': datetime(2025, 5, 1),
            'summary': 'AI is transforming healthcare by enabling faster and more accurate diagnostic tools.',
            'image': None
        },
        {
            'title': 'Top 5 Cybersecurity Trends to Watch in 2025',
            'slug': 'top-5-cybersecurity-trends-2025',
            'published_date': datetime(2025, 4, 20),
            'summary': 'Cyber threats are evolving rapidly. Learn about the latest trends.',
            'image': None
        },
        {
            'title': 'Modern Web Development: Embracing Jamstack',
            'slug': 'modern-web-development-embracing-jamstack',
            'published_date': datetime(2025, 3, 30),
            'summary': 'Jamstack architecture is redefining how developers build fast and secure websites.',
            'image': None
        },
    ]
    return render(request, 'home/index.html', {'blog_posts': blog_posts})

def about(request):
    return render(request, 'home/about.html')

def faqs(request):
    return render(request, 'home/faqs.html')


from django.shortcuts import render

def apply_view(request):
    return render(request, 'home/apply.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm

def apply_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('apply')  # Ensure 'apply' is the name of the URL
    else:
        form = ApplicationForm()
    return render(request, 'home/apply.html', {'form': form})
