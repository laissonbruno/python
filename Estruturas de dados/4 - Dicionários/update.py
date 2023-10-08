contatos = {"laisson@gmail.com": {"nome": "laisson", "telefone": "3333-2221"}}

contatos.update({"laisson@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'laisson@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'laisson@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)