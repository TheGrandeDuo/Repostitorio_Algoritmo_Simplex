def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def encontrar_colunaPivot(matriz, iteracao):
    ultima_linha = matriz[-1]
    coluna_pivot = ultima_linha[0]
    
    for i, numero in enumerate(ultima_linha):
        if numero < coluna_pivot:
            coluna_pivot = numero
            indice_coluna_pivot = i  # Adicione esta linha
        else:
            indice_coluna_pivot = 0
    
    print(f"Iteração {iteracao}:")
    print("Coluna Pivot:", coluna_pivot)
    print("Índice Coluna Pivot:", indice_coluna_pivot)  # Adicione esta linha
    
    return indice_coluna_pivot

def encontrar_linhaPivot(rest_semValores, rest_valores, indice_coluna_pivot):
    
    resultados_divisao = [rest_valores[i] / linha[indice_coluna_pivot] for i, linha in enumerate(rest_semValores)]

    if not resultados_divisao:
        return None, None  # Trata a lista vazia

    menor_valor = resultados_divisao[0]
    indice_linha_pivot = 0

    for i, valor in enumerate(resultados_divisao):
        if valor < menor_valor:
            menor_valor = valor
            indice_linha_pivot = i
            
    print("Index Linha Pivot",indice_linha_pivot)
    print("Resultados da Divisão:", resultados_divisao)

    return indice_linha_pivot
    
def separar_ultima_linha(matriz):
    matriz_copia = [linha[:] for linha in matriz]  # Cria uma cópia da matriz original
    ultima_linha = matriz_copia.pop()  # Remove e retorna a última linha da cópia
    return matriz_copia, ultima_linha

def verificaColunaZ(matriz):
    coluna_z = []

    coluna_z.append(separar_ultima_linha(matriz))
    print("Coluna Z",coluna_z)
    
    for linha_z in coluna_z:
        for valor_z in linha_z:
            if (valor_z > 0):
                print("Encerramos")
                return 0
    return 1

def separaMatriz(matriz):
    matriz_copia, ultima_linha = separar_ultima_linha(matriz)
    
    primeiros_elementos = []  # Lista para armazenar os primeiros n-1 elementos
    ultimos_valores = []      # Lista para armazenar os últimos valores

    for linha in matriz_copia:
        primeiros_elementos.append(linha[:-1])  # Adiciona todos os elementos, exceto o último
        ultimos_valores.append(linha[-1])       # Adiciona o último elemento

    print("Primeiros Elementos:", primeiros_elementos)
    print("Ultimos Valores",ultimos_valores)
    
    return primeiros_elementos, ultimos_valores

def elementoPivot(matriz, indice_linha_pivot, indice_coluna_pivot):
    elemento_pivot = matriz[indice_linha_pivot][indice_coluna_pivot]
    #print(elementoPivot)
    return elemento_pivot

def calculaListaFatores(matriz, indice_linha_pivot, indice_coluna_pivot):
    fatores = []
    matriz2, ultimaLinha = separar_ultima_linha(matriz)
    for i in range(len(matriz2)):
        if i != indice_linha_pivot:
            fator = matriz[i][indice_coluna_pivot]
            if fator not in fatores:
                fatores.append(-1*fator)                
    return fatores

def eliminacao_gaussiana(matriz):
    iteracao = 1
    
    valorVerificacao = 2 # Colocar dinamico -> Fazer a funcao funcionar
    
    if valorVerificacao != 0:
        indice_coluna_pivot = encontrar_colunaPivot(matriz, iteracao)
        rest_semValores, rest_valores = separaMatriz(matriz)
        indice_linha_pivot = encontrar_linhaPivot(rest_semValores, rest_valores, indice_coluna_pivot)
        elemento_pivot = elementoPivot(matriz, indice_linha_pivot, indice_coluna_pivot)
        fatores = calculaListaFatores(matriz, indice_linha_pivot, indice_coluna_pivot)
        print("Elemento Pivot",elemento_pivot)
        print("Fatores",fatores)
       
        for coluna in range(len(matriz[indice_linha_pivot])):
            matriz[indice_linha_pivot][coluna] /= elemento_pivot
        
        matriz2, ultimaLinha = separar_ultima_linha(matriz)
        print(matriz2, ultimaLinha)

        for i, linha in enumerate(matriz2):
            #print(i, linha)
            if i != indice_linha_pivot:
                for fator in fatores:  
                    matriz2.append(matriz2[linha][0] + fator)
                    
        
        print("Matriz Mod: ",matriz2)
        # for linha in matriz:
        #     for coluna in linha:
        #         matriz[indice_linha_pivot][coluna] /= elemento_pivot
        # print(matriz)

matriz = [[2, 3, 1, 0, 100],
        [4, 2, 0, 1, 120],
        [-60, -40, 0, 0, 0]]

#eliminacao_gaussiana(matriz)


# Matriz original
matriz_mod = [[2, 3, 1, 0, 100], [1.0, 0.5, 0.0, 0.25, 30.0]]

matriz3 = matriz_mod.copy()

# Índice da linha que você deseja substituir (0 para a primeira linha)
linha_a_substituir = 0

# Lista de fatores
fatores = [-2]

# Índice da outra linha usada para o cálculo (0 para a primeira linha)
outra_posicao = 1

# Realize o cálculo e substitua a linha
matriz_mod[linha_a_substituir] = [x + y * fatores[0] for x, y in zip(matriz_mod[linha_a_substituir], matriz_mod[outra_posicao])]

# Exibir a matriz resultante
print(matriz3)
print(matriz_mod)


#         elemento_pivot = ultima_linha[indice_coluna_pivot]
        
#         if elemento_pivot == 0:
#             print("Não foi possível encontrar um elemento pivot não zero.")
#             break
        
#         for i in range(len(ultima_linha)):
#             ultima_linha[i] /= elemento_pivot
        
#         imprimir_matriz(matriz)
        
#         for i in range(len(matriz)):
#             fator = matriz[i][indice_coluna_pivot]
#             for j in range(len(matriz[i])):
#                 matriz[i][j] -= fator * ultima_linha[j]
        
#         imprimir_matriz(matriz)
        
#         iteracao += 1
#         if iteracao > min(len(matriz), len(matriz[0])):
#             break

# # Matriz Original
# matriz = [[1, 2, 1, 0, 450],
#           [2, 1, 0, 1, 600],
#           [-3, -4, 0, 0, 0]]

# eliminacao_gaussiana(matriz)


# imprimir matriz
# encontrar_indiceLinhaPivot
# encontrar_indiceColunaPivot
# encontrar_elementoPivot
# Eliminaçao Gaussiana
    # Dividr linha[indiceLinhaPivot] / elementoPivot = e adicionar na matriz na posicaoLinhaPivot
    # Demais Linhas
        # Encontrar coeficienteColunaPivot 
        # fator = coeficiente * -1
        # adicionar na matriz novaLinha = linha - (fator * linhaPivot)
        # Imprimir iteracao
        # reiniciar ciclo
        
        
