from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms



class UserAdminCreationForm(UserCreationForm):

    #sobrescrever a classe meta para adicionar novos campos

    class Meta:
        model = User
        fields = ['username','name','email']

class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','name','is_active','is_staff']
