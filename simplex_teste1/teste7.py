import numpy as np

# Suponha que você tenha uma matriz de restrições A (numpy array) e um vetor RHS (lado direito das restrições).
A = np.array([[2, 1, 1, 0, 0, 100],
              [1, 1, 0, 1, 0, 80],
              [1, 0, 0, 0, 1, 40],
              [-3, -2, 0, 0, 0, 0]], dtype=float)

np.set_printoptions(suppress=True)

# Número de variáveis e restrições
num_variaveis = 2
num_restricoes = 3

# Número máximo de iterações
num_iteracoes = 3


for iteracao in range(num_iteracoes):
    print(f"Iteração {iteracao + 1}:")
    print("Tabela atual:")
    print(A)
    
    # Escolha da variável de entrada (coluna pivot) com o coeficiente mais negativo na linha da função objetivo
    coluna_pivot = np.argmin(A[-1, :-1])
    print(f"Variável de entrada (coluna pivot): x{coluna_pivot + 1}")
    
    divisor = A[:num_restricoes, coluna_pivot]
    if divisor.any() == 0:
        razoes = 10000
    else:
        razoes = A[:num_restricoes, -1] / A[:num_restricoes, coluna_pivot]
    
    # Encontra a linha pivot
    linha_pivot = np.argmin(razoes)
    print(f"Variável de saída (linha pivot): x{linha_pivot + 1}")
    
    # Normalização da linha pivot (dividir pelo elemento pivot)
    elemento_pivot = A[linha_pivot, coluna_pivot]
    A[linha_pivot, :] /= elemento_pivot
    
    # Atualização das outras linhas
    for i in range(num_restricoes + 1):
        print("Esse e o i = ",i)
        if i != linha_pivot:
            fator = -A[i, coluna_pivot]
            print("Esse e o fator", fator)
            A[i, :] += fator * A[linha_pivot, :]
    
    print("Tabela atualizada:")
    print(A)

# A tabela final após duas iterações é a solução ótima
print("Solução ótima:")
print(A)
