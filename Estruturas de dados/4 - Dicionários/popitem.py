contatos = {"laisson@gmail.com": {"nome": "laisson", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('laisson@gmail.com', {'nome': 'laisson', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError