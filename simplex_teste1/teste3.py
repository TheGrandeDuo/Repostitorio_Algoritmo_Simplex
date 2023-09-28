import re
import numpy as np

# Inicialize as listas
listaFuncObj = []
listaRest = []
listaCondNaoNeg = []

def leArquivo():

    # Abra o arquivo e leia as linhas
    with open('teste.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    # Itere pelas linhas e separe-as nas listas apropriadas
    for linha in linhas:
        linha = linha.strip()  # Remova espaços em branco no início e no fim da linha
        if linha.startswith("Maximizar") or linha.startswith("Minimizar"):
            listaFuncObj.append(linha)
        elif linha.find(("+") or ("-") or ("/") or ("*")) != -1:
            listaRest.append(linha)
        elif linha.find(","): 
            listaCondNaoNeg.append(linha)

    # Imprima as listas resultantes
    # print("listaFuncObj:")
    # for item in listaFuncObj:
    #     print(item)

    # print("\nlistaRest:")
    # for item in listaRest:
    #     print(item)

    # print("\nlistaCondNaoNeg:")
    # for item in listaCondNaoNeg:
    #     print(item)

def separaFuncObj():
    for item in range(len(listaFuncObj)):
        item = listaFuncObj[0].split("Maximizar")
        func_obj = item[-1]
        
    padrao = r'([+-]?\d*)?([a-zA-Z]\w*)'

    matches = re.findall(padrao, func_obj)

    coeficientes = {}  # Dicionário para armazenar os coeficientes

    for coeficiente, variavel in matches:
        coeficiente = coeficiente.strip()
        variavel = variavel.strip()
        
        if coeficiente:
            coeficiente = int(coeficiente)
        else:
            coeficiente = 1  # Se nenhum coeficiente é especificado, assume 1
        
        coeficientes[variavel] = coeficiente

    # Imprima o dicionário resultante
    print(coeficientes)
    
    coeficientes_funcObj = []
    for i in coeficientes.values():    
        coeficientes_funcObj.append(i)
        funcObj_coef = np.array(coeficientes_funcObj, dtype=int)
    #print(funcObj_coef)
    
    matriz = []    
    matriz.append(funcObj_coef)

    # for elemento in func_obj:
    #     if(elemento.startswith("Z")):
    #         z = elemento

    #for valor in func_obj[1]:
    #   print(valor)

def separaRest():
    coeficiente2 = {}
    
    for linha in range(len(listaRest)):
        coeficiente2 = listaRest[linha]
        
        #variavel = variavel.strip()


    print(coeficiente2)

    

   
   
   
        


def main():
    leArquivo()
    separaFuncObj()
    separaRest()
    
main()