from django.shortcuts import redirect, render

# Create your views here.

def root(request):
    return redirect('/home')

def home(request):
    return render(request, 'core/home.html')

def conciertos(request):
    return render(request, 'core/conciertos.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')
