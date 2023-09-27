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

# Função para verificar se a solução é ótima
def solucao_otima(A):
    return all(A[-1, :-1] >= 0)

# Número máximo de iterações
num_iteracoes = 3

for iteracao in range(num_iteracoes):
    print(f"Iteração {iteracao + 1}:")
    print("Tabela atual:")
    print(A)

    if solucao_otima(A):
        print("Solução ótima encontrada!")
        break

    # Escolha da variável de entrada (coluna pivot) com o coeficiente mais negativo na linha da função objetivo
    coluna_pivot = np.argmin(A[-1, :-1])
    print(f"Variável de entrada (coluna pivot): x{coluna_pivot + 1}")

    # Cálculo das razões para determinar a variável de saída (linha pivot)
    divisor = A[:num_restricoes, coluna_pivot]
    divisor = divisor.astype(int)
    
    for div in divisor:
        if div == 0:
            razoes = 100000000
        else:
            razoes = A[:num_restricoes, -1] / div
            razoes.astype(int)
    
    print("DIV = ",divisor)
    #razoes = np.where(divisor.any() == 0, np.inf, A[:num_restricoes, -1] / divisor)

    # Encontra a linha pivot
    linha_pivot = np.argmin(razoes)
    print(f"Variável de saída (linha pivot): x{linha_pivot + 1}")

    # Normalização da linha pivot (dividir pelo elemento pivot)
    elemento_pivot = A[linha_pivot, coluna_pivot]
    A[linha_pivot, :] /= elemento_pivot

    # Atualização das outras linhas
    for i in range(num_restricoes + 1):
        if i != linha_pivot:
            fator = -A[i, coluna_pivot]
            A[i, :] += fator * A[linha_pivot, :]

    print("Tabela atualizada:")
    print(A)

# A tabela final após as iterações é a solução ótima
print("Solução ótima:")
print(A)
