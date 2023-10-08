# conjuntos não suportam indexação, você deve converter o set para uma lista

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])