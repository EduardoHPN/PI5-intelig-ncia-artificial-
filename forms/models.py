from django.db import models

SEXO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino')
)

class Pessoa(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    sexo = models.CharField(choices=SEXO_CHOICES)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    cor_favorita = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nome