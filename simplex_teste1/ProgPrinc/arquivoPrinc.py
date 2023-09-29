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

def main():
    listaFuncObj, restr, cond_n_neg = leArquivo_criaLista()
    listaFuncObj = encontraCoef_listaFuncObj(listaFuncObj)
    listaRestr = encontraCoef_listaRest(restr)


    
    
main()
    