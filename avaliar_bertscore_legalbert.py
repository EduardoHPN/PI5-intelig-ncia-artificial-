import pandas as pd
from bert_score import score
from transformers import AutoTokenizer

# 1. Carregar o CSV
df = pd.read_csv("comparativo_peticoes.csv")

# 2. Verificação das colunas
if not {"peticao_ia", "peticao_referencia"}.issubset(df.columns):
    raise ValueError("O CSV deve conter as colunas 'peticao_ia' e 'peticao_referencia'.")

peticoes_ia = df["peticao_ia"].astype(str).tolist()
peticoes_ref = df["peticao_referencia"].astype(str).tolist()

# 3. Usar modelo compatível
modelo = "neuralmind/bert-base-portuguese-cased"
tokenizer = AutoTokenizer.from_pretrained(modelo)

# 4. Truncamento
def truncar_para_512_tokens(texto):
    inputs = tokenizer(
        texto,
        max_length=512,
        truncation=True,
        return_tensors="pt",
        return_attention_mask=False,
        return_token_type_ids=False
    )
    return tokenizer.decode(inputs["input_ids"][0], skip_special_tokens=True)

peticoes_ia_truncadas = [truncar_para_512_tokens(txt) for txt in peticoes_ia]
peticoes_ref_truncadas = [truncar_para_512_tokens(txt) for txt in peticoes_ref]

# 5. Calcular BERTScore
PREC, REC, F1 = score(
    cands=peticoes_ia_truncadas,
    refs=peticoes_ref_truncadas,
    lang="pt",
    model_type=modelo,
    num_layers=12,  # importante!
    verbose=True
)

# 6. Adicionar resultados ao DataFrame e salvar
df["bertscore_f1"] = F1.tolist()
df.to_csv("comparativo_peticoes_com_bertscore.csv", index=False, encoding="utf-8")

# 7. Exibir resumo
for idx, row in df.iterrows():
    print(f"Petição {idx+1} - BERTScore F1: {row['bertscore_f1']:.4f}")

print(f"\n📊 Média Geral do BERTScore (F1): {F1.mean().item():.4f}")
print("\n✅ Resultado salvo em: comparativo_peticoes_com_bertscore.csv")
