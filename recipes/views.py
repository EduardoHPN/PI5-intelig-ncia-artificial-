from django.shortcuts import render


def home(resquest):
    return render(resquest, 'recipes/pages/home.html',{})

def Penal(request):
    return render(request, 'recipes/pages/penal_home.html',{})

def EmBreve(request):
    return render(request, 'recipes/pages/emBreve.html', {})

def Login(request):
    return render(request, 'recipes/pages/login.html', {})

def Cadastro(request):
    return render(request, 'recipes/pages/cadastro.html', {})