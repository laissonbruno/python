# operadores logicos


saldo = 1000
saque = 200
limite = 100
conta_especial = True

# operador and

saldo >= saque and saque <= limite

# operador or

saldo >= saque or saque <= limite

# operador not (inverte o resultado)

valor = not 1000 > 1500
print(valor)

# parenteses

saldo >= saque and saque <= limite or conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

