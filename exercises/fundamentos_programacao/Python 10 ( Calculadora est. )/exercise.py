import math

lista_digitada_pelo_usuario = [1,4,5,7,3,2,123,512,3,121,7,5,3,1,6,8,9,421,214,321]

def media(lista):
    return (sum(lista) / len(lista))

def mediana(lista):
    lista_exemplo = sorted(lista)
    tamanho_lista = len(lista_exemplo)
    if tamanho_lista % 2 != 0:
        return lista_exemplo[tamanho_lista // 2]
    else:
        primeiro = lista_exemplo[(tamanho_lista // 2) - 1]
        segundo = lista_exemplo[tamanho_lista // 2]

        return (primeiro + segundo) / 2
    
def moda(lista):
    valor_com_mais_frequencia = 0
    lista_mais_frequentes = []

    for valor in lista:
        valor_com_mais_frequencia = valor if lista.count(valor) > valor_com_mais_frequencia else valor_com_mais_frequencia

    for valor in lista:
        if lista.count(valor) == lista.count(valor_com_mais_frequencia):
            lista_mais_frequentes.append(valor)

    return set(lista_mais_frequentes)

# Formula da variance = somatório de cada indice - a média ao quadrado sobre o numero total
def variance(lista):
    denominador = len(lista)
    media_lista = media(lista)
    numerador = 0

    for valor in lista:
        numerador += ((valor - media_lista) ** 2)

    return (numerador / denominador)

def st_deviation(lista):
    return math.sqrt(variance(lista))


def get_metrics(lista_digitada_pelo_usuario):
    # O que eu faço aqui fere o pep-8, mas é só por fins didáticos de aprender unpack
    return media(lista_digitada_pelo_usuario), mediana(lista_digitada_pelo_usuario), moda(lista_digitada_pelo_usuario), variance(lista_digitada_pelo_usuario), st_deviation(lista_digitada_pelo_usuario)

if __name__ == "__main__":
    lista_digitada_pelo_usuario = [1,4,5,7,3,2,123,512,3,121,7,5,3,1,6,8,9,421,214,321]

    # O que eu faço aqui fere o pep-8, mas é só por fins didáticos de aprender unpack
    media, mediana, moda, variance, st_deviation = get_metrics(lista_digitada_pelo_usuario.copy())

    print(f"""\nA média é: {media}\nA mediana é: {mediana}\nA moda é: {moda}\nA variance é: {variance}\nA standard deviation é: {st_deviation}""")