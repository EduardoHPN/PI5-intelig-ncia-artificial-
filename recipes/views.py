import re
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from recipes.forms import *
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse
import traceback
from django.views.decorators.http import require_POST

from recipes.scripts import *

import json


paragrafo1 = '0'
paragrafo2 = '0'
paragrago3 = '0'

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

        return redirect('preliminar')
  



    return render(request, 'recipes/formulario/paragrafOne.html', {'form': form})


def EmBreve(request):
    if not request.session.get('autenticado'):
        return redirect('/')
    return render(request, 'recipes/pages/emBreve.html', {})

def Login(request):
    return render(request, 'recipes/pages/login.html', {})

def logout(request):
    request.session.flush()
    response = redirect('/')
    response.delete_cookie('firebase_token')
    django_logout(request)
    return response

def Cadastro(request):
    return render(request, 'recipes/pages/cadastro.html', {})



def defesa_preliminar(request):
    if not request.session.get('autenticado'):
        return redirect('/')

    if request.method == "GET":
        form = DefesaPreliminarForm()
        return render(request, 'recipes/formulario/DefesaPrelimitar.html', {'form': form})

    form = DefesaPreliminarForm(request.POST)
    if form.is_valid():
        cliente = form.save(commit=False)
        uid = request.session.get('uid')

        if not uid:
            return JsonResponse({'error': 'UID não encontrado na sessão'}, status=400)

        cliente.uid = uid
        cliente.save()

        return redirect('argju')

    return render(request, 'recipes/formulario/DefesaPrelimitar.html', {'form': form})





def ArgJuridica(request):
    if not request.session.get('autenticado'):
        return redirect('/')

    campos_nulidades = [
        "falha_cumprimento_legal",
        "falha_qual",
        "tratamento_injusto",
        "irregularidade_prisao",
        "direito_ampla_defesa",
        "direito_ampla_defesa_como",
        "defesa_ouvida",
        "defesa_prejuizos"
    ]


    campos_excludentes = [
    "estado_necessidade",
    "estado_necessidade_justificativa",
    "legitima_defesa",
    "legitima_defesa_explicacao",
    "erro_tipo_ou_proibicao",
    "erro_explicacao",
    "coercao_moral_irresistivel",
    "coercao_moral_explicacao",
    "outras_causas_excluintes",
    "outras_causas_excluintes_descr"
]

    campos_materialidade = [
        "prova_testemunhal_suficiente",
        "testemunhas_falha",
        "laudo_pericial_comprova",
        "laudo_falha_ou_omissao",
        "materialidade_nao_comprovada",
        "materialidade_por_que",
        "alibi_comprova_inocencia",
        "alibi_descricao",
        "acusacao_baseada_em_suposicoes",
        "acusacao_natureza_provas"
    ]

    campos_principios = [
    "presuncao_inocencia",
    "presuncao_inocencia_como",
    "devido_processo_legal",
    "devido_processo_legal_impactos",
    "proporcionalidade_violada",
    "proporcionalidade_como",
    "cerceamento_defesa",
    "cerceamento_defesa_momento",
    "dignidade_pessoa_humana",
    "dignidade_pessoa_humana_aspecto",
    "tratamento_diferenciado",
    "tratamento_diferenciado_qual",
    "julgamento_imparcial",
    "julgamento_imparcial_como"
]

    campos_outros_argumentos = [
        "circunstancia_relevante",
        "circunstancia_descricao",
        "pena_desproporcional",
        "pena_desproporcional_justificativa",
        "jurisprudencia_favorece",
        "jurisprudencia_descricao"
    ]

    if request.method == "GET":
        form = ArgumentacaoJuridicaForm()
        return render(request, 'recipes/formulario/ArgumentacaoJuridica.html', {
        'form': form,
        'campos_nulidades': campos_nulidades,
        'campos_materialidade': campos_materialidade,
        'campos_excludentes': campos_excludentes,
        'campos_principios': campos_principios,
        'campos_outros_argumentos': campos_outros_argumentos,
        })

    form = ArgumentacaoJuridicaForm(request.POST)
    if form.is_valid():
        cliente = form.save(commit=False)
        uid = request.session.get('uid')

        if not uid:
            return JsonResponse({'error': 'UID não encontrado na sessão'}, status=400)

        cliente.uid = uid
        cliente.save()

        return redirect('pedido')

    return render(request, 'recipes/formulario/ArgumentacaoJuridica.html', {
        'form': form,
        'campos_nulidades': campos_nulidades,
        'campos_materialidade': campos_materialidade,
        'campos_excludentes': campos_excludentes,
        'campos_principios': campos_principios,
        'campos_outros_argumentos': campos_outros_argumentos,
    })



