mensagem_para_criptografar = "Too late have I loved you, O Beauty so ancient, O Beauty so new. Too late have I loved you! You were within me but I was outside myself, and there I sought you!"

# Criptografar

lista_mensagem_para_criptografar = list(mensagem_para_criptografar)

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']

for indice, letra in enumerate(lista_mensagem_para_criptografar):
    if not letra.isalpha():
        continue
    if letra == letra.upper():
        indice_inicial = alfabeto.index(letra.lower())
        indice_final = indice_inicial + 1

        lista_mensagem_para_criptografar[indice] = alfabeto[indice_final].upper()
    else:
        indice_inicial = alfabeto.index(letra)
        indice_final = indice_inicial + 1

        lista_mensagem_para_criptografar[indice] = alfabeto[indice_final]

mensagem_criptografada = ''.join(lista_mensagem_para_criptografar)

print(f"A mensagem Criptografada é: {mensagem_criptografada}")

# Descriptografar

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lista_mensagem_para_descriptografrar = list(mensagem_criptografada)

for indice, letra in enumerate(lista_mensagem_para_descriptografrar):
    if not letra.isalpha():
        continue
    if letra == letra.upper():
        indice_inicial = alfabeto.index(letra.lower())
        indice_final = indice_inicial - 1

        lista_mensagem_para_descriptografrar[indice] = alfabeto[indice_final].upper()
    else:
        indice_inicial = alfabeto.index(letra)
        indice_final = indice_inicial - 1

        lista_mensagem_para_descriptografrar[indice] = alfabeto[indice_final]

mensagem_descriptografada = ''.join(lista_mensagem_para_descriptografrar)

print(f"\nA mensagem Descriptografada é: {mensagem_descriptografada}")