texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

# transforma texto em uma lista com índices

texto_splitado = texto.split()
copia_texto_splitado = texto.split()

# itera palavra e índice

for indice, valor in enumerate(texto_splitado):
    if indice % 3 == 0 and indice % 5 == 0 and indice != 0:
        copia_texto_splitado[indice] = "FizzBuzz"
    elif indice % 3 == 0 and indice != 0:
        copia_texto_splitado[indice] = "Fizz"
    elif indice % 5 == 0 and indice != 0:
        copia_texto_splitado[indice] = "Buzz"

print(" ".join(copia_texto_splitado))