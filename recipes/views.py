from django.shortcuts import render


def home(resquest):
    return render(resquest, 'recipes/pages/home.html',{
    })

