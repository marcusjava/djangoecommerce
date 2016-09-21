"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from accounts import views

urlpatterns = [
    url(r'^registro/$',views.register,name='register'),
    url(r'^atualizar-dados/$',views.update_user,name='update_user'),
    url(r'^alterar-senha/$',views.password_change,name='password_change'),
    url(r'^usuarios/$',views.userlist,name='userlist'),
    url(r'^$',views.index,name='index'),
]
