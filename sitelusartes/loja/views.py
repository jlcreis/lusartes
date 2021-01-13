from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def LojaIndex (request):
    return render (request, 'home.html')

def LojaProdutos (request):
    return render (request, 'produtos.html')
