import csv

# Percebi que cometi alguns erros como magic value na linha 13
# e o len(dicionario) na linha 24 ( deveria ser um `len(rows)) - 1` )

def exercise(rows):

    lista_nomes = rows[0]
    dicionario = {nome: [] for nome in lista_nomes}
    tipos_de_colunas = []

    for data in rows[1:]:
        for x in range(8):
            if data[x] == "":
                dicionario[lista_nomes[x]].append("NaN")
            else:
                if data[x].isalpha():
                    tipos_de_colunas.append("Texto")
                else:
                    tipos_de_colunas.append("Numérico")
                
                dicionario[lista_nomes[x]].append(data[x])

    contagem_de_linhas = len(dicionario)
    print(f"Cada coluna do dicionário tem {contagem_de_linhas} dados\n")

    for idx, key in enumerate(dicionario):
        contagem_nan_values = dicionario[key].count("NaN")
        
        print(f"A coluna {key} tem o tipo: {tipos_de_colunas[idx]} e a quantidade {contagem_nan_values} de valores nulos")

with open("exercises/fundamentos_programacao/Python 9/dados_mistos.csv", encoding="utf-8-sig") as df:
    reader = csv.reader(df)
    exercise(list(reader))
