contato = {"nome": "laisson", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "laisson"
print(contato)  # {'nome': 'laisson', 'telefone': '3333-2221'}

contato.setdefault("idade", 27)  # 27
print(contato)  # {'nome': 'laisson', 'telefone': '3333-2221', 'idade': 27}