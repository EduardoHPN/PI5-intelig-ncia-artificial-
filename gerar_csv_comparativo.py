import os
import pandas as pd

# Pastas com as petições da IA e as petições de referência
PASTA_IA = "peticoes_geradas"
PASTA_REF = "peticoes_referencia"

dados = []

# Percorrer os arquivos da IA
for nome_arquivo in os.listdir(PASTA_IA):
    if not nome_arquivo.endswith(".txt"):
        continue

    caminho_ia = os.path.join(PASTA_IA, nome_arquivo)

    # Tenta extrair o UID para buscar a petição de referência correspondente
    try:
        uid = nome_arquivo.split("_")[1]
    except IndexError:
        print(f"Nome de arquivo inválido: {nome_arquivo}")
        continue

    caminho_ref = os.path.join(PASTA_REF, f"peticao_{uid}.txt")
    if not os.path.exists(caminho_ref):
        print(f"Petição de referência não encontrada para UID: {uid}")
        continue

    # Leitura dos arquivos
    with open(caminho_ia, "r", encoding="utf-8") as f:
        texto_ia = f.read()

    with open(caminho_ref, "r", encoding="utf-8") as f:
        texto_ref = f.read()

    dados.append({
        "uid": uid,
        "peticao_ia": texto_ia,
        "peticao_referencia": texto_ref
    })

# Salva em CSV
df = pd.DataFrame(dados)
df.to_csv("comparativo_peticoes.csv", index=False, encoding="utf-8")
print("Arquivo comparativo_peticoes.csv criado com sucesso.")