def pedido(request):
    if not request.session.get('autenticado'):
        return redirect('/')

    if request.method == "GET":
        form = PedidoDefesaPenalForm()
        return render(request, 'recipes/formulario/Pedido.html', {'form': form})

    print("jaslkdjasldkjasldkjaslkdj")
    form = PedidoDefesaPenalForm(request.POST)
    if form.is_valid():
        cliente = form.save(commit=False)
        uid = request.session.get('uid')

        if not uid:
            return JsonResponse({'error': 'UID não encontrado na sessão'}, status=400)

        cliente.uid = uid
        cliente.save()

        

        return redirect('documentos')
    return render(request, 'recipes/formulario/Pedido.html', {'form': form})





def PrimeiroParagrado(resquest):
    uid = resquest.session.get('uid')
    clientes = buscar_clientes_por_uid(uid=uid)
    print(clientes)
    

def documentos(request):
    print("Início da função documentos")

    if not request.session.get('autenticado'):
        print("Usuário não autenticado. Redirecionando para /")
        return redirect('/')

    if request.method == "GET":
        print("Método GET detectado. Exibindo formulário.")
        form = DocumentacaoEJurisprudenciaForm()
        return render(request, 'recipes/formulario/documentacao.html', {'form': form})

    print("Método POST detectado. Processando dados do formulário.")

    try:
        form = DocumentacaoEJurisprudenciaForm(request.POST)
        if form.is_valid():
            print("Formulário válido.")
            cliente = form.save(commit=False)

            uid = request.session.get('uid')
            if not uid:
                print("UID não encontrado na sessão.")
                return JsonResponse({'error': 'UID não encontrado na sessão'}, status=400)

            cliente.uid = uid

            try:
                cliente.save()
                print(f"Cliente salvo com sucesso com UID: {uid}")
            except Exception as e:
                print(f"Erro ao salvar cliente: {e}")
                return JsonResponse({'error': 'Erro ao salvar cliente.'}, status=500)

            # Redireciona para a URL nomeada "relotorio"
            return redirect(reverse('generate_pdf'))

        else:
            print("Formulário inválido.")
            print(form.errors)

    except Exception as e:
        print(f"Erro inesperado ao processar o formulário: {e}")
        return JsonResponse({'error': 'Erro inesperado ao processar o formulário.'}, status=500)

    return render(request, 'recipes/formulario/documentacao.html', {'form': form})


def string_para_dicionario(texto: str) -> dict:
    dicionario = {}
    topico_atual = None
    subtopico_atual = None
    linhas = texto.strip().splitlines()

    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue

        # Verifica se é um tópico principal (ex: 3.0 - ...)
        match_topico = re.match(r'^(\d+\.\d+)\s*-\s*(.+)', linha)
        if match_topico:
            topico_atual = match_topico.group(1) + ' - ' + match_topico.group(2)
            dicionario[topico_atual] = ""  # Cria uma chave no dicionário
            subtopico_atual = None
            continue

        # Verifica se é um subtópico (ex: 3.1 - ...)
        match_subtopico = re.match(r'^(\d+\.\d+)\s*-\s*(.+)', linha)
        if match_subtopico and topico_atual:
            subtopico_atual = match_subtopico.group(1) + ' - ' + match_subtopico.group(2)
            dicionario[subtopico_atual] = ""  # Cria uma chave para o subtópico
            continue

        # Se estiver em um tópico ou subtópico, adiciona o conteúdo
        if subtopico_atual:
            dicionario[subtopico_atual] += linha + " "
        elif topico_atual:
            dicionario[topico_atual] += linha + " "

    # Remove espaços extras no fim
    for chave in dicionario:
        dicionario[chave] = dicionario[chave].strip()

    return dicionario


