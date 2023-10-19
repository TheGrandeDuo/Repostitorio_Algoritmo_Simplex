import copy

def transformaStringInt(matriz_string):
    
    matriz_int = []

    for linha in matriz_string:
        linha_numeros = []
        for elemento in linha:
            if '.' in elemento:
                try:
                    numero = float(elemento)
                except ValueError:
                    numero = elemento
            else:
                try:
                    numero = int(elemento)
                except ValueError:
                    numero = elemento
            linha_numeros.append(numero)
        matriz_int.append(linha_numeros)

    # print("Matriz Int:",matriz_int)
    return matriz_int
        
def adicionaMatrizIdentidade(matriz_int):

    # Procedimento Padrao
    # 1) separar ultima linha -> linha objetivo
    # 2) separar ultimos valores, ficando somente com os coeficientes das restricoes
    # 3) Adicionar matriz_identidade do tamanho da matriz_das_restricoes nas listas
    # 4) Adicionar ultimos valores novamente no final de cada lista
    # 5) Adicionar quantidade de 0 certas na funcao objetivo
    # 6) Adicionar ultima linha (linha_objetivo) novamente na matriz_separada_mod
    # 7) Retorna matriz_separada_mod para utilizar em calculos

    # -----------------------------------------------------------------------------------------#
    
    # 1) Divide em matriz_das_restricoes e ultima_linha
    
    matriz_das_restricoes, ultima_linha = separar_ultima_linha(matriz_int)

    # Armazena os resultados das restricoes em lista_ultimos_valores
    lista_ultimos_valores = [row.pop() for row in matriz_das_restricoes]

    # print("Lista Ultimos Valores:", lista_ultimos_valores)
    # print("Matriz das Restricoes:", matriz_das_restricoes)
    
    # -----------------------------------------------------------------------------------------#
    
    # 2) Adicionar matriz_identidade do tamanho da matriz_das_restricoes nas listas
    
    #matriz_separada = [[1, 2], [4, 5], [7, 8]]
    tamanho_matriz = len(matriz_das_restricoes)

    # Adicionar a matriz identidade a cada lista em matriz_separada
    matriz_separada_mod = [row + [1 if i == j else 0 for i in range(tamanho_matriz)] for j, row in enumerate(matriz_das_restricoes)]
    
    # print("Matriz Separada Mod:", matriz_separada_mod)
    
    # -----------------------------------------------------------------------------------------#
    
    # 3) Adicionar ultimos valores novamente no final de cada lista
    
    if len(matriz_separada_mod) == len(lista_ultimos_valores):
        for i in range(len(matriz_separada_mod)):
            matriz_separada_mod[i].append(lista_ultimos_valores[i])
    
    # print("Matriz Separada Mod:", matriz_separada_mod)
    
    # -----------------------------------------------------------------------------------------#
    
    # 4) Adicionar quantidade de 0 certas na funcao objetivo
    
    tamanho_matriz_separada = len(matriz_separada_mod[0])
    tamanho_ultima_linha = len(ultima_linha)
    
    # print("Tamanho Matriz Separada", tamanho_matriz_separada)
    # print("Tamanho Ultima Linha", tamanho_ultima_linha)

    while tamanho_ultima_linha < tamanho_matriz_separada:
        ultima_linha.append(0)
        tamanho_ultima_linha += 1

    # -----------------------------------------------------------------------------------------#

    # 5) Adicionar ultima linha (linha_objetivo) novamente na matriz_separada_mod
    
    matriz_separada_mod.append(ultima_linha)

    # -----------------------------------------------------------------------------------------#

    # 7) Retorna matriz_separada_mod para utilizar em calculos

    return matriz_separada_mod

# Agora, matriz_separada_mod conterá as listas originais com a matriz identidade adicionada ao final de cada uma


def separaPrimeiraIteracao(matriz):
    
    matriz_copia = copy.deepcopy(matriz)
    
    linha_fObj_primeira_iteracao = matriz_copia.pop()
    
    # print("Matriz Copia:", matriz_copia)
    # print("Linha Primeira Iteracao:", linha_fObj_primeira_iteracao)
    
    return linha_fObj_primeira_iteracao

