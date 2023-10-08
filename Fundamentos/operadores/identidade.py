# operadores de identidade são utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200


# operador de identidade ( is )
curso is nome_curso

# negacao
curso is not nome_curso

# comparando
saldo is limite