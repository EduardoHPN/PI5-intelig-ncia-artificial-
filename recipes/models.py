from django.db import models

# Create your models here.
 
sexo_choise = (
    ('F', 'Feminino'),
    ('M', 'Masculino')

)

TypeActionChoise = (
    ('AC', 'Ação Penal'),
    ('IP', 'Inquerito Policial')
)


preso = (
    ('S', 'Preso'),
    ('N', 'Não Preso')
)

class ClienteTeste(models.Model):
    nome = models.CharField(max_length=50)
    data_nasc = models.DateField(blank=True, null= True)
    sexo = models.CharField(max_length=1, choices=sexo_choise)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
    


class  ClientParagrafOne(models.Model):
    uid = models.CharField(max_length=100, verbose_name="uid user",blank=True, null=True)
    ProcessNumer = models.CharField(max_length=40, verbose_name="Numero do processo")
    NumberStickCriminal = models.CharField(max_length=40, verbose_name=" Numero da vara criminal")
    CityComarc = models.CharField(max_length=40, verbose_name="Numero da comarca")
    TypeAction = models.CharField(max_length=2, choices=TypeActionChoise, verbose_name="Tipo da acusação")
    PartOuter = models.CharField(max_length=40, verbose_name="Parte da autora")
    NameAcused = models.CharField(max_length=40, verbose_name="Nome do acusado")
    Nacionalit = models.CharField(max_length=15, verbose_name="Nacionalidade")
    CivilState = models.CharField(max_length=15, verbose_name="Estado Civíl")
    Cpf = models.CharField(max_length=14, verbose_name="CPF")
    Address = models.CharField(max_length=150, verbose_name="Endereço")
    State = models.CharField(max_length=1, choices=preso, verbose_name="O cliente está preso?")
    AnoterDefender = models.CharField(max_length=40,blank=True, null=True, verbose_name="Nome do advogado de ataque" )


    def __str__(self):
        return self.NameAcused
    