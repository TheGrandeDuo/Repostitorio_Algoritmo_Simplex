import copy

def separaPrimeiraIteracao(matriz):
    
    matriz_copia = copy.deepcopy(matriz)
    
    linha_fObj_primeira_iteracao = matriz_copia.pop()
    
    # print("Matriz Copia:", matriz_copia)
    # print("Linha Primeira Iteracao:", linha_fObj_primeira_iteracao)
    
    return linha_fObj_primeira_iteracao

def encontrar_colunaPivot(matriz):
    ultima_linha = matriz[-1]
    coluna_pivot = ultima_linha[0]
    indice_coluna_pivot = 0
        
    for i, numero in enumerate(ultima_linha):
        if (numero > coluna_pivot):
            coluna_pivot = numero
            indice_coluna_pivot = i
    
    print("Coluna Pivot:", coluna_pivot)
    print("Índice Coluna Pivot:", indice_coluna_pivot)
    
    return indice_coluna_pivot

def encontrar_linhaPivot(rest_semValores, rest_valores, indice_coluna_pivot):
    
    resultados_divisao = [10000 if linha[indice_coluna_pivot] == 0 else rest_valores[i] / linha[indice_coluna_pivot] for i, linha in enumerate(rest_semValores)]

    if not resultados_divisao:
        return None, None  # Trata a lista vazia

    menor_valor = 1000000
    indice_linha_pivot = 0

    for i, valor in enumerate(resultados_divisao):
        if valor >= 0:                  # Validacao para que nao pegue numeros negativos
            if valor < menor_valor:
                menor_valor = valor
                indice_linha_pivot = i
                print(menor_valor)
            
    print("Index Linha Pivot:", indice_linha_pivot)
    print("Resultados da Divisão:", resultados_divisao)
    print("Menor Valor",menor_valor)

    return indice_linha_pivot
    
def separar_ultima_linha(matriz):
    matriz_copia = [linha[:] for linha in matriz]  # Cria uma cópia da matriz original
    ultima_linha = matriz_copia.pop()  # Remove e retorna a última linha da cópia
    
    # print("Matriz Copia:", matriz_copia)
    # print("Ultima Linha", ultima_linha)
    
    return matriz_copia, ultima_linha

def separaMatriz(matriz):
    matriz_das_restricoes, ultima_linha = separar_ultima_linha(matriz)
    
    variaveis = []  # Lista para armazenar os primeiros n-1 elementos
    resultados = []      # Lista para armazenar os últimos valores

    for linha in matriz_das_restricoes:
        variaveis.append(linha[:-1])  # Adiciona todos os elementos, exceto o último
        resultados.append(linha[-1])       # Adiciona o último elemento

    # print("Variaveis:", variaveis)
    # print("Resultados:", resultados)
    
    return variaveis, resultados

def elementoPivot(matriz, indice_linha_pivot, indice_coluna_pivot):
    elemento_pivot = matriz[indice_linha_pivot][indice_coluna_pivot]
    
    print("Elemento Pivot:", elemento_pivot)
    
    return elemento_pivot

def calculaListaFatores(matriz, indice_linha_pivot, indice_coluna_pivot):
    fatores = []
    matriz2, ultimaLinha = separar_ultima_linha(matriz)
    for i in range(len(matriz2)):
        if i != indice_linha_pivot:
            fator = matriz[i][indice_coluna_pivot]
            if fator not in fatores:
                fatores.append(-1*fator)
                
    # print("Lista Fatores:", fatores)
    
    return fatores

def calculaLinhaCjZj(valores_vars_basica, variaveis_basicas,indice_linha_pivot, indice_coluna_pivot, teste, matriz_das_restricoes):
    
    # print("Variaveis do padrao (nao modificadas)")
    # print("Variaveis Basicas:", valores_vars_basica)
    # print("Indice Linha:", indice_linha_pivot)
    # print("Indice Coluna:", indice_coluna_pivot)
    # print("Teste:", teste)
    # print("Matriz Restricoes", matriz_das_restricoes)
        
    variaveis_basicas.pop(indice_linha_pivot)
    print("VB",variaveis_basicas)
    variaveis_basicas.insert(indice_linha_pivot, legendas[indice_coluna_pivot])
    print("VB",variaveis_basicas)
    
    valores_vars_basica.pop(indice_linha_pivot)
    valores_vars_basica.insert(indice_linha_pivot, teste[indice_coluna_pivot])
    
    for linha in range(len(matriz_das_restricoes)):
        for coluna in range(len(matriz_das_restricoes[0])):
            matriz_das_restricoes[linha][coluna] *= valores_vars_basica[linha]
                
    soma_listas = [sum(x) for x in zip(*matriz_das_restricoes)]
    
    linha_cjzj = []
    for valor in range(len(teste)):
        linha_cjzj.append(teste[valor] - soma_listas[valor])
    
    # print("Linha Cj-Zj:",linha_cjzj)
    
    return linha_cjzj

