# recipes/scripts.py
from recipes.models import *
import google.generativeai  as genai
from datetime import datetime

genai.configure(api_key="AIzaSyAcwUz7nk6imi9xBzXar71skr01vkBYxPE")


def buscar_clientes_por_uid(uid):
    return ClientParagrafOne.objects.filter(uid=uid).first()


def montar_script(cliente): 
    numero_processo = cliente.ProcessNumer
    vara_criminal = cliente.NumberStickCriminal
    comarca = cliente.CityComarc
    tipo_acusacao = cliente.TypeAction
    parte_autora = cliente.PartOuter
    nome_acusado = cliente.NameAcused
    nacionalidade = cliente.Nacionalit
    estado_civil = cliente.CivilState
    cpf = cliente.Cpf
    endereco = cliente.Address
    preso = cliente.State
    advogado_defesa = cliente.AnoterDefender

    # Exemplo de uso das variáveis - montar um texto com esses dados
    texto = f"""
Com base nas informações abaixo, redija o primeiro parágrafo de uma petição de defesa penal com linguagem formal, jurídica e adequada ao processo:

- Número do processo: {numero_processo}
- Vara Criminal: {vara_criminal}
- Comarca: {comarca}
- Tipo de Ação: {tipo_acusacao}
- Parte autora: {parte_autora}
- Nome do acusado: {nome_acusado}
- Nacionalidade: {nacionalidade}
- Estado civil: {estado_civil}
- CPF: {cpf}
- Endereço: {endereco}
- O acusado está preso? {preso}
- Nome do advogado de defesa: {advogado_defesa if advogado_defesa else "não informado"}

O parágrafo deve conter:
- quero que faça como tivesse regindo uma petição ou seja oq escrever aqui o juiz vai ler

1. Identificação do processo e do juízo;
2. Qualificação resumida do acusado;
3. Indicação de que se trata de uma defesa;
4. Menção ao advogado, se informado;
5. Tom respeitoso, técnico e claro.
    """

    print(f'\n\n\n\n{texto}')

    model = genai.GenerativeModel("gemini-1.5-flash")  # ou "gemini-pro"
    response = model.generate_content(texto)

    return response.text


def buscar_clientes_por_uid2(uid):
    return DefesaPreliminar.objects.filter(uid=uid).first()

def montar_script2(cliente, paragrafo):
    artigo_crime = cliente.artigo_crime
    data_fato = cliente.data_fato.strftime('%d/%m/%Y')
    local_fato = cliente.local_fato
    admite_crime = "sim" if cliente.admite_crime else "não"
    havia_testemunhas = "sim" if cliente.havia_testemunhas else "não"
    descricao_testemunhas = cliente.descricao_testemunhas or "Não informado"
    provas = cliente.provas_mencionadas or "Não mencionadas"
    antecedentes = "sim" if cliente.antecedentes else "não"
    preso = "sim" if cliente.esta_preso else "não"
    local_prisao = cliente.local_prisao or "Não informado"
    liberdade = cliente.em_liberdade or "Não informado"
    alibi_defesa = cliente.alibi_ou_testemunha_defesa or "Não informado"
    mencionar_defesa_futura = "sim" if cliente.mencionar_defesa_futura else "não"

    tons = {
        'F': 'formal, técnico e objetivo',
        'E': 'enfático e contundente',
        'N': 'neutro',
    }
    tom_texto = tons.get(cliente.tonalidade, 'neutro')

    prompt = f"""
Com base nas informações abaixo, redija um parágrafo introdutório de uma peça de defesa preliminar em matéria penal, respeitando a linguagem jurídica, a estrutura formal e o tom indicado ({tom_texto}):

- Artigo ou tipo de crime: {artigo_crime}
- Data do fato: {data_fato}
- Local do fato: {local_fato}
- O acusado admite o crime? {admite_crime}
- Havia testemunhas? {havia_testemunhas}
- Informações sobre as testemunhas: {descricao_testemunhas}
- Provas mencionadas: {provas}
- Possui antecedentes criminais? {antecedentes}
- Está preso atualmente? {preso}
- Local da prisão (se preso): {local_prisao}
- Situação se estiver em liberdade: {liberdade}
- Álibi ou testemunhas de defesa: {alibi_defesa}
- Deseja mencionar que a defesa será apresentada em momento oportuno? {mencionar_defesa_futura}

Requisitos do texto:
- quero que faça como tivesse regindo uma petição ou seja oq escrever aqui o juiz vai ler

1. Redação clara, objetiva e juridicamente precisa;
2. Abordagem introdutória da tese defensiva com base nas informações fornecidas;
3. Adaptação ao tom ({tom_texto}).
4. SEJA CONEXO COM ESSE PARAGRAFO: {paragrafo}

com base também nesse exemplo:
2.1 - Identificação da peça:

*"Defesa Preliminar nos autos do processo em epígrafe, com fundamento no art. 396-A do CPP."*

2.2 - Resumo do caso:
    """

    print(f'\n\nPrompt enviado ao modelo:\n{prompt}')

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text



