from django.shortcuts import render
from .models import Message

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        Message.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message'],
        )
    return render(request, 'contact.html')