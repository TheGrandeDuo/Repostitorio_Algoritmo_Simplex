import numpy as np

# Inicialização da matriz (tabela simplex)
A = np.array([[2, 1, 1, 0, 6],
              [1, 2, 0, 1, 4],
              [-3, -2, 0, 0, 0]])

# Número de variáveis e restrições
num_variaveis = 2
num_restricoes = 2

# Número máximo de iterações
num_iteracoes = 2

for iteracao in range(num_iteracoes):
    print(f"Iteração {iteracao + 1}:")
    print("Tabela atual:")
    print(A)
    
    # Escolha da variável de entrada (coluna pivot) com o coeficiente mais negativo na linha da função objetivo
    coluna_pivot = np.argmin(A[-1, :-1])
    print(f"Variável de entrada (coluna pivot): x{coluna_pivot + 1}")
    
    # Cálculo das razões para determinar a variável de saída (linha pivot)
    razoes = A[:num_restricoes, -1] / A[:num_restricoes, coluna_pivot]
    
    # Encontra a linha pivot
    linha_pivot = np.argmin(razoes)
    print(f"Variável de saída (linha pivot): x{linha_pivot + 1}")
    
    # Atualização da tabela
    elemento_pivot = A[linha_pivot, coluna_pivot]
    A[linha_pivot, :] /= elemento_pivot
    
    for i in range(num_restricoes + 1):
        if i != linha_pivot:
            fator = -A[i, coluna_pivot]
            A[i, :] += fator * A[linha_pivot, :]
    
    print("Tabela atualizada:")
    print(A)

# A tabela final após duas iterações é a solução ótima
print("Solução ótima:")
print(A)