def separaVariaveisPrimeiraIteracao(matriz):
    
    linha_variaveis_totais_primeira_iteracao = []
    tamanho_colunas_matriz_total = len(matriz[0])
    tamanho_linha_variaveis_totais_primeira_iteracao = len(linha_variaveis_totais_primeira_iteracao)
    
    while tamanho_linha_variaveis_totais_primeira_iteracao < tamanho_colunas_matriz_total-1:
        linha_variaveis_totais_primeira_iteracao.append("x" + str(tamanho_linha_variaveis_totais_primeira_iteracao+1))
        tamanho_linha_variaveis_totais_primeira_iteracao += 1
    
    
    
    return linha_variaveis_totais_primeira_iteracao

def encontraValoresVariaveisBasicas(matriz):
    num_linhas = len(matriz)
    valores_variaveis_basicas = [0] * (num_linhas-1)
    
    return valores_variaveis_basicas

def encontraVariaveisBasicas(matriz):
    
    variaveis_basicas = []
    
    matriz_copia, ult = separaMatriz(matriz)
    
    num_colunas = len(matriz[0])
    num_linhas_matriz_copia = len(matriz_copia)

    num_variaveis_basicas = num_colunas - num_linhas_matriz_copia
    
    while num_variaveis_basicas < num_colunas:
        variaveis_basicas.append("x" + str(num_variaveis_basicas))
        num_variaveis_basicas += 1
        
    # print("Variaveis Basicas", variaveis_basicas)
    
    return variaveis_basicas

def encontrar_colunaPivot(matriz):
    ultima_linha = matriz[-1]
    coluna_pivot = ultima_linha[0]
    indice_coluna_pivot = 0
        
    for i, numero in enumerate(ultima_linha):
        if (numero > coluna_pivot):
            coluna_pivot = numero
            indice_coluna_pivot = i
    
    # print("Coluna Pivot:", coluna_pivot)
    # print("Índice Coluna Pivot:", indice_coluna_pivot)
        
    return indice_coluna_pivot

def encontraProblemaSemFronteira(resultados_divisao):
    
    # Trocar valor de 10000 por alguma constante sla, para nao ter problema
    if all(resultado == 1000000 or resultado < 0 for resultado in resultados_divisao):
        print("Encontrei um problema sem fronteira")
        exit()  # Encerra o programa

        
def encontrar_linhaPivot(rest_semValores, rest_valores, indice_coluna_pivot):
    
    resultados_divisao = [1000000 if linha[indice_coluna_pivot] == 0 else rest_valores[i] / linha[indice_coluna_pivot] for i, linha in enumerate(rest_semValores)]

    encontraProblemaSemFronteira(resultados_divisao)

    if not resultados_divisao:
        return None, None  # Trata a lista vazia

    menor_valor = 1000000
    indice_linha_pivot = 0
    
    for i, valor in enumerate(resultados_divisao):
        if valor >= 0:                  # Validacao para que nao pegue numeros negativos
            if valor < menor_valor:
                menor_valor = valor
                indice_linha_pivot = i
            
    # print("Index Linha Pivot:", indice_linha_pivot)
    # print("Resultados da Divisão:", resultados_divisao)
    # print("Menor Valor",menor_valor)

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
    resultados = [] # Lista para armazenar os últimos valores

    for linha in matriz_das_restricoes:
        variaveis.append(linha[:-1])  # Adiciona todos os elementos, exceto o último
        resultados.append(linha[-1])  # Adiciona o último elemento

    # print("Variaveis:", variaveis)
    # print("Resultados:", resultados)
    
    return variaveis, resultados

def elementoPivot(matriz, indice_linha_pivot, indice_coluna_pivot):
    elemento_pivot = matriz[indice_linha_pivot][indice_coluna_pivot]
    
    # print("Elemento Pivot:", elemento_pivot)
    
    return elemento_pivot

