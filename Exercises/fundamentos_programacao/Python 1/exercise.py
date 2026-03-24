import random

numero_para_acertar = random.randint(0, 100)

print("\nBem-vindo ao jogo de adivinhação\nPara começar, digite o seu palpite e a máquinha dirá se está abaixo ou acima do número certo!\n")

while(True):
    palpite = int(input("Qual o seu palpite? "))

    if palpite > numero_para_acertar:
        print("O número que você escreveu é MAIOR do que o número certo")
        continue
    elif palpite < numero_para_acertar:
        print("O número que você escreveu é MENOR do que o número certo")
        continue
    else:
        print(f"Você acertou, o número correto era o {numero_para_acertar}")
        break