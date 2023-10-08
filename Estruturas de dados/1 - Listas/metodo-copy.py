# irá criar uma copia da lista

lista = [1, "Python", [40, 30, 20]]

lista2 = lista.copy()

print(lista2)  # [1, "Python", [40, 30, 20]]

print(id(lista2), id(lista))

