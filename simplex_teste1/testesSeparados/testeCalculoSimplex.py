matriz = [[1, 2, 1, 0, 450],
          [2, 1, 0, 1, 600],
          [-3, -4, 0, 0, 0]]

ultima_linha = matriz[-1]
print(ultima_linha)

# Inicialize a variável "coluna_pivot" com o primeiro elemento da lista
coluna_pivot = ultima_linha[0]

# Use um loop for para comparar cada elemento com o valor atual de "coluna_pivot"
menor = ultima_linha[0]
indice_linha_pivot = 0
for i, numero in enumerate(ultima_linha):
    if numero < menor:
        menor = numero
        posicao = i
coluna_pivot = menor

print("Coluna Pivot:",coluna_pivot)
print("Indice Coluna Pivot:",indice_linha_pivot)

# Matriz Original
matriz2 = [[1, 2, 1, 0, 450],
          [2, 1, 0, 1, 600]]

primeiros_elementos = []  # Lista para armazenar os primeiros n-1 elementos
ultimos_valores = []      # Lista para armazenar os últimos valores

for linha in matriz2:
    primeiros_elementos.append(linha[:-1])  # Adiciona todos os elementos, exceto o último
    ultimos_valores.append(linha[-1])       # Adiciona o último elemento

print("Primeiros Elementos:", primeiros_elementos)
print("Ultimos Valores",ultimos_valores)

valores_col_pivot = []

# Dividir coef resultados / coef col pivot
for linha in matriz2:
    valores_col_pivot.append(linha[indice_linha_pivot])
print("Valores Coluna Pivot:", valores_col_pivot)

resultados_divisao = []

for i in range(len(ultimos_valores)):
    resultado = ultimos_valores[i] / valores_col_pivot[i]
    resultados_divisao.append(resultado)

print("Resultados da Divisão:", resultados_divisao)

# Encontre o índice do menor valor na lista
indice_coluna_pivot = resultados_divisao.index(min(resultados_divisao))

print("Índice Linha Pivot:", indice_coluna_pivot)

# Encontrando o elemento pivot
elemento_pivot = matriz2[indice_linha_pivot][indice_coluna_pivot]

print("Elemento Pivot:", elemento_pivot)

# Use um loop for para realizar a divisão
for i in range(len(matriz2[indice_linha_pivot])):
    matriz2[indice_linha_pivot][i] /= elemento_pivot

# Realize a eliminação gaussiana para zerar os elementos abaixo do elemento de pivô
for i in range(len(matriz2)):
    if i != indice_linha_pivot:
        fator = matriz2[i][indice_coluna_pivot]  # Obtenha o fator de multiplicação
        for j in range(len(matriz2[i])):
            matriz2[i][j] -= fator * matriz2[indice_linha_pivot][j]

# Imprima a matriz após a eliminação gaussiana
print("Matriz após a eliminação gaussiana:")
for linha in matriz2:
    print(linha)

# print("Matriz após a divisão:")
# for linha in matriz2:
#     print(linha)

# fatores = []

# for i, linha in enumerate(matriz2):
#     if i != indice_linha_pivot:
#         print("Linha",linha)    
#         fatores.append(linha[indice_coluna_pivot]*-1)       
# print(fatores)
# print(matriz2)




# Obter elemento PIVOT
    # Encontrar menor termo (mais negativo) da coluna Cj
    # Armazenar o index que ele esta
# Varrer as outras listas (no indice obtido) para obter seus coeficientes
# Calcular Z = (coeficientes das colunas) * (coeficientes das funcObj) = Somar e armazenar em lista pos 1, ou seja 1 coluna, 1 elemento da lista

# NovaLinha (indice da linha pivot) = LinhaPivot / Elemento Pivot
    # fator = coeficientes na coluna pivot * -1
# NovasLinhas = pos(LinhaAnterior) - fator(LinhaPivot)

def obtemColunaPivot_e_indiceColunaPivot():
    matriz = [  [1, 2, 1, 0, 450],
                [2, 1, 0, 1, 600],
                [-3, -4, 0, 0, 0]   ]

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
    coluna_pivot = menor

    print("Coluna Pivot:",coluna_pivot)
    print("Indice Coluna Pivot:",posicao)

    return 0

    
     