from django.shortcuts import render, redirect
from b.forms import PetInterestForm
from django.http import HttpResponse

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


def contact(request):
    if request.method == 'POST':
        form = PetInterestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PetInterestForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
   return HttpResponse('Success!')



