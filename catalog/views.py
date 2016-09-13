# codding=utf-8
from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from django.views import generic
# Create your views here.


class ProductListView(generic.ListView):
    template_name = 'catalog/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5



product_list = ProductListView.as_view()

class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self,*args, **kwargs):
        context = super(CategoryListView,self).get_context_data(*args, **kwargs)
        context['current_category'] = get_object_or_404(Category,slug=self.kwargs['slug'])
        context['product_list'] = self.get_queryset
        return context

category = CategoryListView.as_view()

def product(request,slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product':product,
    }
    return render(request,'catalog/product.html',context)
