texto = input("Informe um texto: ")
VOGAIS = "AEIOU"



# exemplo de iteração
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()



# exemplos com range
for numero in range(11):
    print(numero, end=" ")


# tabuada do 5

for numero in range(0, 51, 5):
    print(numero, end=" ")

