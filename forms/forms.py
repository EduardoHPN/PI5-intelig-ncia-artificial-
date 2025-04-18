from django import forms
from forms.models import Pessoa  
from django.contrib.auth.models import User

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__' 


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' 