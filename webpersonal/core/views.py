from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hola que ase</h1>")

