from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm, DocumentForm
from .models import Application

def admissions_home(request):
    return render(request, 'admissions/admissions_home.html')

def admission_process(request):
    return render(request, 'admissions/admission_process.html')

def apply(request):
    if request.method == 'POST':
        app_form = ApplicationForm(request.POST)
        doc_form = DocumentForm(request.POST, request.FILES)
        if app_form.is_valid() and doc_form.is_valid():
            application = app_form.save()
            document = doc_form.save(commit=False)
            document.application = application
            document.save()
            # Use namespaced URL here
            return redirect('admissions:application_status', application_id=application.id)
    else:
        app_form = ApplicationForm()
        doc_form = DocumentForm()
    return render(request, 'admissions/apply.html', {'app_form': app_form, 'doc_form': doc_form})

def application_status(request, application_id=None):
    application = None
    if application_id:
        application = get_object_or_404(Application, id=application_id)
    return render(request, 'admissions/status.html', {'application': application})
