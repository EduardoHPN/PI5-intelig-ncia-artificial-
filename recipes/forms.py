from django import forms 
from recipes.models import ClienteTeste, ClientParagrafOne

class ClienteTesteForma(forms.ModelForm):
    class Meta:
        model = ClienteTeste
        fields = "__all__"


        
class ParagrafOneForm(forms.ModelForm):
    class Meta:
        model = ClientParagrafOne
        fields = [
            'ProcessNumer',
            'NumberStickCriminal',
            'CityComarc',
            'TypeAction',
            'PartOuter',
            'NameAcused',
            'Nacionalit',
            'CivilState',
            'Cpf',
            'Address',
            'State',
            'AnoterDefender',
        ]
