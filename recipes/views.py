from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import json


@csrf_exempt
def autenticar_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            uid = data.get('uid')

            if uid:
                print(f'UID recebido: {uid}')
                request.session['autenticado'] = True
                request.session['uid'] = uid 
                return HttpResponseRedirect('/home/')
            else:
                return JsonResponse({'error': 'UID não fornecido'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

    return JsonResponse({'error': 'Método não permitido'}, status=405)



def home(request):
    uid = request.session.get('uid')
    if not request.session.get('autenticado'):
        return redirect('/')
    print(f"UID do usuário autenticado: {uid}")
    return render(request, 'recipes/pages/home.html', {})

def Penal(request):
    return render(request, 'recipes/pages/penal_home.html',{})

def EmBreve(request):
    return render(request, 'recipes/pages/emBreve.html', {})

def Login(request):
    return render(request, 'recipes/pages/login.html', {})

def Cadastro(request):
    return render(request, 'recipes/pages/cadastro.html', {})