from django.http.request import QueryDict
from django import http
from django.shortcuts import render, HttpResponse
from AppCoder.models import Curso, Profesor
from django.http import HttpResponse
from AppCoder.forms import CursoForm, ProfeForm

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
        form= CursoForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            comision= info["comision"]
            curso= Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request, "Appcoder/inicio.html")
        
    else:
        form= CursoForm()

    return render(request, "Appcoder/cursoFormulario.html", {"formulario":form})

def profeFormulario(request):

    if request.method=="POST":
        form= ProfeForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request, "Appcoder/inicio.html")
    else:
        form= ProfeForm()
        return render(request, "Appcoder/profeform.html", {"formulario":form})
        
def busquedaComision(request):

    return render(request, "Appcoder/busquedaComision.html")

def buscar(request):
    if request.GET["comision"]:
        comi= request.GET["comision"]
        cursos= Curso.objects.filter(comision__icontains=comi)
        return render(request, "Appcoder/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "Appcoder/busquedaComision.html", {"error":"No se ingreso ninguna comision"})

def leerprofesores(request):
    profesores= Profesor.objects.all()
    return render(request, "Appcoder/leerprofesores.html", {"profesores":profesores})

def eliminarProfesor(request, nombre_profesor):
    profe= Profesor.objects.get(nombre=nombre_profesor)
    profe.delete()
    profesores= Profesor.objects.all()
    return render(request, "Appcoder/leerprofesores.html", {"profesores":profesores})

def editarProfesor(request, nombre_profesor):
    profe= Profesor.objects.get(nombre=nombre_profesor)
    if request.method=="POST":
        form= ProfeForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            profe.nombre= info["nombre"]
            profe.apellido= info["apellido"]
            profe.email= info["email"]
            profe.profesion= info["profesion"]
            profe.save()
            return render(request, "Appcoder/inicio.html")
    else:
        form= ProfeForm(initial={"nombre":profe.nombre, "apellido":profe.apellido, "email":profe.email, "profesion":profe.profesion})
    return render(request, "Appcoder/editarProfesor.html", {"formulario":form, "nombre_profesor":nombre_profesor})




    #respuesta= f"estoy buscando la comision : {comision}"
    #return HttpResponse(respuesta)


"""
def cursoFormulario(request):

    if (request.method=="POST"):

        nombre= request.POST.get("curso")
        comision= request.POST.get("comision")
        curso = Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, "Appcoder/inicio.html")

    return render(request, "Appcoder/cursoFormulario.html")
    """