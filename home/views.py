from django.shortcuts import render , HttpResponse , redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login , authenticate

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_data = Contact(name=name, email=email, subject = subject , message= message) 
        contact_data.save()
        
        return redirect("/")
    return render(request , "index.html")

# def contact(request):
    # if request.method == "POST":
    #     fname = request.POST.get('name')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')

    #     contact_data = Contact(name=fname, email=email, subject = subject , message=message)
    #     contact_data.save()
        
    #     return redirect("index.html")
    




# def home(request):
#     return render(request , "index.html")

