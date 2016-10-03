from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Nome',max_length=100)
    slug = models.SlugField('Identificador',max_length=100)
    created = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em',auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        '''se a ordem for decres colocar - na frente do campo'''
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category',kwargs={'slug':self.slug})

class Product(models.Model):
    name = models.CharField(verbose_name='Nome',max_length=100)
    slug = models.SlugField('Identificador',max_length=100)
    '''um produto tem varias categorias'''
    category = models.ForeignKey('catalog.Category',verbose_name='Categoria')
    description = models.TextField('Descrição',blank=True)
    price = models.DecimalField('Preço',decimal_places=2,max_digits=8)
    created = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em',auto_now=True)
    image = models.ImageField(
            upload_to='catalog/images', verbose_name='Imagem',
            null=True, blank=True
    )

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        '''se a ordem for decres colocar - na frente do campo'''
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product',kwargs={'slug':self.slug})
