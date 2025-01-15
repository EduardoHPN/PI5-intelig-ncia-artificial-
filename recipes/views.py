from django.shortcuts import render


def home(resquest):
    return render(resquest, 'recipes/pages/home.html',{
        'name': "Eduardo Henrique Porto Nemesio"
    })