def buscar_clientes_por_uid3(uid):
    return ArgumentacaoJuridica.objects.filter(uid=uid).first()



def montar_script3(argumento: ArgumentacaoJuridica, paragrafo):
    def sim_nao(valor):
        return "Sim" if valor else "Não"

    # Listas para categorias específicas
    nulidades = []
    materialidade = []
    excludentes = []
    principios = []

    # 3.1 - Nulidades ou vícios processuais
    if argumento.falha_cumprimento_legal:
        nulidades.append(f"Inobservância de formalidades legais: {argumento.falha_qual}")
    if argumento.tratamento_injusto:
        nulidades.append(f"Tratamento processual injusto: {argumento.tratamento_injusto}")
    if argumento.irregularidade_prisao:
        nulidades.append(f"Irregularidade na prisão: {argumento.irregularidade_prisao}")
    if not argumento.defesa_ouvida and argumento.defesa_prejuizos:
        nulidades.append(f"Prejuízo por ausência de oitiva da defesa: {argumento.defesa_prejuizos}")
    if argumento.cerceamento_defesa:
        nulidades.append(f"Cerceamento de defesa: {argumento.cerceamento_defesa_momento}")
    if not argumento.julgamento_imparcial:
        nulidades.append(f"Ausência de julgamento imparcial: {argumento.julgamento_imparcial_como}")

    # 3.2 - Inexistência de materialidade ou autoria
    if not argumento.laudo_pericial_comprova and argumento.laudo_falha_ou_omissao:
        materialidade.append(f"Laudo pericial inconclusivo: {argumento.laudo_falha_ou_omissao}")
    if argumento.materialidade_nao_comprovada:
        materialidade.append(f"Materialidade não comprovada: {argumento.materialidade_por_que}")
    if not argumento.prova_testemunhal_suficiente and argumento.testemunhas_falha:
        materialidade.append(f"Prova testemunhal frágil ou contraditória: {argumento.testemunhas_falha}")
    if argumento.acusacao_baseada_em_suposicoes:
        materialidade.append(f"Acusação baseada em suposições: {argumento.acusacao_natureza_provas}")
    if argumento.alibi_comprova_inocencia:
        materialidade.append(f"Álibi apresentado: {argumento.alibi_descricao}")

    # 3.3 - Excludentes de ilicitude ou culpabilidade
    if argumento.legitima_defesa:
        excludentes.append(f"Legítima defesa: {argumento.legitima_defesa_explicacao}")
    if argumento.estado_necessidade:
        excludentes.append(f"Estado de necessidade: {argumento.estado_necessidade_justificativa}")
    if argumento.erro_tipo_ou_proibicao != 'nao_aplica':
        excludentes.append(f"{argumento.get_erro_tipo_ou_proibicao_display()}: {argumento.erro_explicacao}")
    if argumento.coercao_moral_irresistivel:
        excludentes.append(f"Coação moral irresistível: {argumento.coercao_moral_explicacao}")
    if argumento.outras_causas_excluintes:
        excludentes.append(f"Outras causas excludentes: {argumento.outras_causas_excluintes_descr}")
    if argumento.circunstancia_relevante:
        excludentes.append(f"Circunstância relevante: {argumento.circunstancia_descricao}")

    # 3.4 - Princípios violados
    if argumento.presuncao_inocencia:
        principios.append(f"Violação à presunção de inocência: {argumento.presuncao_inocencia_como}")
    if not argumento.devido_processo_legal:
        principios.append(f"Violação ao devido processo legal: {argumento.devido_processo_legal_impactos}")
    if argumento.proporcionalidade_violada:
        principios.append(f"Violação ao princípio da proporcionalidade: {argumento.proporcionalidade_como}")
    if argumento.dignidade_pessoa_humana:
        principios.append(f"Violação à dignidade da pessoa humana: {argumento.dignidade_pessoa_humana_aspecto}")
    if argumento.tratamento_diferenciado:
        principios.append(f"Discriminação ou tratamento desigual: {argumento.tratamento_diferenciado_qual}")

    # Gerar prompt estruturado
    prompt = f"""
Você é um advogado criminalista. Redija uma **argumentação jurídica detalhada**, organizada nos tópicos abaixo, com base nas informações fornecidas:

3.0 - ARGUMENTAÇÃO JURÍDICA (Detalhada)

3.1 - Nulidades ou vícios processuais (se aplicável):
{chr(10).join(f"- {item}" for item in nulidades) if nulidades else "- Não identificadas."}

3.2 - Inexistência de materialidade ou autoria:
{chr(10).join(f"- {item}" for item in materialidade) if materialidade else "- Não identificadas."}

3.3 - Excludentes de ilicitude ou culpabilidade:
{chr(10).join(f"- {item}" for item in excludentes) if excludentes else "- Não identificadas."}

3.4 - Princípios violados:
{chr(10).join(f"- {item}" for item in principios) if principios else "- Não identificados."}

Requisitos:
- quero que faça como tivesse regindo uma petição ou seja oq escrever aqui o juiz vai ler

- Redação técnica e jurídica, com base na doutrina e jurisprudência.
- Linguagem clara e precisa.
- Tom persuasivo e defensivo.
NAO VOU COLOCAR NEM DATA NEM NOME DO ADVOGADO nao coloque nada entre parenteses isso vai ser ligo pelo juiz
SEJA CONEXO COM ESSE PARAGRAFO: {paragrafo}
-Não pode ter mais topicos apenas o 3.0 3.1 3.2 3.3 e 3.4, e nao pode ter subtopicos
    """

    print(f"\n\nPrompt para IA:\n{prompt}")

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text


