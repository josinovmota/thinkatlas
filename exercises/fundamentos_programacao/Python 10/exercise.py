lista_digitada_pelo_usuario = [1,4,5,7,3,2,123,512,3,121,7,5,3,1,6,8,9,421412,213124,321]

def media(lista):
    return (sum(lista) / len(lista))

def mediana(lista):
    lista_exemplo = sorted(lista)
    tamanho_lista = len(lista_exemplo)
    print(tamanho_lista // 2)
    if tamanho_lista % 2 != 0:
        return lista_exemplo[tamanho_lista // 2]
    else:
        primeiro = lista_exemplo[tamanho_lista // 2]
        segundo = lista_exemplo[(tamanho_lista // 2) + 1]

        return (primeiro+ segundo) / 2
    
def moda(lista):
    valor_com_mais_frequencia = 0
    lista_mais_frequentes = []

    for valor in lista:
        valor_com_mais_frequencia = valor if lista.count(valor) > valor_com_mais_frequencia else valor_com_mais_frequencia

    for valor in lista:
        if lista.count(valor) == lista.count(valor_com_mais_frequencia):
            lista_mais_frequentes.append(valor)

    return set(lista_mais_frequentes)

def variance(lista):
    

print(f"""A média é: {media(lista_digitada_pelo_usuario)}
A mediana é: {mediana(lista_digitada_pelo_usuario)}
A moda é: {moda(lista_digitada_pelo_usuario)}
A variance é: {variance(lista_digitada_pelo_usuario)}
A standard deviation é: {standard_d(lista_digitada_pelo_usuario)}
""")