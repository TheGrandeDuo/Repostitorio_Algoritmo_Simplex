matriz2 = [
        [2, 1, 1, 0, 0, 16],
        [1, 2, 0, 1, 0, 11],
        ]

fatores = [-1, -2]

lista_pivot = [1, 3, 0, 0, 1, 15]

elemento_pivot = 3

for valor in range(len(lista_pivot)):
    lista_pivot[valor] /= elemento_pivot

# Defina o número de duplicações desejado
numero_de_duplicacoes = 2

# Crie a matriz duplicando a lista
matriz_pivot = [lista_pivot[:] for _ in range(numero_de_duplicacoes)]

indice_linha_pivot = 2

print("Iteracao 0")
print("Matriz Pivot",matriz_pivot)
print("Lista Pivot",lista_pivot)

for linha in range(len(matriz_pivot)):
    for coluna in range(len(matriz_pivot[0])):
        matriz_pivot[linha][coluna] *= fatores[linha]
        #print(f"Matriz: [{linha}][{coluna}]",matriz_pivot[linha][coluna])
        #matriz[i][j] = matriz[i][j] * fatores[i]
        matriz2[linha][coluna] += matriz_pivot[linha][coluna]

print("Iteracao 1")
print("Matriz Pivot",matriz_pivot)
print("Matriz Nao Pivot",matriz2)
print("Lista Pivot",lista_pivot)

matriz2.insert(indice_linha_pivot, lista_pivot)
print("Matriz Resultante",matriz2)

for linha in matriz2:
    print(linha)

