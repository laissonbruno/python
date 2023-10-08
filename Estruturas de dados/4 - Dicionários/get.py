contatos = {"laisson@gmail.com": {"nome": "laisson", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "laisson@gmail.com", {}
)  # {"laisson@gmail.com": {"nome": "laisson", "telefone": "3333-2221"}
print(resultado)