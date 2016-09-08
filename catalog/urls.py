from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.product_list,name='product_list'),
    url(r'^categoria/(?P<slug>[\w_-]+)/$',views.category,name='category'),
    #url /produtos/design por exemplo
    url(r'^produtos/(?P<slug>[\w_-]+)/$',views.product,name='product'),
]
