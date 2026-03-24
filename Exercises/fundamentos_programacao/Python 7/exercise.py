import os

cwd = os.getcwd()

print("Vamos percorrer a pasta `ConfigLol` encontrada no mesmo diretório que este exercício.\n")

for root, diretorio, arquivo in os.walk(cwd + "\\ConfigLol"):
    if diretorio and arquivo:
        print(f"Dentro do caminho: `{root}`\ntemos os diretorios: {diretorio} e os arquivos: {arquivo}\n\n")
    if diretorio:
        print(f"Dentro do caminho: `{root}`\ntemos os diretorios: {diretorio} e não temos arquivos\n\n")
    if arquivo:
        print(f"Dentro do caminho: `{root}`\nnão temos os diretorios, porém temos os arquivos: {arquivo}\n\n")