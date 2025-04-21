# recipes/scripts.py
from recipes.models import ClientParagrafOne
import google.generativeai  as genai

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