def calcula_variaveis_basicas(matriz, rest_semValores):
    print("Matriz",matriz)
    print("Restricoes",rest_semValores)
    
    tamanho_matriz_original = len(matriz[0])
    tamanho_matriz_restricoes_linha = len(rest_semValores)
    tamanho_matriz_restricoes_coluna = len(rest_semValores[0])
    
    
    print("Tamanho Matriz Original",)
    print("Tamanho Matriz Restricoes_Linha",tamanho_matriz_restricoes_linha)
    print("Tamanho Matriz Restricoes_Coluna",tamanho_matriz_restricoes_coluna)
    
    variaveis_basicas = []

    tamanho_var = tamanho_matriz_original - tamanho_matriz_restricoes_linha

    while tamanho_var < tamanho_matriz_original:
        variaveis_basicas.append("x" + str(tamanho_var))
        tamanho_var += 1
        
    print("Variaveis Basicas",variaveis_basicas)
    
    return variaveis_basicas
    

def eliminacao_gaussiana(matriz, variaveis_basicas, valores_var_basica, linha_fObj_primeira_iteracao):
    iteracao = 0
    valores_vars_basica = valores_var_basica
    variaveis_basicas = variaveis_basicas
    
    indice_coluna_pivot = encontrar_colunaPivot(matriz)
    rest_semValores, rest_valores = separaMatriz(matriz)
    indice_linha_pivot = encontrar_linhaPivot(rest_semValores, rest_valores, indice_coluna_pivot)
    elemento_pivot = elementoPivot(matriz, indice_linha_pivot, indice_coluna_pivot)
    fatores = calculaListaFatores(matriz, indice_linha_pivot, indice_coluna_pivot)
    variaveis_basicas = calcula_variaveis_basicas(matriz, rest_semValores)

    matriz_das_restricoes, linha_aux = separar_ultima_linha(matriz)

    teste = linha_fObj_primeira_iteracao
    
    lista_pivot = matriz_das_restricoes.pop(indice_linha_pivot)

    for valor in range(len(lista_pivot)):
        lista_pivot[valor] /= elemento_pivot
    
    num_linhas = len(matriz)-1
    numero_de_duplicacoes = num_linhas - 1
    
    # Duplicacao da lista_pivot para facilitar os calculos
    matriz_pivot = [lista_pivot[:] for _ in range(numero_de_duplicacoes)]

    # print("Matriz Pivot",matriz_pivot)
    # print("Lista Pivot",lista_pivot)

    for linha in range(len(matriz_pivot)):
        for coluna in range(len(matriz_pivot[0])):
            matriz_pivot[linha][coluna] *= fatores[linha]
            matriz_das_restricoes[linha][coluna] += matriz_pivot[linha][coluna]

    # print("Matriz Pivot", matriz_pivot)
    # print("Matriz Nao Pivot", matriz_das_restricoes)
    # print("Lista Pivot", lista_pivot)

    matriz_das_restricoes.insert(indice_linha_pivot, lista_pivot)
    
    matriz_resultante = [row[:] for row in matriz_das_restricoes]
    
    linha_cjzj = calculaLinhaCjZj(valores_vars_basica, variaveis_basicas, indice_linha_pivot, indice_coluna_pivot, teste, matriz_das_restricoes)
    
    matriz_resultante.append(linha_cjzj)
    
    # print("Matriz Resultante", matriz_resultante)
    
    iteracao += 1
    
    return matriz_resultante, linha_cjzj, variaveis_basicas

def imprimeMatriz(matriz):
    print("\n")
    print("Matriz")
    for linha in matriz:
        print(linha)
    print("\n")
    
def main():
    
    matriz1 = [[2, 3, 1, 0, 100],
            [4, 2, 0, 1, 120],
            [60, 40, 0, 0, 0]]

    matriz2 = [[2, 1, 1, 0, 0, 16],
            [1, 2, 0, 1, 0, 11],
            [1, 3, 0, 0, 1, 15],
            [30, 50, 0, 0, 0, 0]]

    matriz4 = [ [2.0, 1.0, 1, 0, 0, 100.0],
                [1.0, 1.0, 0, 1, 0, 80.0],
                [1.0, 0.0, 0, 0, 1, 40.0],
                [3.0, 2.0, 0, 0, 0, 0] ]
    
    matriz8 = [ [0.7, 1.0, 1, 0, 0, 630.0],
                [0.5, 0.84, 0, 1, 0, 600.0],
                [1.0, 0.67, 0, 0, 1, 700.0],
                [10.0, 9.0, 0, 0, 0, 0] ]



    matriz = matriz1

    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    
    var_basica = [0] * (num_colunas-1)

    variaveis_basicas = []
    tamanho_variaveis_basicas = len(variaveis_basicas)
    while tamanho_variaveis_basicas < num_colunas-1:
        variaveis_basicas.append("x" + str(tamanho_variaveis_basicas+1))
        tamanho_variaveis_basicas += 1
    print("VB",variaveis_basicas)

    iteracao = 1
    linha_fObj_primeira_iteracao = separaPrimeiraIteracao(matriz)
    matriz, linhacjzj = eliminacao_gaussiana(matriz, variaveis_basicas, var_basica, linha_fObj_primeira_iteracao)

    print(f"Iteracao {iteracao}", imprimeMatriz(matriz))
    while iteracao <= 2:
        if all(x <= 0 for x in linhacjzj[:-1]):
            break
        else:
            matriz, linhacjzj = eliminacao_gaussiana(matriz, variaveis_basicas, var_basica, linha_fObj_primeira_iteracao)
            iteracao += 1
            print(f"Iteracao {iteracao}", imprimeMatriz(matriz))

    imprimeMatriz(matriz)
 

if __name__ == "__main__":
    main()
