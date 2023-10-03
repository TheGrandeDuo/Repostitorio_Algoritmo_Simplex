import numpy as np

# Função de custo
c = np.array([-60, -40], dtype=float)

# Coeficientes das restrições
A = np.array([[2, 3],
              [4, 2]], dtype=float)

# Lados direitos das restrições
b = np.array([100, 120], dtype=float)

# Inicialização
x = np.array([0, 0], dtype=float)

while True:
    # Passo 2: Teste de otimização
    reduced_costs = c - np.dot(x, A)
    if all(reduced_costs >= 0):
        break

    # Passo 3: Escolha da variável de entrada
    entering_var = np.argmin(reduced_costs)

    # Passo 4: Escolha da variável de saída
    candidate_ratios = b / A[:, entering_var]
    
    # Trata divisão por zero
    valid_ratios = [ratio if ratio > 0 else np.inf if ratio == 0 else -np.inf for ratio in candidate_ratios]
    
    if all(ratio == -np.inf for ratio in valid_ratios):
        print("Problema ilimitado.")
        break

    # Encontra o índice mínimo manualmente
    min_ratio_index = None
    min_ratio_value = np.inf
    for i, ratio in enumerate(valid_ratios):
        if ratio < min_ratio_value:
            min_ratio_index = i
            min_ratio_value = ratio

    leaving_var = min_ratio_index

    # Passo 5: Atualização da base
    pivot_element = A[leaving_var, entering_var]
    A[leaving_var, :] /= pivot_element
    b[leaving_var] /= pivot_element
    for i in range(len(A)):
        if i != leaving_var:
            factor = A[i, entering_var]
            A[i, :] -= factor * A[leaving_var, :]
            b[i] -= factor * b[leaving_var]
    x[entering_var] = b[leaving_var]

# Verifica se a solução é factível antes de imprimir os resultados ótimos
if all(b >= 0):
    print("Solução ótima:")
    print("x1 =", x[0])
    print("x2 =", x[1])
    print("Valor ótimo (Z) =", -np.dot(c, x))
