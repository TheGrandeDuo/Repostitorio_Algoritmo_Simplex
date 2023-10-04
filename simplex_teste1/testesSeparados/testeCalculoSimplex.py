matriz = [[1, 2, 1, 0, 450],
          [2, 1, 0, 1, 600],
          [-3, -4, 0, 0, 0]]

ultima_linha = matriz[-1]
print(ultima_linha)

# Inicialize a variável "coluna_pivot" com o primeiro elemento da lista
coluna_pivot = ultima_linha[0]

# Use um loop for para comparar cada elemento com o valor atual de "coluna_pivot"
menor = ultima_linha[0]
posicao = 0
for i, numero in enumerate(ultima_linha):
    if numero < menor:
        menor = numero
        posicao = i
print("Coluna Pivot:",coluna_pivot)
print("Posicao Coluna Pivot:",posicao)

# Matriz original
matriz2 = [[1, 2, 1, 0, 450],
          [2, 1, 0, 1, 600]]

# Coluna pela qual você deseja dividir (coluna 1)
coluna_divisor = coluna_pivot[posicao]

# Valor pelo qual você deseja dividir
divisor = coluna_pivot[posicao]  # Neste exemplo, estamos dividindo por 2

# Inicialize uma nova matriz para armazenar os resultados
matriz_resultante = []

# Itere pelas linhas da matriz original
for linha in matriz:
    linha_resultante = []  # Inicialize uma linha vazia para armazenar os resultados da linha atual
    
    # Itere pelos elementos da linha
    for i, elemento in enumerate(linha):
        if i == coluna_divisor:  # Verifique se estamos na coluna desejada
            resultado = elemento / divisor  # Realize a divisão
            linha_resultante.append(resultado)  # Adicione o resultado à linha resultante
    
    matriz_resultante.append(linha_resultante)  # Adicione a linha resultante à matriz resultante

# Exiba a matriz resultante
for linha in matriz_resultante:
    print(linha)
print(matriz_resultante)