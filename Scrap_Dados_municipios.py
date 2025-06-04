import requests
import pandas as pd
import re

HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_tables_from_wikipedia(url):
    response = requests.get(url, headers=HEADERS)
    return pd.read_html(response.text, flavor="lxml")

def limpar_numero(texto):
    """Remove espaços, vírgulas e \xa0 de números e converte para int."""
    return float(re.sub(r"[^\d]", "", str(texto)))

def normalizar_nome(nome):
    return str(nome).strip().lower()

# --- POPULAÇÃO ---
url_pop = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o_(2022)"
df_pop = get_tables_from_wikipedia(url_pop)[0]
df_pop["População"] = df_pop["População"].apply(limpar_numero)
df_pop["Município"] = df_pop["Município"].replace("Brasília[nota 1]", "Brasília")
df_pop.drop(columns=["Posição"], inplace=True)

# --- ÁREA ---
url_area = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_brasileiros_por_%C3%A1rea_decrescente"
df_area = get_tables_from_wikipedia(url_area)[0]
df_area["Área (km²)"] = df_area["Área (km²)"].apply(limpar_numero)
df_area.drop(columns=["Posição"], inplace=True)

# --- CIDADES LITORÂNEAS ---
url_litoral = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_litor%C3%A2neos_do_Brasil"
df_litoral = get_tables_from_wikipedia(url_litoral)

# Extrai nomes normalizados dos municípios litorâneos
cidades_litoraneas = set()
for tabela in df_litoral:
    if "Município" in tabela.columns or "Municípios" in tabela.columns:
        col = "Municípios" if "Municípios" in tabela.columns else "Município"
        cidades = tabela[col].dropna().apply(normalizar_nome)
        cidades_litoraneas.update(cidades)

# --- ADICIONA COLUNA LITORÂNEA ---
df_area["Municipio_normalizado"] = df_area["Município"].apply(normalizar_nome)
df_area["Litoraneo"] = df_area["Municipio_normalizado"].apply(lambda x: 1 if x in cidades_litoraneas else 0)

# Normaliza os nomes nos dois DataFrames
df_pop["Municipio_normalizado"] = df_pop["Município"].apply(normalizar_nome)

# Junta os dois DataFrames com base no nome normalizado
df_area["Chave"] = df_area["Município"].str.lower().str.strip() + " - " + df_area["Unidade federativa"].str.lower().str.strip()
df_pop["Chave"] = df_pop["Município"].str.lower().str.strip() + " - " + df_pop["Unidade federativa"].str.lower().str.strip()

df_final = pd.merge(
    df_area,
    df_pop[["Chave", "População"]],
    on="Chave",
    how="inner"
)

df_final.drop(columns=["Chave"], inplace=True)

# Ordena colunas
df_final = df_final[["Município", "Unidade federativa", "População", "Área (km²)", "Litoraneo"]]

# Salva em CSV
df_final.to_csv("Dados_Municipios.csv", index=False, encoding="utf-8-sig")

# Dataframe Área litorânea dos estados
df_est_litoral = df_litoral[1]

# Salva em CSV
df_est_litoral.to_csv("Estados_Litoral.csv", index=False, encoding="utf-8-sig")