def buscar_clientes_por_uid4(uid):
    return PedidoDefesaPenal.objects.filter(uid=uid).first()


def montar_script4(cliente, paragrafo3):
    pedido_principal = cliente.pedido_principal
    absolve_sumaria_como_alternativa = "Sim" if cliente.incluir_absolvicao_como_alternativa else "Não"
    fundamentos_absolvicao = cliente.fundamentos_absolvicao or "Não mencionados"
    reu_preso = "Sim" if cliente.esta_preso else "Não"
    solicita_alvara_soltura = "Sim" if cliente.solicitar_alvara else "Não"
    medidas_cautelares_alternativas = cliente.medidas_cautelares or "Não mencionadas"
    pedido_subsidiario = "Sim" if cliente.incluir_pedido_subsidiario else "Não"
    pedido_subsidiario_qual = cliente.pedido_subsidiario or "Não mencionado"
    requer_nao_recebimento_denuncia = "Sim" if cliente.requerer_nao_recebimento_denuncia else "Não"
    requer_prioridade_tramitacao = "Sim" if cliente.requerer_prioridade else "Não"
    requer_acesso_provas_diligencias = "Sim" if cliente.requerer_acesso_provas else "Não"
    quais_provas_diligencias = cliente.quais_provas or "Não mencionado"
    observacoes_finais = cliente.outros_pedidos or "Não mencionadas"


    prompt = f"""
Com base nas informações abaixo, redija o **quarto parágrafo** da defesa prévia, considerando os pedidos principais e subsidiários, os fundamentos legais e as observações finais do caso. O parágrafo deve ser claro, jurídico e concluir a peça com base nos dados fornecidos. Mantenha coesão com o parágrafo 3 abaixo):

- Pedido principal: {pedido_principal}
- Absolvição sumária como alternativa: {absolve_sumaria_como_alternativa}
- Fundamentos para a absolvição sumária: {fundamentos_absolvicao}
- Réu preso atualmente: {reu_preso}
- Solicita alvará de soltura: {solicita_alvara_soltura}
- Medidas cautelares alternativas: {medidas_cautelares_alternativas}
- Pedido subsidiário: {pedido_subsidiario}
- Pedido subsidiário qual: {pedido_subsidiario_qual}
- Requer não recebimento da denúncia: {requer_nao_recebimento_denuncia}
- Requer prioridade na tramitação: {requer_prioridade_tramitacao}
- Requer acesso às provas/diligências: {requer_acesso_provas_diligencias}
- Quais provas/diligências requer: {quais_provas_diligencias}
- Observações finais: {observacoes_finais}

Requisitos para o parágrafo:
- quero que faça como tivesse regindo uma petição ou seja oq escrever aqui o juiz vai ler
1. Conclusão da peça de defesa, abordando os pedidos finais e fundamentos jurídicos do caso;
2. Enfoque no pedido principal de absolvição, alternativas e medidas cautelares;
3. Manter a conexão com o parágrafo 3 abaixo:
{paragrafo3}
    """

    print(f'\n\nPrompt enviado ao modelo:\n{prompt}')

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text


