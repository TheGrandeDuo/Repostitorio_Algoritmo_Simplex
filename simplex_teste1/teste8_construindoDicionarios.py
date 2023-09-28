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
    listaFuncObj = [linhas[0].strip()]  # Primeira linha na listaFuncObj
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

def encontraCoef_listaFuncObj(funcObj):
    
    ''' +=========================================================+'''
    ''' + ENCONTRA OS COEFICIENTES DA FUNCAO listaFuncObj         +'''
    ''' +=========================================================+'''

    # Use uma expressão regular para encontrar os coeficientes das variáveis
    coeficientes_variaveis = re.findall(r'(-?\s?\d+)x\d+', funcObj[0])

    # Encontre o coeficiente constante (Z)
    coeficiente_constante = 1

    # Crie a lista de coeficientes na ordem desejada
    listaCoefFuncObj = [int(coef.replace(" ", "")) for coef in coeficientes_variaveis] + [int(coeficiente_constante)]

    # Imprima a lista resultante
    print("Lista de Coeficientes da Função Objetivo:")
    print(listaCoefFuncObj)

    return listaCoefFuncObj

def encontraCoef_listaRest(restr):

    ''' +=========================================================+'''
    ''' + ENCONTRA OS COEFICIENTES DA FUNCAO listaRest            +'''
    ''' +=========================================================+'''  
    print("restr",restr)
    
    # for pos in restr:
    #     for pos2 in pos:
    #         print("pos2",pos2)
    #     print("pos",pos)
    
    coefRes = []
    varRes = []
    for pos in range(len(restr)):    
        #pos.strip()
        print("pos",pos)
        pos2 = restr[pos].split(" ")
    
        print("posss222",pos2)
        if "<=":
            coefRes.append(pos2[-1])
            print("coefRes" ,coefRes)
        if "+":
            pos3 = pos2.index("x1")
            if pos3:
                print(pos3)
            else:
                print("e o bichgo")
                
                #print(pos2.index("x1"))
            print("valores",pos2)

    
    # Inicialize uma lista vazia para armazenar as listas de coeficientes
    listasCoefRestricoes = []

    # Itere sobre as restrições
    for restricao in restr:
        # Use uma expressão regular para encontrar os coeficientes
        coeficientes = [int(coef) if coef.isdigit() or (coef[0] == '-' and coef[1:].isdigit()) else 1 for coef in re.findall(r'-?\d+', restricao)]
        listasCoefRestricoes.append(coeficientes)

    # Imprima as listas de coeficientes resultantes
    print("Listas de Coeficientes das Restriçõessaasasas:")
    print(listasCoefRestricoes)
    print("Listas de Coeficientes das Restrições:")
    print(listasCoefRestricoes)
    
    return listasCoefRestricoes

    




def main():
    funcObj, restr, cond_n_neg = leArquivo_criaLista()
    listaFuncObj = encontraCoef_listaFuncObj(funcObj)
    listaRestr = encontraCoef_listaRest(restr)
    print("listaRest",listaRestr)
    #print(listaRestr)
    matriz = []
    matriz.append(listaFuncObj)
    #print(matriz)
    
    # Lista de Restrições
    listaRestricoes = ['x1 + x2 <= 5', '2x1 + 5x2 <= 10']



    
    
main()
    