def calculaListaFatores(matriz, indice_linha_pivot, indice_coluna_pivot):
    fatores = []
    matriz2, ultimaLinha = separar_ultima_linha(matriz)
    for i in range(len(matriz2)):
        if i != indice_linha_pivot:
            fator = matriz[i][indice_coluna_pivot]
            fatores.append(-1*fator)
                
    # print("Lista Fatores:", fatores)
    
    return fatores

def calculaLinhaCjZj(variaveis_basicas, valores_vars_basica, indice_linha_pivot, indice_coluna_pivot, teste, teste2,  matriz_das_restricoes):
    
    # print("Variaveis do padrao (nao modificadas)")
    # print("Variaveis Basicas:", valores_vars_basica)
    # print("Indice Linha:", indice_linha_pivot)
    # print("Indice Coluna:", indice_coluna_pivot)
    # print("Teste:", teste)
    # print("Matriz Restricoes", matriz_das_restricoes)
    
    variaveis_basicas.pop(indice_linha_pivot)
    variaveis_basicas.insert(indice_linha_pivot, teste2[indice_coluna_pivot])
    
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

def eliminacao_gaussiana(matriz, variaveis_basicas, valores_var_basica, linha_fObj_primeira_iteracao, linha_variaveis_totais_primeira_iteracao):
    iteracao = 0
    valores_vars_basica = valores_var_basica
    variaveis_basicas = variaveis_basicas
        
    indice_coluna_pivot = encontrar_colunaPivot(matriz)
    rest_semValores, rest_valores = separaMatriz(matriz)
    indice_linha_pivot = encontrar_linhaPivot(rest_semValores, rest_valores, indice_coluna_pivot)
    elemento_pivot = elementoPivot(matriz, indice_linha_pivot, indice_coluna_pivot)
    fatores = calculaListaFatores(matriz, indice_linha_pivot, indice_coluna_pivot)

    matriz_das_restricoes, linha_aux = separar_ultima_linha(matriz)

    teste = linha_fObj_primeira_iteracao
    teste2 = linha_variaveis_totais_primeira_iteracao
    
    lista_pivot = matriz_das_restricoes.pop(indice_linha_pivot)

    for valor in range(len(lista_pivot)):
        lista_pivot[valor] /= elemento_pivot
    
    num_linhas = len(matriz)-1
    numero_de_duplicacoes = num_linhas - 1
    
    # Duplicacao da lista_pivot para facilitar os calculos
    matriz_pivot = [lista_pivot[:] for _ in range(numero_de_duplicacoes)]

    # print("Matriz Pivot",matriz_pivot)
    # print("Lista Pivot",lista_pivot)

    # print("Fatores:", fatores)

    for linha in range(len(matriz_pivot)):
        for coluna in range(len(matriz_pivot[0])):
            if matriz_pivot[linha][coluna] != 0:
                matriz_pivot[linha][coluna] *= fatores[linha]
                matriz_das_restricoes[linha][coluna] += matriz_pivot[linha][coluna]

    # print("Matriz Pivot", matriz_pivot)
    # print("Matriz Nao Pivot", matriz_das_restricoes)
    # print("Lista Pivot", lista_pivot)

    matriz_das_restricoes.insert(indice_linha_pivot, lista_pivot)
    
    matriz_resultante = [row[:] for row in matriz_das_restricoes]
    
    linha_cjzj = calculaLinhaCjZj(variaveis_basicas, valores_vars_basica, indice_linha_pivot, indice_coluna_pivot, teste, teste2, matriz_das_restricoes)
    
    matriz_resultante.append(linha_cjzj)
    
    # print("Matriz Resultante", matriz_resultante)
    
    iteracao += 1
    
    return matriz_resultante, linha_cjzj

def imprimeMatriz(matriz):
    print("Matriz")
    for linha in matriz:
        print(linha)

def imprimeResultado(matriz, iteracao, variaveis_basicas):
    print("\n")
    print("+=================================+")
    print("| Resultado Final                 |")
    print("| Numero de Iteracoes Totais: ",iteracao," |")
    # print("Variaveis Basicas Finais: ",variaveis_basicas)
    print("| Solucao Otima                   |") 
    
    resultado = [linha[-1] for linha in matriz]
    # print("Resultado:",resultado)
    
    for i in range(len(variaveis_basicas)):
        resultado[i] = int(resultado[i])
        print(f"| {variaveis_basicas[i]} = {resultado[i]}                          |")

    Z = int(-1 * resultado[-1])
    print(f"| Z = {Z}                         |")
    print("+=================================+")

