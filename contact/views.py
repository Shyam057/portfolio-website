from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages
from core.models import About

def contact(request):
    about = About.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    context = {
        'about': about,
    }
    return render(request, 'contact/contact.html', context)