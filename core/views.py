from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category

# Create your views here.
"""função que recebe uma request e devolve HttpResponse"""
def index(request):
    text = ['Testando o foorloop do Django','e aprendendo tambem sobre o','if e foorloop que contem','o controle do laço']
    context = {'title':'Django E-commerce',
                'description':text,
                }
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')