@csrf_exempt
def relotorio(request):
    print("Início da função relotorio")

    uid = request.session.get('uid')
    print(f"UID da sessão: {uid}")

    if not uid:
        print("UID não encontrado na sessão. Retornando erro.")
        return JsonResponse({'error': 'Usuário não autenticado'}, status=400)

    # 1) Buscar dados dos formulários
    try:
        cliente1 = buscar_clientes_por_uid(uid)
        cliente2 = buscar_clientes_por_uid2(uid)
        cliente3 = buscar_clientes_por_uid3(uid)
        cliente4 = buscar_clientes_por_uid4(uid)
        cliente5 = buscar_clientes_por_uid5(uid)

        print("Dados buscados com sucesso.")
        print(f"cliente1: {cliente1}")
        print(f"cliente2: {cliente2}")
        print(f"cliente3: {cliente3}")
        print(f"cliente4: {cliente4}")
        print(f"cliente5: {cliente5}")
    except Exception:
        print("Erro ao buscar os dados dos formulários.")
        traceback.print_exc()
        return JsonResponse({'error': 'Erro ao buscar os dados do cliente'}, status=500)

    # 2) Verificar dados faltantes
    missing = []
    if cliente1 is None: missing.append("Formulário Parágrafo 1")
    if cliente2 is None: missing.append("Formulário Defesa Preliminar")
    if cliente3 is None: missing.append("Formulário Argumentação Jurídica")
    if cliente4 is None: missing.append("Formulário Pedido")
    if cliente5 is None: missing.append("Formulário Documentação")

    if missing:
        print("Formulários faltando:", missing)
        return JsonResponse({
            'error': 'Dados incompletos',
            'detail': 'Você precisa preencher: ' + ', '.join(missing)
        }, status=400)

    # 3) Montar scripts e gerar PDF
    try:
        print("Montando parágrafos...")
        paragrafo1 = montar_script(cliente1)
        paragrafo2 = montar_script2(cliente2, paragrafo1)
        paragrafo3 = montar_script3(cliente3, paragrafo2)
        paragrafo4 = montar_script4(cliente4, paragrafo3)
        paragrafo5 = montar_script5(cliente5, paragrafo3)
        paragrafo6 = scriptfinal(paragrafo1, paragrafo2)

        print("Parágrafos montados com sucesso.")
        print("Renderizando HTML...")

        html = render_to_string('recipes/pdf_template.html', {
            'paragrafo1': paragrafo1,
            'paragrafo2': paragrafo2,
            'paragrafo3': string_para_dicionario(paragrafo3),
            'paragrafo4': paragrafo4,
            'paragrafo5': string_para_dicionario(paragrafo5),
            'paragrafo6': paragrafo6,
        })

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="peticao_completa.pdf"'

        print("Gerando PDF...")
        pisa_status = pisa.CreatePDF(src=html, dest=response)
        if pisa_status.err:
            print("Erro ao gerar o PDF.")
            return JsonResponse({'error': 'Erro ao gerar PDF'}, status=500)

        print("PDF gerado com sucesso.")
        return response

    except Exception:
        print("Erro ao montar o PDF:")
        traceback.print_exc()
        return JsonResponse({'error': 'Erro interno ao processar PDF'}, status=500)