def buscar_clientes_por_uid5(uid):
    return DocumentacaoEJurisprudencia.objects.filter(uid=uid).first()

def montar_script5(cliente, paragrafo):
    # Coletando os dados do cliente e da documentação
    certidao = cliente.certidao
    laudo = cliente.laudo
    testemunha_nome = cliente.testemunha_nome
    testemunha_qualificacao = cliente.testemunha_qualificacao
    jurisprudencias = cliente.jurisprudencias
    incluir_jurisprudencia_apoio = cliente.incluir_jurisprudencia_apoio
    tese_juridica_apoio = cliente.tese_juridica_apoio
    julgado_especifico = cliente.julgado_especifico

    # Exemplo de uso das variáveis - montar um texto com esses dados
    prompt = f"""
Com base nas informações abaixo, redija o quinto parágrafo de uma petição de defesa penal com base na documentação apresentada:

- Certidão relevante: {certidao if certidao else "não fornecida"}
- Laudo técnico ou pericial: {laudo if laudo else "não fornecido"}
- Testemunha: {testemunha_nome if testemunha_nome else "não indicada"}
- Qualificação da testemunha: {testemunha_qualificacao if testemunha_qualificacao else "não informada"}
- Jurisprudências relevantes: {jurisprudencias if jurisprudencias else "não fornecida"}
- Incluir jurisprudência de apoio? {incluir_jurisprudencia_apoio}
- Tese jurídica de apoio: {tese_juridica_apoio if tese_juridica_apoio else "não fornecida"}
- Julgado específico: {julgado_especifico if julgado_especifico else "não fornecido"}

O parágrafo deve conter:
- quero que faça como tivesse regindo uma petição ou seja oq escrever aqui o juiz vai ler
seguindo esse modelo como base pode sofrer alterações se necessarios
5.0 - DOCUMENTAÇÃO E PROVAS (Anexos)
5.1 - Lista de documentos:

Certidões, laudos, testemunhas, jurisprudências (ex.: STJ, STF).

5.2 - Jurisprudência de apoio:

Citar julgados recentes (ex.: *"HC 123.456/STJ: 'A falta de flagrante inviabiliza a prisão preventiva...'"*).
     agora as perguntas pra serem feitas aqui
1. Identificação da documentação relevante apresentada para sustentar a defesa;
2. Menção a laudos técnicos, certidões e testemunhas que possam corroborar a defesa;
3. Referência a jurisprudências que apoiam a tese de defesa;
4. Menção a tese jurídica a ser adotada para a defesa do acusado;
5. Tom formal, jurídico e técnico, adequado ao processo e respeitante à autoridade do juiz.

e use com base o 3 paragrafo {paragrafo}
    """

    print(f'\n\nPrompt enviado ao modelo:\n{prompt}')

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text




def scriptfinal(relatorio1, relatorio2):
    data_atual = datetime.now()
    prompt = f"""
    com base nas informações contidas aqui: {relatorio2}
    e essa: {relatorio1}
    LEMRBADNO QUE HOJE È DIA {data_atual}
faça um paragrafo final para a petição penal com essa base de conhecimento: 6.0 - ASSINATURA
[Local, data] de hoje pf

[Nome do Advogado]

[OAB/UF Nº]"""
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text
# recipes/scripts.py
from recipes.models import *
import google.generativeai  as genai
from datetime import datetime

