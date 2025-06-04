import requests
from bs4 import BeautifulSoup
import pandas as pd

def bandeiras_estados(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    tabela = soup.find("table", {"class": "wikitable"})
    dados = []

    for linha in tabela.find_all("tr")[1:]:
        colunas = linha.find_all("td")
        if len(colunas) >= 2:
            estado = colunas[1].get_text(strip=True).split("[")[0]

            img_tag = colunas[0].find("img")
            if img_tag:
                # Link da imagem baixa
                src_baixa = "https:" + img_tag["src"]

                # Link da imagem alta (sem /thumb/)
                partes = src_baixa.split("/thumb/")
                if len(partes) > 1:
                    caminho = partes[1].split("/")
                    nome_arquivo = caminho[-1]
                    src_alta = "https://upload.wikimedia.org/wikipedia/commons/" + "/".join(caminho[:-1]) + "/" + nome_arquivo
                else:
                    src_alta = src_baixa
            else:
                src_baixa = src_alta = None

            dados.append({
                "Estado": estado,
                "Bandeira_Baixa": src_baixa,
                "Bandeira_Alta": src_alta
            })

    return pd.DataFrame(dados)

# Executa e salva
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
df_bandeiras = bandeiras_estados(url)
df_bandeiras.to_csv("bandeiras_estados.csv", index=False, encoding="utf-8-sig")