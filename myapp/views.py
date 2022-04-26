import email
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from myapp.models import Contact

# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def service(request):
    return render(request, "service.html")
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name'),
        number=request.POST.get('number'),
        email=request.POST.get('email'),
        cont=request.POST.get('cont'),
        done= Contact(name=name , number=number, email = email, cont = cont , date=datetime.today())
        done.save()



    return render(request, "contact.html")