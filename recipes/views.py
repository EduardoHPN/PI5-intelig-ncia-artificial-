from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from recipes.forms import ParagrafOneForm
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse

from recipes.scripts import buscar_clientes_por_uid, montar_script

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

from recipes.scripts import buscar_clientes_por_uid

def Penal(request):
    if not request.session.get('autenticado'):
        return redirect('/')

    if request.method == "GET":
        form = ParagrafOneForm()
        return render(request, 'recipes/formulario/paragrafOne.html', {'form': form})

    form = ParagrafOneForm(request.POST)
    if form.is_valid():
        cliente = form.save(commit=False)
        uid = request.session.get('uid')

        if not uid:
            return JsonResponse({'error': 'UID não encontrado na sessão'}, status=400)

        cliente.uid = uid
        cliente.save()

        clientes = buscar_clientes_por_uid(uid)
        paragrafo1 = montar_script(clientes)
        clientes = buscar_clientes_por_uid(uid)
        paragrafo1 = montar_script(clientes)

        # Gera HTML com o texto
        html = render_to_string('recipes/pdf_template.html', {'paragrafo': paragrafo1})

        # Gera PDF a partir do HTML
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="peticao.pdf"'

        pisa_status = pisa.CreatePDF(
            src=html,
            dest=response,
        )

        if pisa_status.err:
            return HttpResponse('Erro ao gerar PDF', status=500)

        return response


    return render(request, 'recipes/formulario/paragrafOne.html', {'form': form})


def EmBreve(request):
    return render(request, 'recipes/pages/emBreve.html', {})

def Login(request):
    return render(request, 'recipes/pages/login.html', {})

def Cadastro(request):
    return render(request, 'recipes/pages/cadastro.html', {})




def PrimeiroParagrado(resquest):
    uid = resquest.session.get('uid')
    clientes = buscar_clientes_por_uid(uid=uid)
    print(clientes)
    