genai.configure(api_key="AIzaSyAcwUz7nk6imi9xBzXar71skr01vkBYxPE")


def buscar_clientes_por_uid(uid):
    return ClientParagrafOne.objects.filter(uid=uid).first()


def montar_script(cliente):
    numero_processo = cliente.ProcessNumer
    vara_criminal = cliente.NumberStickCriminal
    comarca = cliente.CityComarc
    tipo_acusacao = cliente.TypeAction
    parte_autora = cliente.PartOuter
    nome_acusado = cliente.NameAcused
    nacionalidade = cliente.Nacionalit
    estado_civil = cliente.CivilState
    cpf = cliente.Cpf
    endereco = cliente.Address
    preso = cliente.State
    advogado_defesa = cliente.AnoterDefender

    # Exemplo de uso das variáveis - montar um texto com esses dados
    texto = f"""
Com base nas informações abaixo, redija o primeiro parágrafo de uma petição de defesa penal com linguagem formal, jurídica e adequada ao processo:

- Número do processo: {numero_processo}
- Vara Criminal: {vara_criminal}
- Comarca: {comarca}
- Tipo de Ação: {tipo_acusacao}
- Parte autora: {parte_autora}
- Nome do acusado: {nome_acusado}
- Nacionalidade: {nacionalidade}
- Estado civil: {estado_civil}
- CPF: {cpf}
- Endereço: {endereco}
- O acusado está preso? {preso}
- Nome do advogado de defesa: {advogado_defesa if advogado_defesa else "não informado"}

O parágrafo deve conter:
- quero que faça como tivesse regindo uma petição ou seja oq escrever aqui o juiz vai ler

1. Identificação do processo e do juízo;
2. Qualificação resumida do acusado;
3. Indicação de que se trata de uma defesa;
4. Menção ao advogado, se informado;
5. Tom respeitoso, técnico e claro.
    """

    print(f'\n\n\n\n{texto}')

    model = genai.GenerativeModel("gemini-1.5-flash")  # ou "gemini-pro"
    response = model.generate_content(texto)

    return response.text


def buscar_clientes_por_uid2(uid):
    return DefesaPreliminar.objects.filter(uid=uid).first()

def montar_script2(cliente, paragrafo):
    artigo_crime = cliente.artigo_crime
    data_fato = cliente.data_fato.strftime('%d/%m/%Y')
    local_fato = cliente.local_fato
    admite_crime = "sim" if cliente.admite_crime else "não"
    havia_testemunhas = "sim" if cliente.havia_testemunhas else "não"
    descricao_testemunhas = cliente.descricao_testemunhas or "Não informado"
    provas = cliente.provas_mencionadas or "Não mencionadas"
    antecedentes = "sim" if cliente.antecedentes else "não"
    preso = "sim" if cliente.esta_preso else "não"
    local_prisao = cliente.local_prisao or "Não informado"
    liberdade = cliente.em_liberdade or "Não informado"
    alibi_defesa = cliente.alibi_ou_testemunha_defesa or "Não informado"
    mencionar_defesa_futura = "sim" if cliente.mencionar_defesa_futura else "não"

    tons = {
        'F': 'formal, técnico e objetivo',
        'E': 'enfático e contundente',
        'N': 'neutro',
    }
    tom_texto = tons.get(cliente.tonalidade, 'neutro')

    prompt = f"""
Com base nas informações abaixo, redija um parágrafo introdutório de uma peça de defesa preliminar em matéria penal, respeitando a linguagem jurídica, a estrutura formal e o tom indicado ({tom_texto}):

- Artigo ou tipo de crime: {artigo_crime}
- Data do fato: {data_fato}
- Local do fato: {local_fato}
- O acusado admite o crime? {admite_crime}
- Havia testemunhas? {havia_testemunhas}
- Informações sobre as testemunhas: {descricao_testemunhas}
- Provas mencionadas: {provas}
- Possui antecedentes criminais? {antecedentes}
- Está preso atualmente? {preso}
- Local da prisão (se preso): {local_prisao}
- Situação se estiver em liberdade: {liberdade}
- Álibi ou testemunhas de defesa: {alibi_defesa}
- Deseja mencionar que a defesa será apresentada em momento oportuno? {mencionar_defesa_futura}

Requisitos do texto:
- quero que faça como tivesse regindo uma petição ou seja oq escrever aqui o juiz vai ler

1. Redação clara, objetiva e juridicamente precisa;
2. Abordagem introdutória da tese defensiva com base nas informações fornecidas;
3. Adaptação ao tom ({tom_texto}).
4. SEJA CONEXO COM ESSE PARAGRAFO: {paragrafo}

com base também nesse exemplo:
2.1 - Identificação da peça:

*"Defesa Preliminar nos autos do processo em epígrafe, com fundamento no art. 396-A do CPP."*

2.2 - Resumo do caso:
    """

    print(f'\n\nPrompt enviado ao modelo:\n{prompt}')

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text



