saldo = 2000
# saque = 200
# saque = 2500


status = "sucesso" if saldo >= saque else "Falha"

print(f'{status} ao realizado o saque')