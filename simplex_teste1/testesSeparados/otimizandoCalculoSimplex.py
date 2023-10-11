import copy

def encontrar_colunaPivot(matriz, iteracao):
    ultima_linha = matriz[-1]
    coluna_pivot = ultima_linha[0]
    indice_coluna_pivot = 0
    
    # print(ultima_linha)
    
    for i, numero in enumerate(ultima_linha):
        if (numero > coluna_pivot):
            # print(i,numero)
            coluna_pivot = numero
            indice_coluna_pivot = i # Adicione esta linha
    
    # print(f"Iteração {iteracao}:")
    # print("Coluna Pivot:", coluna_pivot)
    # print("Índice Coluna Pivot:", indice_coluna_pivot)  # Adicione esta linha
    
    return indice_coluna_pivot

def encontrar_linhaPivot(rest_semValores, rest_valores, indice_coluna_pivot):
    
    resultados_divisao = [rest_valores[i] / linha[indice_coluna_pivot] if linha[indice_coluna_pivot] != 0 else 10000 for i, linha in enumerate(rest_semValores)]

    if not resultados_divisao:
        return None, None  # Trata a lista vazia

    menor_valor = resultados_divisao[0]
    indice_linha_pivot = 0

    for i, valor in enumerate(resultados_divisao):
        if valor < menor_valor:
            menor_valor = valor
            indice_linha_pivot = i
            
    # print("Index Linha Pivot",indice_linha_pivot)
    # print("Resultados da Divisão:", resultados_divisao)

    return indice_linha_pivot
    
def separar_ultima_linha(matriz):
    matriz_copia = [linha[:] for linha in matriz]  # Cria uma cópia da matriz original
    ultima_linha = matriz_copia.pop()  # Remove e retorna a última linha da cópia
    return matriz_copia, ultima_linha

def verificaColunaZ(matriz):
    coluna_z = []

    coluna_z.append(separar_ultima_linha(matriz))
    # print("Coluna Z",coluna_z)
    
    for linha_z in coluna_z:
        for valor_z in linha_z:
            if (valor_z > 0):
                # print("Encerramos")
                return 0
    return 1

def separaMatriz(matriz):
    matriz_copia, ultima_linha = separar_ultima_linha(matriz)
    
    primeiros_elementos = []  # Lista para armazenar os primeiros n-1 elementos
    ultimos_valores = []      # Lista para armazenar os últimos valores

    for linha in matriz_copia:
        primeiros_elementos.append(linha[:-1])  # Adiciona todos os elementos, exceto o último
        ultimos_valores.append(linha[-1])       # Adiciona o último elemento

    # print("Primeiros Elementos:", primeiros_elementos)
    # print("Ultimos Valores",ultimos_valores)
    
    return primeiros_elementos, ultimos_valores

def elementoPivot(matriz, indice_linha_pivot, indice_coluna_pivot):
    elemento_pivot = matriz[indice_linha_pivot][indice_coluna_pivot]
    ## print(elementoPivot)
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

def copia_lista(lista):
    copiaLista = lista[:]
    return copiaLista