def buscar_clientes_por_uid3(uid):
    return ArgumentacaoJuridica.objects.filter(uid=uid).first()



def montar_script3(argumento: ArgumentacaoJuridica, paragrafo):
    def sim_nao(valor):
        return "Sim" if valor else "Não"

    # Listas para categorias específicas
    nulidades = []
    materialidade = []
    excludentes = []
    principios = []

    # 3.1 - Nulidades ou vícios processuais
    if argumento.falha_cumprimento_legal:
        nulidades.append(f"Inobservância de formalidades legais: {argumento.falha_qual}")
    if argumento.tratamento_injusto:
        nulidades.append(f"Tratamento processual injusto: {argumento.tratamento_injusto}")
    if argumento.irregularidade_prisao:
        nulidades.append(f"Irregularidade na prisão: {argumento.irregularidade_prisao}")
    if not argumento.defesa_ouvida and argumento.defesa_prejuizos:
        nulidades.append(f"Prejuízo por ausência de oitiva da defesa: {argumento.defesa_prejuizos}")
    if argumento.cerceamento_defesa:
        nulidades.append(f"Cerceamento de defesa: {argumento.cerceamento_defesa_momento}")
    if not argumento.julgamento_imparcial:
        nulidades.append(f"Ausência de julgamento imparcial: {argumento.julgamento_imparcial_como}")

    # 3.2 - Inexistência de materialidade ou autoria
    if not argumento.laudo_pericial_comprova and argumento.laudo_falha_ou_omissao:
        materialidade.append(f"Laudo pericial inconclusivo: {argumento.laudo_falha_ou_omissao}")
    if argumento.materialidade_nao_comprovada:
        materialidade.append(f"Materialidade não comprovada: {argumento.materialidade_por_que}")
    if not argumento.prova_testemunhal_suficiente and argumento.testemunhas_falha:
        materialidade.append(f"Prova testemunhal frágil ou contraditória: {argumento.testemunhas_falha}")
    if argumento.acusacao_baseada_em_suposicoes:
        materialidade.append(f"Acusação baseada em suposições: {argumento.acusacao_natureza_provas}")
    if argumento.alibi_comprova_inocencia:
        materialidade.append(f"Álibi apresentado: {argumento.alibi_descricao}")

    # 3.3 - Excludentes de ilicitude ou culpabilidade
    if argumento.legitima_defesa:
        excludentes.append(f"Legítima defesa: {argumento.legitima_defesa_explicacao}")
    if argumento.estado_necessidade:
        excludentes.append(f"Estado de necessidade: {argumento.estado_necessidade_justificativa}")
    if argumento.erro_tipo_ou_proibicao != 'nao_aplica':
        excludentes.append(f"{argumento.get_erro_tipo_ou_proibicao_display()}: {argumento.erro_explicacao}")
    if argumento.coercao_moral_irresistivel:
        excludentes.append(f"Coação moral irresistível: {argumento.coercao_moral_explicacao}")
    if argumento.outras_causas_excluintes:
        excludentes.append(f"Outras causas excludentes: {argumento.outras_causas_excluintes_descr}")
    if argumento.circunstancia_relevante:
        excludentes.append(f"Circunstância relevante: {argumento.circunstancia_descricao}")

    # 3.4 - Princípios violados
    if argumento.presuncao_inocencia:
        principios.append(f"Violação à presunção de inocência: {argumento.presuncao_inocencia_como}")
    if not argumento.devido_processo_legal:
        principios.append(f"Violação ao devido processo legal: {argumento.devido_processo_legal_impactos}")
    if argumento.proporcionalidade_violada:
        principios.append(f"Violação ao princípio da proporcionalidade: {argumento.proporcionalidade_como}")
    if argumento.dignidade_pessoa_humana:
        principios.append(f"Violação à dignidade da pessoa humana: {argumento.dignidade_pessoa_humana_aspecto}")
    if argumento.tratamento_diferenciado:
        principios.append(f"Discriminação ou tratamento desigual: {argumento.tratamento_diferenciado_qual}")

    # Gerar prompt estruturado
    prompt = f"""
Você é um advogado criminalista. Redija uma **argumentação jurídica detalhada**, organizada nos tópicos abaixo, com base nas informações fornecidas:

3.0 - ARGUMENTAÇÃO JURÍDICA (Detalhada)

3.1 - Nulidades ou vícios processuais (se aplicável):
{chr(10).join(f"- {item}" for item in nulidades) if nulidades else "- Não identificadas."}

3.2 - Inexistência de materialidade ou autoria:
{chr(10).join(f"- {item}" for item in materialidade) if materialidade else "- Não identificadas."}

3.3 - Excludentes de ilicitude ou culpabilidade:
{chr(10).join(f"- {item}" for item in excludentes) if excludentes else "- Não identificadas."}

3.4 - Princípios violados:
{chr(10).join(f"- {item}" for item in principios) if principios else "- Não identificados."}

Requisitos:
- quero que faça como tivesse regindo uma petição ou seja oq escrever aqui o juiz vai ler

- Redação técnica e jurídica, com base na doutrina e jurisprudência.
- Linguagem clara e precisa.
- Tom persuasivo e defensivo.
NAO VOU COLOCAR NEM DATA NEM NOME DO ADVOGADO nao coloque nada entre parenteses isso vai ser ligo pelo juiz
SEJA CONEXO COM ESSE PARAGRAFO: {paragrafo}
    """

    print(f"\n\nPrompt para IA:\n{prompt}")

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text


