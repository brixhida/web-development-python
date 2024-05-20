from django.shortcuts import render


def home(request):
    return render(request, "pawportal.html")

def about(request):
    return render(request, "aboutpaw.html")


def contact(request):
    return render(request, "contact.html")


def adopt(request):
    return render(request, "adoptnow.html")


def pets(request):
    return render(request, "pets.html")

def form(request):
    create_contact.objects.create(
        
    )

