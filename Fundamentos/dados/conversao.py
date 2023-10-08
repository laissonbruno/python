# convertendo tipos de dados.


# int para flot e vice-versa

preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10 / 2
print (preco)

preco = int(preco)
print(preco)


# numero para string e vice-versa

preco = 10.50
idade = 27

print(str(preco))
print(str(idade))


# f strings
texto = f'idade {idade} preco {preco}'
print(texto)

preco = "10.50"
idade = "27"

print(float(preco))
print(int(idade))


# erros de conversão

preco = "python"
print(float(preco))

# palavras não podem ser diretamente convertidas em numeros