def buscar_clientes_por_uid4(uid):
    return PedidoDefesaPenal.objects.filter(uid=uid).first()


def montar_script4(cliente, paragrafo3):
    pedido_principal = cliente.pedido_principal
    absolve_sumaria_como_alternativa = "Sim" if cliente.incluir_absolvicao_como_alternativa else "Não"
    fundamentos_absolvicao = cliente.fundamentos_absolvicao or "Não mencionados"
    reu_preso = "Sim" if cliente.esta_preso else "Não"
    solicita_alvara_soltura = "Sim" if cliente.solicitar_alvara else "Não"
    medidas_cautelares_alternativas = cliente.medidas_cautelares or "Não mencionadas"
    pedido_subsidiario = "Sim" if cliente.incluir_pedido_subsidiario else "Não"
    pedido_subsidiario_qual = cliente.pedido_subsidiario or "Não mencionado"
    requer_nao_recebimento_denuncia = "Sim" if cliente.requerer_nao_recebimento_denuncia else "Não"
    requer_prioridade_tramitacao = "Sim" if cliente.requerer_prioridade else "Não"
    requer_acesso_provas_diligencias = "Sim" if cliente.requerer_acesso_provas else "Não"
    quais_provas_diligencias = cliente.quais_provas or "Não mencionado"
    observacoes_finais = cliente.outros_pedidos or "Não mencionadas"


    prompt = f"""
Com base nas informações abaixo, redija o **quarto parágrafo** da defesa prévia, considerando os pedidos principais e subsidiários, os fundamentos legais e as observações finais do caso. O parágrafo deve ser claro, jurídico e concluir a peça com base nos dados fornecidos. Mantenha coesão com o parágrafo 3 abaixo):

- Pedido principal: {pedido_principal}
- Absolvição sumária como alternativa: {absolve_sumaria_como_alternativa}
- Fundamentos para a absolvição sumária: {fundamentos_absolvicao}
- Réu preso atualmente: {reu_preso}
- Solicita alvará de soltura: {solicita_alvara_soltura}
- Medidas cautelares alternativas: {medidas_cautelares_alternativas}
- Pedido subsidiário: {pedido_subsidiario}
- Pedido subsidiário qual: {pedido_subsidiario_qual}
- Requer não recebimento da denúncia: {requer_nao_recebimento_denuncia}
- Requer prioridade na tramitação: {requer_prioridade_tramitacao}
- Requer acesso às provas/diligências: {requer_acesso_provas_diligencias}
- Quais provas/diligências requer: {quais_provas_diligencias}
- Observações finais: {observacoes_finais}

Requisitos para o parágrafo:
- quero que faça como tivesse regindo uma petição ou seja oq escrever aqui o juiz vai ler
1. Conclusão da peça de defesa, abordando os pedidos finais e fundamentos jurídicos do caso;
2. Enfoque no pedido principal de absolvição, alternativas e medidas cautelares;
3. Manter a conexão com o parágrafo 3 abaixo:
{paragrafo3}
    """

    print(f'\n\nPrompt enviado ao modelo:\n{prompt}')

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text


