from .models import Category


#semelhante ao session do jsf onde o dicionario fica disponivel por toda aplicação
#necessario adicionar no settings
def categories(request):
    return{
        'categories':Category.objects.all()
    }
