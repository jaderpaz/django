from django.shortcuts import render
from django.http import HttpResponse
from .models import Estoque


def cadastro(request):
    return render(request, 'cadastro.html')
def listar_produto(request):
    lista_estoque = Estoque.objects.all()
    return render(request, 'lista_produto.html', {'lista_produto': lista_estoque})