def buscar_clientes_por_uid5(uid):
    return DocumentacaoEJurisprudencia.objects.filter(uid=uid).first()

def montar_script5(cliente, paragrafo):
    # Coletando os dados do cliente e da documentação
    certidao = cliente.certidao
    laudo = cliente.laudo
    testemunha_nome = cliente.testemunha_nome
    testemunha_qualificacao = cliente.testemunha_qualificacao
    jurisprudencias = cliente.jurisprudencias
    incluir_jurisprudencia_apoio = cliente.incluir_jurisprudencia_apoio
    tese_juridica_apoio = cliente.tese_juridica_apoio
    julgado_especifico = cliente.julgado_especifico

    # Exemplo de uso das variáveis - montar um texto com esses dados
    prompt = f"""
Com base nas informações abaixo, redija o quinto parágrafo de uma petição de defesa penal com base na documentação apresentada:

- Certidão relevante: {certidao if certidao else "não fornecida"}
- Laudo técnico ou pericial: {laudo if laudo else "não fornecido"}
- Testemunha: {testemunha_nome if testemunha_nome else "não indicada"}
- Qualificação da testemunha: {testemunha_qualificacao if testemunha_qualificacao else "não informada"}
- Jurisprudências relevantes: {jurisprudencias if jurisprudencias else "não fornecida"}
- Incluir jurisprudência de apoio? {incluir_jurisprudencia_apoio}
- Tese jurídica de apoio: {tese_juridica_apoio if tese_juridica_apoio else "não fornecida"}
- Julgado específico: {julgado_especifico if julgado_especifico else "não fornecido"}

O parágrafo deve conter:
- quero que faça como tivesse regindo uma petição ou seja oq escrever aqui o juiz vai ler
seguindo esse modelo como base pode sofrer alterações se necessarios
5.0 - DOCUMENTAÇÃO E PROVAS (Anexos)
5.1 - Lista de documentos:

Certidões, laudos, testemunhas, jurisprudências (ex.: STJ, STF).

5.2 - Jurisprudência de apoio:

Citar julgados recentes (ex.: *"HC 123.456/STJ: 'A falta de flagrante inviabiliza a prisão preventiva...'"*).
     agora as perguntas pra serem feitas aqui
1. Identificação da documentação relevante apresentada para sustentar a defesa;
2. Menção a laudos técnicos, certidões e testemunhas que possam corroborar a defesa;
3. Referência a jurisprudências que apoiam a tese de defesa;
4. Menção a tese jurídica a ser adotada para a defesa do acusado;
5. Tom formal, jurídico e técnico, adequado ao processo e respeitante à autoridade do juiz.

e use com base o 3 paragrafo {paragrafo}
    """

    print(f'\n\nPrompt enviado ao modelo:\n{prompt}')

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text




def scriptfinal(relatorio1, relatorio2):
    data_atual = datetime.now()
    prompt = f"""
    com base nas informações contidas aqui: {relatorio2}
    e essa: {relatorio1}
    LEMRBADNO QUE HOJE È DIA {data_atual}
faça um paragrafo final para a petição penal com essa base de conhecimento: 6.0 - ASSINATURA
[Local, data] de hoje pf

[Nome do Advogado]

[OAB/UF Nº]"""
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text