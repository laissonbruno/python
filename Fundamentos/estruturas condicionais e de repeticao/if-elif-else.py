saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")
    
    
# /\/\/\/\/\/\//\/\/\/\/\//\/\/\/\//\/\/\/\//\/\/\/\/\/\//\/\/\/

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")
    
    
# /\/\/\/\/\/\//\/\/\/\/\//\/\/\/\//\/\/\/\//\/\/\/\/\/\//\/\/\/
    

opcao = int(input("Informe uma opção: [1] sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")