# Vou considerar + - * /
# Coloquei apenas a parte inteira da divisão à fim de tornar mais simples :)

import re

calculo = str(input("Escreva o cálculo que você quer saber a resposta: "))

multiplicacao_regex = re.compile(r'(\d)+ (\*)+ (\d)+')
divisao_regex = re.compile(r'(\d)+ (/)+ (\d)+')
soma_regex = re.compile(r'(\d)+ (\+)+ (\d)+')
subtracao_regex = re.compile(r'(\d)+ (-)+ (\d)+')

while(calculo.count("*") != 0):
    mo = multiplicacao_regex.search(calculo)
    parte_anterior = mo.group()

    conta_splitada = parte_anterior.split()

    parte1 = int(conta_splitada[0])
    parte2 = int(conta_splitada[2])

    nova_parte = str(parte1 * parte2)

    calculo = calculo.replace(parte_anterior, nova_parte)

while(calculo.count("/") != 0):
    mo = divisao_regex.search(calculo)
    parte_anterior = mo.group()

    conta_splitada = parte_anterior.split()

    parte1 = int(conta_splitada[0])
    parte2 = int(conta_splitada[2])

    nova_parte = str(parte1 // parte2)

    calculo = calculo.replace(parte_anterior, nova_parte)

while(calculo.count("+") != 0):
    mo = soma_regex.search(calculo)
    parte_anterior = mo.group()

    conta_splitada = parte_anterior.split()

    parte1 = int(conta_splitada[0])
    parte2 = int(conta_splitada[2])

    nova_parte = str(parte1 + parte2)

    calculo = calculo.replace(parte_anterior, nova_parte)

while(calculo.count("-") != 0):
    mo = subtracao_regex.search(calculo)
    parte_anterior = mo.group()

    conta_splitada = parte_anterior.split()

    parte1 = int(conta_splitada[0])
    parte2 = int(conta_splitada[2])

    nova_parte = str(parte1 - parte2)

    calculo = calculo.replace(parte_anterior, nova_parte)

print(calculo)