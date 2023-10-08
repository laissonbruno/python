contatos = {"tales@gmail.com": {"nome": "tales", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["tales@gmail.com"] = {"nome": "Gui"}

print(contatos["tales@gmail.com"])  # {"nome": "tales", "telefone": "3333-2221"}

print(copia["tales@gmail.com"])  # {"nome": "Gui"}