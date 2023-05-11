from django.shortcuts import render
from .models import About, Contacts

def about(request):
    about = About.objects.all()
    contacts = Contacts.objects.all()
    context = {'about':about, 'contacts':contacts}
    return render(request, 'about/about.html', context)