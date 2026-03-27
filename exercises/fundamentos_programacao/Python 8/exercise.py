import random
import csv

print("Bem-vindo ao jogo de adivinhação! aqui você deverá tentar acertar um número de 0 a 100.")

numero_aleatorio = random.randint(0, 100)

# Var para colocar no csv

tentativas = 0
jogadas = 0

while True:
    chute = int(input("\nDigite o número para tentar adivinhar: "))

    if chute > numero_aleatorio:
        print("O seu número é MAIOR do que o número aleatório")
        tentativas += 1
        continue
    elif chute < numero_aleatorio:
        print("O seu número é MENOR que o número aleatório")
        tentativas += 1
        continue
    else:
        print("Parabéns, você acertou !!!\n")
        jogadas += 1
        break

# Ler

jogadas_passadas = None
tentativas_passadas = None
media_passada = None
recorde_passado = None

with open("dados.csv", "r") as csvfile:
    reader = list(csv.reader(csvfile))

    jogadas_passadas = int(reader[1][0])
    tentativas_passadas = int(reader[1][1])
    media_passada = float(reader[1][2])
    recorde_passado = int(reader[1][3])

# Tratar as variáveis

novas_jogadas = jogadas + jogadas_passadas
novas_tentativas = tentativas + tentativas_passadas
nova_media = (((jogadas_passadas * media_passada) + tentativas) / novas_jogadas)
novo_recorde = recorde_passado if tentativas > tentativas_passadas else tentativas

# Escrever

with open("dados.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['jogadas', 'tentativas', 'media', 'recorde'])
    writer.writerow([novas_jogadas, novas_tentativas, nova_media, novo_recorde])

# Mostrar dados

with open("dados.csv", "r") as csvfile:
    reader = list(csv.reader(csvfile))

    print(f'Você já jogou {reader[1][0]} vezes!')
    print(f'Teve {reader[1][1]} tentativas no total!')
    print(f'A sua média de acertos é: {reader[1][2]}')
    print(f'E o seu recorde foi: {reader[1][3]}')