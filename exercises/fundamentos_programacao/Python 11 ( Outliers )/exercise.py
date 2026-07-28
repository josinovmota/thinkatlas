import pandas as pd

df = pd.read_csv("dados_outliers.csv")

def mediana(lista):
    lista_exemplo = sorted(lista)
    tamanho_lista = len(lista_exemplo)
    if tamanho_lista % 2 != 0:
        return lista_exemplo[tamanho_lista // 2]
    else:
        primeiro = lista_exemplo[(tamanho_lista // 2) - 1]
        segundo = lista_exemplo[tamanho_lista // 2]

        return (primeiro + segundo) / 2

def outlier_detector(column, name):
    data = column.copy()
    data = sorted(data)
    n = len(data)

    q2 = mediana(data)

    if n % 2 == 0:
        lower_half = data[:n // 2]
        upper_half = data[n // 2:]
    else:
        lower_half = data[:n // 2]
        upper_half = data[n // 2 + 1:]

    q1 = mediana(lower_half)
    q3 = mediana(upper_half)

    iqr = q3 - q1

    lower = q1 - (1.5 * iqr)
    upper = q3 + (1.5 * iqr)

    lower_outliers = [number for number in data if number < lower]
    upper_outliers = [number for number in data if number > upper]

    print(f"Na categoria {name}\nOs valores ABAIXO de Q1−1.5×IQR são: {lower_outliers}\nE os ACIMA de Q3+1.5×IQR são: {upper_outliers}\n")

outlier_detector(list(df["vendas_diarias"]), "Vendas Diarias")
outlier_detector(list(df["preco_unitario"]), "Preço Unitário")
outlier_detector(list(df["estoque"]), "Estoque")