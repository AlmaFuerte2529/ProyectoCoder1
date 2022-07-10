from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.


def curso(self):
    
    curso= Curso(nombre="Django", comision=939393)
    curso.save()
    texto= f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)



def inicio(request):
    return render(request, "Appcoder/inicio.html")

def cursos(request):
    return render(request, "Appcoder/cursos.html")

def profesores(request):
    return render(request, "Appcoder/profesores.html")

def estudiantes(request):
    return render(request, "Appcoder/estudiantes.html")

def entregables(request):
    return render(request, "Appcoder/entregables.html")

def cursoFormulario(request):

    if (request.method=="POST"):

        nombre= request.POST.get("curso")
        comision= request.POST.get("comision")
        curso= Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, "AppCoder/inicio.html")

    return render(request, "Appcoder/cursoFormulario.html")

