from django import forms 
from recipes.models import ClienteTeste

class ClienteTesteForma(forms.ModelForm):
    class meta():
        model = ClienteTeste
        fields = "__all__"