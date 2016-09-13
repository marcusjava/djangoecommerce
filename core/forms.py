from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem',widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome:{0}\nEmail:{1}\n{2}'.format(name,email,message)
        #enviando email no console
        send_mail('Contato Django E-commerce',message,settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_FROM_EMAIL])

    '''

    #mudar aparencia do form adicionando classe do bootstrap
    usar o widget_tweaks no template
    def __init__(self,*args,**kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)
        #atribuindo ao widget no atributo classe o form-control do bootstrap
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'
    '''
