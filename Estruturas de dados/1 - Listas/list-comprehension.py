# cria uma lista com base nos valores de uma outra lista existente(filtro) ou gera uma nova lista aplicando alguma modificação nos elementos de uma lista existente.


# filtros

numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# versão list comprehension

pares = [numero for numero in numeros if numero % 2 == 0]


# modificando valores

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# versão list comprehension
quadrado = [numero ** 2 for numero in numeros]
