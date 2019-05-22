from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserCreationForm
from .models import Alumno,Asignatura,Profesor
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def cargarInicio(request):
    return render(request, 'pagina/base.html')

def cargarLogin(request):
    return render(request, 'pagina/login.html')

def cargarRegistro(request):
	return render(request, 'pagina/registro.html')

def cargarDocentes(request):
    return render(request, 'pagina/docentes.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/pagina/inicio')
    else:
        form = UserCreationForm()
    return render(request, 'pagina/registro.html', {'form': form})



def cargarDocentes(request):  
    #Obtenemos los departamentos ordenados de manera descendente.
    #[Z-A] Se antepone el signo menos (-)
    cargarDocentes = Profesor.objects.all()

    #Cargamos el archivo index.html que se encuentra en la carpeta 'templates'
    template = loader.get_template('pagina/docentes.html')

    #Creamos el nombre 'deptos' para reutilizarlo en el archivo 'index.html'
    context = {
        'docentes': cargarDocentes,
    }

    #Invocamos la página de respuesta 'index.html'
    return HttpResponse(template.render(context, request))

def cargarAsignaturas(request):  
    #Obtenemos los departamentos ordenados de manera descendente.
    #[Z-A] Se antepone el signo menos (-)
    cargarAsignaturas = Asignatura.objects.all()

    #Cargamos el archivo index.html que se encuentra en la carpeta 'templates'
    template = loader.get_template('pagina/asignaturas.html')

    #Creamos el nombre 'deptos' para reutilizarlo en el archivo 'index.html'
    context = {
        'asignaturas': cargarAsignaturas,
    }

    #Invocamos la página de respuesta 'index.html'
    return HttpResponse(template.render(context, request))