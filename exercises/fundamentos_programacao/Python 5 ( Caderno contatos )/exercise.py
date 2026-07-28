import csv

dicionario_nome_telefone = {}
lista_dicionarios = []

while True:
    dicionario_nome_telefone['nome'] = str(input("Digite o nome que você deseja armazenar: "))
    dicionario_nome_telefone['telefone'] = str(input("Digite o telefone que você deseja armazenar: "))

    lista_dicionarios.append(dicionario_nome_telefone)
    dicionario_nome_telefone = {}

    escolha = int(input("Deseja continuar adiconando? se sim digite (1), se não, digite (2) "))

    if escolha == 2:
        break

with open('dados.csv', 'w', newline='') as csvfile:
    field_names = ['nome', 'telefone']
    writer = csv.DictWriter(csvfile, fieldnames = field_names)

    writer.writeheader()
    for item in lista_dicionarios:
        writer.writerow(item)