def eliminacao_gaussiana(matriz, valores_var_basica):
    iteracao = 0
    valores_vars_basica = valores_var_basica
    
    indice_coluna_pivot = encontrar_colunaPivot(matriz, iteracao)
    rest_semValores, rest_valores = separaMatriz(matriz)
    indice_linha_pivot = encontrar_linhaPivot(rest_semValores, rest_valores, indice_coluna_pivot)
    elemento_pivot = elementoPivot(matriz, indice_linha_pivot, indice_coluna_pivot)
    fatores = calculaListaFatores(matriz, indice_linha_pivot, indice_coluna_pivot)
    ## print("Elemento Pivot",elemento_pivot)
    ## print("Fatores",fatores)

    matriz_das_restricoes, linha_aux = separar_ultima_linha(matriz)
    ## print("Matriz2",matriz2,"Ultima linha",linha_cj_zj)
    

    #teste = copy.deepcopy(linha_aux)
    #teste = copia_lista(linha_aux)
    ## print("Linha aux",linha_aux)
    
    #teste = []

    # Itere pelas linhas da matriz original e copie cada linha para a matriz de cópia
    # for linha in linha_aux:
    #     linha_copia = linha  # Crie uma cópia da linha
    #     teste.append(linha_copia)
    
    teste = [60, 40, 0, 0, 0]
    # print("Copiaaaaa",teste)
    
    lista_pivot = matriz_das_restricoes.pop(indice_linha_pivot)

    for valor in range(len(lista_pivot)):
        lista_pivot[valor] /= elemento_pivot
    
    num_linhas = 2
    numero_de_duplicacoes = num_linhas - 1
    
    # Duplicacao da lista_pivot para facilitar os calculos
    matriz_pivot = [lista_pivot[:] for _ in range(numero_de_duplicacoes)]

    # print("Iteracao 0")
    # print("Fatores",fatores)
    # print("Matriz Pivot",matriz_pivot)
    # print("Lista Pivot",lista_pivot)

    for linha in range(len(matriz_pivot)):
        for coluna in range(len(matriz_pivot[0])):
            matriz_pivot[linha][coluna] *= fatores[linha]
            ## print(f"Matriz: [{linha}][{coluna}]",matriz_pivot[linha][coluna])
            #matriz[i][j] = matriz[i][j] * fatores[i]
            matriz_das_restricoes[linha][coluna] += matriz_pivot[linha][coluna]

    # print("Iteracao 1")
    # print("Matriz Pivot",matriz_pivot)
    # print("Matriz Nao Pivot",matriz_das_restricoes)
    # print("Lista Pivot",lista_pivot)

    matriz_das_restricoes.insert(indice_linha_pivot, lista_pivot)
    # print("Matriz Resultante",matriz_das_restricoes)
    
    matriz_resultante = [row[:] for row in matriz_das_restricoes]
    # Calcular linha Zj-Cj
    
    num_colunas = len(matriz[0])

    linha_zj = [[0] * num_colunas]

    # print(linha_zj)

    
    # print("Copia Lista AUX",teste)
    
    valores_vars_basica.pop(indice_linha_pivot)
    valores_vars_basica.insert(indice_linha_pivot, teste[indice_coluna_pivot])
    
    # print("Linha Aux para calculos: ",teste)
    # print("Valores das variaveis basicas: ",valores_vars_basica)
    
    for linha in range(len(matriz_das_restricoes)):
        for coluna in range(len(matriz_das_restricoes[0])):
            matriz_das_restricoes[linha][coluna] *= valores_vars_basica[linha]
    # print("Linha Zj",linha_zj)
    # print("Matriz das restricoes",matriz_das_restricoes)
    
    soma_listas = [sum(x) for x in zip(*matriz_das_restricoes)]
    
    linha_cjzj = []
    for valor in range(len(teste)):
        linha_cjzj.append(teste[valor] - soma_listas[valor])
    
    #linha_cjzj[-1] = linha_cjzj[-1] * -1
    ## print("ESSA E AULTLAS MALINASH",linha_cjzj[-1])
        #linha_cjzj[-1].pop()
    
    matriz_resultante.append(linha_cjzj)
    
    # print("Soma_Listas",soma_listas)
    # print("Linha CjZj",linha_cjzj)
    # print("Matriz Final",matriz_resultante)
    
    # for i in range(len(matriz_resultante)):
    #     for j in range(len(matriz_resultante[0])):
    #         # print(matriz_resultante[i][-1])
        
    return matriz_resultante, valores_vars_basica, linha_cjzj
        # for coluna in range(len(matriz[indice_linha_pivot])):
        #     matriz[indice_linha_pivot][coluna] /= elemento_pivot

        # =================== FUNCIONA =========================
        # FUNCIONA, trabalhando em alguns ajustes
        # matriz2, ultimaLinha = separar_ultima_linha(matriz)
        # matriz3 = [linha[:] for linha in matriz2]
 
        # for i in range(len(matriz3)-1):
        #     for j in range(len(matriz3[i])):
        #         matriz3[indice_linha_pivot][j] *= fatores[i]
        #         if i != indice_linha_pivot:
        #             matriz3[i][j] += matriz3[i-1][j]
        #         matriz3[indice_linha_pivot][j] = matriz2[indice_linha_pivot][j]

         # =================== FUNCIONA =========================
        # Funciona porem tambem acredito que precisa de ajustes, ideia boa entretanto
        # matriz2, ultimaLinha = separar_ultima_linha(matriz)
        # matriz_nao_pivot = [linha[:] for linha in matriz2]
        # lista_pivot = matriz_nao_pivot.pop(indice_linha_pivot)

        # lista_nao_pivot = []
        # for sublist in matriz_nao_pivot:
        #     lista_nao_pivot.extend(sublist)

        # for i in range(len(lista_pivot)):
        #     for j in range(len(fatores)):
        #         # Alguma maneira de nao fazer essa gambiarra
        #         lista_pivot[i] *= fatores[j]
        #         lista_nao_pivot[i] += lista_pivot[i]
        #         lista_pivot[i] /= fatores[j]

        # matriz2, ultimaLinha = separar_ultima_linha(matriz)
        # matriz_nao_pivot = [linha[:] for linha in matriz2]
        # lista_pivot = matriz_nao_pivot.pop(indice_linha_pivot)

        # ============== NAO FUNCIONA ====================
        # for i in range(len(lista_pivot)):
        #     for j in range(len(fatores)):
        #         lista_pivot[i] *= fatores[j]

        # for i in range(len(matriz_nao_pivot)):
        #     for j in range(len(matriz_nao_pivot[i])):
        #         for k in range(len(fatores)):
        #             matriz_nao_pivot[i][j] += lista_pivot[j]
        #             #matriz_nao_pivot[i][j] /= fatores[k]
        # for i in range(len(lista_pivot)):
        #     for j in range(len(fatores)):
        #         lista_pivot[i] /= fatores[j]

        # for i in range(len(matriz2)):
        #     for j in range(len(matriz2[i])-1):
        #         if matriz2[i].index(i) != indice_linha_pivot:
        #             # print(matriz_nao_pivot[i][j])
        #             matriz2[i].append(matriz_nao_pivot[0][i])

        # for linha in matriz:
        #     for coluna in linha:
        #         matriz[indice_linha_pivot][coluna] /= elemento_pivot
        # # print(matriz)

