from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category
from .forms import ContactForm
#classe principal generica
from django.views.generic import View,TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy

#model user do django
User = get_user_model()

# Create your views here.
"""função que recebe uma request e devolve HttpResponse"""
class IndexView(TemplateView):
    # metodo da view
    template_name = 'index.html'
    #metodo para adicionar o contexto
    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['description'] = 'Testando o foorloop do Django','e aprendendo tambem sobre o','if e foorloop que contem','o controle do laço'
        context['title'] = 'Django E-commerce'
        return context

index = IndexView.as_view()


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    #sempre testar se form é valido
    if form.is_valid():
        form.send_mail()
        success = True
        form = ContactForm()
    context = {
        'form': form,
        'success': success,
    }
    return render(request,'contact.html',context)
