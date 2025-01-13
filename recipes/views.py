from django.http import HttpResponse
from django.shortcuts import render


def home(resquest):
    return render(resquest, 'recipes/home.html',{
        'name': "Eduardo Henrique Porto Nemesio"
    })

def contato(request):
    return HttpResponse("+55(19)99949-8012")

def sobre(request):
    return HttpResponse("Eduardo Henrique Porto Nemesio")