def main():

    # Exercicio 1    
    matriz_string1 = [['1','1','450'],
                     ['2','1','600'],
                     ['3','4']]

    # Exercicio 2
    matriz_string2 = [['2','3','100'],
                     ['4','2','120'],
                     ['60','40']]

    # Exercicio 3 - Transformada para modo canonico
    matriz_string3 = [['5','4','200'],
                     ['3','5','150'],
                     ['-5','-4','-100'],
                     ['-8','-4','-80'],
                     ['300000','400000']]

    # Exercicio 4
    matriz_string4 = [['2','1','100'],
                        ['1','1','80'],
                        ['1','0','40'],
                        ['3','2']]

    # Exercicio 5
    matriz_string5 = [['2','1','16'],
                     ['1','2','11'],
                     ['1','3','15'],
                     ['30','50']]

    # Exercicio 6 - Minimizacao (encontrar o dual, da matriz primal de minimizacao)
    matriz_string6 = [['-2','-4','0.3'],
                     ['-3','-3','0.4'],
                     ['-90','-120']]
    
    # Exercicio 7 - Nao esta em forma canonica, mesmo problema do 3
    matriz_string7 = [['-1','-1','-20'],
                     ['2','3','180'],
                     ['1','0','60'],
                     ['-1','0','-10'],
                     ['0','1','40'],
                     ['3','1']]
    
    # Exercicio 8
    matriz_string8 = [['0.7','1','630'],
                      ['0.5','0.8333','600'],
                      ['1','0.6666','700'],
                      ['0.1','0.25','135'],
                      ['10','9']]
    
    # Exercicio 9
    matriz_string9 = [['0.5','0.3333','130'],
                    ['0.5','0.6666','170'],
                    ['20','12.5']]

    # Exercicio 10
    matriz_string10 = [['1','1','10000'],
                    ['1','0','6000'],
                    ['-0','-1','-2000'],
                    ['0.1','0.07']]
    
    # Matriz simulando um problema sem fronteira
    matriz_problema_sem_fronteira = [['1','-6','5'],
                                     ['3','0','11'],
                                     ['4','3']]

    matriz_string = matriz_problema_sem_fronteira
    
    matriz_transformada = transformaStringInt(matriz_string)
    matriz_resultante = adicionaMatrizIdentidade(matriz_transformada)
    
    # print("Matriz_Transformada:", matriz_transformada)
    # print("Matriz_Resultante", matriz_resultante)
    
    matriz = matriz_resultante

    iteracao = 1
    
    valores_variaveis_basicas = encontraValoresVariaveisBasicas(matriz)
    variaveis_basicas = encontraVariaveisBasicas(matriz)
    
    linha_fObj_primeira_iteracao = separaPrimeiraIteracao(matriz)
    linha_variaveis_totais_primeira_iteracao = separaVariaveisPrimeiraIteracao(matriz)
    
    matriz, linhacjzj = eliminacao_gaussiana(matriz, variaveis_basicas, valores_variaveis_basicas, linha_fObj_primeira_iteracao, linha_variaveis_totais_primeira_iteracao)

    print("Iteracao: ",iteracao)
    imprimeMatriz(matriz)
    print("Variaveis Basicas: ",variaveis_basicas)
    print("\n")
    while True:
        if all(x <= 0 for x in linhacjzj[:-1]):
            break
        else:
            matriz, linhacjzj = eliminacao_gaussiana(matriz, variaveis_basicas, valores_variaveis_basicas, linha_fObj_primeira_iteracao, linha_variaveis_totais_primeira_iteracao)
            iteracao += 1
            print("Iteracao: ",iteracao)
            imprimeMatriz(matriz)
            print("Variaveis Basicas: ",variaveis_basicas)
            print("\n")

    imprimeResultado(matriz, iteracao, variaveis_basicas)

if __name__ == "__main__":
    main()
