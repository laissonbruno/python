contatos = {"laisson@gmail.com": {"nome": "laisson", "telefone": "3333-2221"}}

resultado = contatos.pop("laisson@gmail.com")  # {'nome': 'laisson', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("laisson@gmail.com", {})  # {}
print(resultado)