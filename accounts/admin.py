from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserAdminCreationForm,UserAdminForm

# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserAdminForm
    #formulario personalizado que adiciona o email no formulario
    add_form = UserAdminCreationForm
    #adiciona os campos do formulario
    add_fieldsets = (
        (None,{'fields':('username','name','email','password1','password2')}),
    )
    fieldsets = ((None,{'fields':('username','email')}),
                ('Informações Basicas',{'fields':('name','last_login')}),
                ('Permissões',{'fields':('is_active','is_staff','is_superuser','groups','user_permissions')}),
    )
    list_display = ['username','name','email','is_active','is_staff','date_joined']

admin.site.register(User,UserAdmin)
