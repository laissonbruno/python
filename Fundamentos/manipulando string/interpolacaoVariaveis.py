nome = "Laisson"
idade = 27
profissao = "programador"
linguagem = "python"

# old style (pouco utilizado)
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou no curso de %s." %(nome, idade, profissao, linguagem))

print()
print()
print()
print()

# método format (mesmos problemas do anterior, tendo maior possibilidade de erro)
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print()
print()

# igual o anterior, porém você seleciona o indice da variavel.
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))


print()
print()
print()
print()


# f strings (melhor forma para realizar as interpolações)

print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.')

print()
print()
print()
print()

# formatação de strings com f-string

PI = 3.14159

# irá utilizar apenas duas casas decimais
print(f'Valor de PI: {PI:.2f}')

print()

# irá utilizar apenas três casas decimais
print(f'Valor de PI: {PI:.3f}')