matriz = [[2, 3, 1, 0, 100],
         [4, 2, 0, 1, 120],
         [60, 40, 0, 0, 0]]

matriz3 = [[0.0, 2.0, 1.0, -0.5, 40.0],
           [1.0, 0.5, 0.0, 0.25, 30.0], 
           [0.0, 10.0, 0.0, -15.0, 0]]

var_basica = [0, 0]

iteracao = 1
matriz, valores_var_basica, linhacjzj = eliminacao_gaussiana(matriz, var_basica)
print(f"Iteracao {iteracao}")
print(matriz)
while True:
    if all(x <= 0 for x in linhacjzj[:-1]):
        break
    else:
        matriz, valores_var_basica, linhacjzj = eliminacao_gaussiana(matriz, var_basica)
        iteracao += 1
        print(f"Iteracao {iteracao}")
        print(matriz)


# iteracao = 0
# while True:
#     matriz, valores_var_basica, linhacjzj = eliminacao_gaussiana(matriz, var_basica)
#     print(f"Iteracao {iteracao + 1}")
#     iteracao += 1
#     print(matriz)
    
#     if (linhacjzj)
    # print("Matriz tecnicamente final",matriz)
    # Verifique se todos os valores de linhacjzj, exceto o último, são menores que 0
    # todos_menores = []
    # for valor in range(len(linhacjzj[:-1])):
    #     # print(linhacjzj[valor])
    #     if linhacjzj[valor] <= 0:
    #         todos_menores.append(True)
            
    #     if todos_menores:
    #         break

#eliminacao_gaussiana(matriz)
# matriz2 = eliminacao_gaussiana(matriz)

# # print("matriz2")
# for linha in matriz2:
#     # print(linha)

## print("MATRIZ 2")
#imprimir_matriz(matriz2)

# var_basica = [0,0]
# matriz2, valores_var_basica1, linhacjzj1 = eliminacao_gaussiana(matriz, var_basica)
# matriz4, valores_var_basica, linhacjzj2 = eliminacao_gaussiana(matriz2, valores_var_basica1)

# # print(linhacjzj1)
# # print(linhacjzj2)

# for valor in linhacjzj2[:-1]:
#     # print("valor",valor)
#     if valor <= 0:
#         # print("Encerramos")
#         break

# # print("matriz4")
# for linha in matriz4:
#     # print(linha)



# Continue com o código após o loop



#eliminacao_gaussiana(matriz2)

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# pos = 0  # Posição da lista que você deseja retirar

# # Separar a lista na posição 'pos' e armazená-la em 'matriz_pivot'
# matriz_pivot = [matriz.pop(pos)]

# # 'matriz' agora contém as listas restantes
# matriz_nao_pivot = matriz

# fatores = [-2, -4]

# # Certifique-se de que 'fatores' tenha o mesmo número de elementos que 'matriz_pivot[0]'
# if len(fatores) != len(matriz_pivot[0]):
#     raise ValueError("O número de elementos em 'fatores' deve ser igual ao número de elementos em 'matriz_pivot[0]'")

# # Multiplicar os elementos de 'matriz_pivot' pelos fatores correspondentes e somar aos elementos em 'matriz_nao_pivot'
# for i in range(len(matriz_pivot[0])):
#     resultado = matriz_pivot[0][i] * fatores[i]
#     for j in range(len(matriz_nao_pivot)):
#         matriz_nao_pivot[j][i] += resultado

# # Saída
# # print("matriz_nao_pivot resultante:", matriz_nao_pivot)








# matriz = [[1, 2, 3], [4, 5, 6]]
# valores = [2, 3]

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         matriz[i][j] += valores[i]

# # print(matriz)




#         elemento_pivot = ultima_linha[indice_coluna_pivot]
        
#         if elemento_pivot == 0:
#             # print("Não foi possível encontrar um elemento pivot não zero.")
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
        
        
