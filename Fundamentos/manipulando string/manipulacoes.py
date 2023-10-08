curso = "pYtHoN"

# deixa todas letras maiusculas
print(curso.upper())

# deixa todas letras minusculas
print(curso.lower())

# deixa a primeira letra maiscula (capitalização da palavra)
print(curso.title())


# eliminando espaços
curso_2 = "         Python    "


# elimina o espaço na esquerda e direita
print(curso_2.strip())

# elimina o espaço na esquerda
print(curso_2.lstrip())

# elimina o espaço na direita
print(curso_2.rstrip())



# junções e centralizações

curso_3 = "Python"

# centralizar a string
# argumento 1 = numero de caracteres que você quer adicionar
# qual caractere que você quer adicionar(opcional)
print(curso_3.center(10, '#'))


# forma para juntar a string
print(".".join(curso))