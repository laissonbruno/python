MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

# if idade >= MAIOR_IDADE:
#     print(f'Você tem {idade} e é maior de idade, pode tirar cnh')
# else:
#     print(f'Você só tem {idade} e ainda não pode tirar cnh')
    

if idade >= MAIOR_IDADE:
    print(f'Você tem {idade} e é maior de idade, pode tirar cnh')
elif idade == IDADE_ESPECIAL:
    print(f'Você tem {idade} e pode fazer aulas teóricas, porém não pode fazer aula prática.')
else:
    print(f'Você só tem {idade} e ainda não pode tirar cnh')
    