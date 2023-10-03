import numpy as np
import re

def leArquivo_criaLista():

    ''' +=========================================================+'''
    ''' + LE ARQUIVO E SEPARA CADA LINHA EM SUA RESPECTIVA LISTA  +'''
    ''' +=========================================================+'''

    # Leitura do arquivo
    with open('teste.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    # Separação das linhas em listas
    #listaFuncObj = [linhas[0].strip()]  # Primeira linha na listaFuncObj
    
    listaFuncObj = [linhas[0].strip()]
    listaRestr = [linha.strip() for linha in linhas[1:-1]]  # Linhas do meio em listRestr
    listaCondNaoNeg = [linhas[-1].strip()]  # Última linha em listaCondNaoNeg

    # Imprima as listas resultantes
    print("Lista de Função Objetivo:")
    print(listaFuncObj)

    print("Lista de Restrições:")
    print(listaRestr)

    print("Lista de Condições Não Negativas:")
    print(listaCondNaoNeg)
    
    return listaFuncObj, listaRestr, listaCondNaoNeg

def encontraCoef_listaFuncObj(listaFuncObj):

    ''' +=========================================================+'''
    ''' + ENCONTRA OS COEFICIENTES DA FUNCAO listaFuncObj         +'''
    ''' +=========================================================+'''

    resultado = []

    for expressao in listaFuncObj:
        partes = []
        parte_atual = ''
        proximo_sinal = ''

        for caractere in expressao:
            if caractere in ('-'):
                if parte_atual:
                    partes.append(parte_atual)
                parte_atual = ''
                proximo_sinal = caractere
            elif caractere.isdigit():
                parte_atual += caractere
            elif parte_atual and caractere.isalpha():
                partes.append(proximo_sinal + parte_atual)
                parte_atual = ''
                proximo_sinal = ''

        if parte_atual:
            partes.append(proximo_sinal + parte_atual)

        # Transformando a lista em Inteiro
        partes.append(partes.pop(0))
        resultado.append(partes)
        STRCoefFuncObj = resultado[0]
        
        CoefFuncObj = [int(valor) for valor in STRCoefFuncObj]
        
    print("Coeficientes da Funcao Objetivos",CoefFuncObj)
    return CoefFuncObj

def encontraCoef_listaRest(listaRest):
    
    resultado = []
    print("listaRest",listaRest)
    #expressoes = ['1a + 1b <= 5', '2a + 6b <= 10']
    
    for expressao in listaRest:
        partes = []
        parte_atual = ''
        proximo_sinal = ''

        for caractere in expressao:
            if caractere in ('-'):
                if parte_atual:
                    partes.append(parte_atual)
                parte_atual = ''
                proximo_sinal = caractere
            elif caractere.isdigit():
                parte_atual += caractere
            elif parte_atual and caractere.isalpha():
                partes.append(proximo_sinal + parte_atual)
                parte_atual = ''
                proximo_sinal = ''

        if parte_atual:
            partes.append(proximo_sinal + parte_atual)

        resultado.append(partes)
        
        coefRest = [[int(valor) for valor in sublist] for sublist in resultado]
        
    print("CoefRest",coefRest)
    return coefRest

def organizaMatriz_coefRest(CoefRest):
 
    # Inicialize as listas vazias
    lista_1 = []
    lista_2 = []

    # Percorra cada sublista em CoefRest
    for sublista in CoefRest:
        # Adicione as duas primeiras colunas em lista_1
        lista_1.append(sublista[:2])
        # Adicione a terceira coluna em lista_2
        lista_2.append([sublista[2]])

    # Imprima as listas resultantes
    print("lista_1:", lista_1)
    print("lista_2:", lista_2)

    # Número de itens em uma sublista
    #print("CoefRest",len(CoefRest))
    num_itens = len(CoefRest)  # Substitua pelo valor desejado

    # Criar a matriz identidade
    matriz_identidade = [[1 if i == j else 0 for j in range(num_itens)] for i in range(num_itens)]

    # Imprimir a matriz identidade
    for linha in matriz_identidade:
        print(linha)

    #matriz_identidade = [[1, 0], [0, 1]]
    #lista_1 = [[1, 1], [2, 7]]S

    # Verificar as dimensões das matrizes
    num_linhas_ident, num_colunas_ident = len(matriz_identidade), len(matriz_identidade[0])
    num_linhas_1, num_colunas_1 = len(lista_1), len(lista_1[0])

    # Verificar se as dimensões da matriz identidade correspondem às da matriz 1
    if num_colunas_ident == num_linhas_1:
        # Criar uma matriz resultante
        matriz_resultante = []

        # Preencher a matriz resultante com as linhas de lista_1 seguidas pelas linhas de matriz_identidade
        for i in range(num_linhas_1):
            linha_resultante = lista_1[i] + matriz_identidade[i]
            matriz_resultante.append(linha_resultante)

        # Imprimir a matriz resultante
        for linha in matriz_resultante:
            print(linha)
    else:
        print("As dimensões da matriz identidade não correspondem às da matriz 1.")

    #matriz_identidade = [[1, 0], [0, 1]]
    #lista_1 = [[1, 1], [2, 7]]
    #lista_2 = [[5], [10]]

    # Verificar as dimensões das matrizes
    num_linhas_ident, num_colunas_ident = len(matriz_identidade), len(matriz_identidade[0])
    num_linhas_1, num_colunas_1 = len(lista_1), len(lista_1[0])
    num_linhas_outra, num_colunas_outra = len(lista_2), len(lista_2[0])

    # Verificar se as dimensões da matriz identidade e da outra matriz correspondem às da matriz 1
    if num_colunas_ident == num_linhas_1 and num_linhas_1 == num_linhas_outra:
        # Adicionar a outra matriz à matriz resultante
        for i in range(num_linhas_1):
            matriz_resultante[i].extend(lista_2[i])

        # Imprimir a matriz resultante atualizada
        for linha in matriz_resultante:
            print(linha)
    else:
        print("As dimensões da matriz identidade ou da outra matriz não correspondem às da matriz 1.")
    return matriz_resultante, CoefRest

def organizaMatriz_coefFuncObj(coefFuncObj, coefRest):
    
    for coef in coefFuncObj:
        if(coef == 1):
            coefFuncObj[-1] = 0
        else:
            coef = coef
    print("Coef func obj",coefFuncObj)
    
    num_itens = len(coefRest)
    
    matriz_identidade = [[1 if i == j else 0 for j in range(num_itens)] for i in range(num_itens)]
    
    matriz_res = []
    
    # for coef2 in coefRest:
    #     for item in matriz_identidade:
    #         matriz_res.append(coef2)
    #         matriz_res.append(item)
    # print(matriz_res)
    
    
            
    return 0    

def main():
    listaFuncObj, restr, cond_n_neg = leArquivo_criaLista()
    CoefFuncObj = encontraCoef_listaFuncObj(listaFuncObj)
    CoefRest = encontraCoef_listaRest(restr)
    matriz_resultante_coefRest = organizaMatriz_coefRest(CoefRest)
    matriz_resultante_coefFuncObj = organizaMatriz_coefFuncObj(CoefFuncObj, CoefRest)
    print(matriz_resultante_coefRest)


        
    
main()
    