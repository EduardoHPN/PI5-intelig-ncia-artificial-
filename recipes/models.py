from django.db import models

# Create your models here.
 
sexo_choise = (
    ('F', 'Feminino'),
    ('M', 'Masculino')

)

class ClienteTeste(models.Model):
    nome = models.CharField(max_length=50)
    data_nasc = models.DateField(blank=True, null= True)
    sexo = models.CharField(max_length=1, choices=sexo_choise)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.nome