# contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    admin_info = {
        'address': 'Sector 15, Sonipat,Haryana',
        'phone': '8053856536',
        'email': 'ajit74043@gmail.com',
    }
    return render(request, 'contact/contact.html', {'form': form, 'submitted': submitted, 'admin_info': admin_info})
