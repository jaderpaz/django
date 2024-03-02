from django.shortcuts import render
from django.http import HttpResponse
from .models import CLientes



def index(request):
    return render(request, 'index.html')
def cadastro(request):
    return render(request, 'cadastro.html')
def listar(request):
    lista_clientes = CLientes.objects.all()
    return render(request, 'listar.html', {'lista': lista_clientes})



# Create your views here.
