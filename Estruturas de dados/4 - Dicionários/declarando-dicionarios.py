# é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário.

pessoa = {"nome": "tales", "idade": 27}
print(pessoa)

pessoa = dict(nome="tales", idade=27)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "tales", "idade": 27, "telefone": "3333-1234"}
print(pessoa)