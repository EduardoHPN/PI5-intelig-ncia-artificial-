from django import forms
from forms.models import Pessoa  

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__' 
