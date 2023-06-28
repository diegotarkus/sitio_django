from django.shortcuts import render, HttpResponse, redirect, reverse
from crud.models import Concierto, Recinto, Artista
from .models import *
from .forms import *

# Create your views here.

def root(request):
    return redirect('/home')

def home(request):
    return render(request, 'core/home.html')

def conciertos(request):
    context = {'conciertos': Concierto.objects.all()}
    return render(request,'core/conciertos.html',context)

def informacion(request, concierto_id):
    concierto = Concierto.objects.get(idConcierto=concierto_id)
    if concierto:
        context = {'concierto':concierto}
        return render(request,'core/informacion.html',context)

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST, request.FILES)
        if form.is_valid():
            id = form.cleaned_data.get('id')
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            correo = form.cleaned_data.get('correo')
            telefono = form.cleaned_data.get('telefono')
            mensaje = form.cleaned_data.get('mensaje')
            obj = DatosContacto.objects.create(
                id = id,
                nombre = nombre,
                apellido = apellido,
                correo = correo,
                telefono = telefono,
                mensaje = mensaje
            )
            obj.save()
            return redirect(reverse('contact')+ '?OK')
        else:
            return redirect(reverse('contact')+ '?FAIL')
    else:
        form = ContactoForm
    return render(request,'core/contact.html',{'form':form})

def api(request):
    return render(request, 'core/api.html')

def about(request):
    return render(request, 'core/about.html')
