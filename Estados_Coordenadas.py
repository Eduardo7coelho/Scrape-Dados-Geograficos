import pandas as pd

# Dicionário com coordenadas centralizadas por sigla
coords_estados = {
    "Acre": [-8.77, -70.55, "Norte"],
    "Alagoas": [-9.62, -36.82, "Nordeste"],
    "Amazonas": [-3.47, -65.10, "Norte"],
    "Amapá": [1.41, -51.77, "Norte"],
    "Bahia": [-13.29, -41.71, "Nordeste"],
    "Ceará": [-5.20, -39.53, "Nordeste"],
    "Distrito Federal": [-15.83, -47.86, "Centro-Oeste"],
    "Espírito Santo": [-19.19, -40.34, "Sudeste"],
    "Goiás": [-15.98, -49.86, "Centro-Oeste"],
    "Maranhão": [-5.42, -45.44, "Nordeste"],
    "Mato Grosso": [-12.64, -55.42, "Centro-Oeste"],
    "Mato Grosso do Sul": [-20.51, -54.54, "Centro-Oeste"],
    "Minas Gerais": [-18.10, -44.38, "Sudeste"],
    "Pará": [-3.79, -52.48, "Norte"],
    "Paraíba": [-7.28, -36.72, "Nordeste"],
    "Paraná": [-24.89, -51.55, "Sul"],
    "Pernambuco": [-8.38, -37.86, "Nordeste"],
    "Piauí": [-6.60, -42.28, "Nordeste"],
    "Rio de Janeiro": [-22.25, -42.66, "Sudeste"],
    "Rio Grande do Norte": [-5.81, -36.59, "Nordeste"],
    "Rondônia": [-10.83, -63.34, "Norte"],
    "Rio Grande do Sul": [-30.17, -53.50, "Sul"],
    "Roraima": [1.99, -61.33, "Norte"],
    "Santa Catarina": [-27.45, -50.95, "Sul"],
    "Sergipe": [-10.57, -37.45, "Nordeste"],
    "São Paulo": [-22.19, -48.79, "Sudeste"],
    "Tocantins": [-9.46, -48.26, "Norte"]
}

df_coords = pd.DataFrame(coords_estados)

df_coords.to_csv("Coordenadas_Estados.csv", index=False, encoding="utf-8-sig")