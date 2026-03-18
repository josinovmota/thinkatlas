texto = None

with open("texto.txt", encoding="utf-8") as f:
    texto = f.read()

lista_palavras = texto.split()

texto_sem_repeticao = set(lista_palavras)

dicionario_repeticao = {}

for palavra in texto_sem_repeticao:
    if lista_palavras.count(palavra) > 1:
        dicionario_repeticao[palavra] = lista_palavras.count(palavra)

dicionario_ordenado_por_valor = dict(sorted(dicionario_repeticao.items(), key=lambda item: item[1], reverse=True))

limitando_vinte_valores_do_dicionario = dict(list(dicionario_ordenado_por_valor.items())[:20])

print(limitando_vinte_valores_do_dicionario)