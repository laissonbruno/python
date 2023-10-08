carros = ['gol', 'celta', 'palio']

for carro in carros:
    print(carro) 
    
# função enumerate - utilizada para saber o indice do iteravel

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')