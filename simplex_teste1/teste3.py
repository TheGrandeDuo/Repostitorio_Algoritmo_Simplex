import re

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

def separaElementos():
    for item in range(len(listaFuncObj)):
        item = listaFuncObj[0].split("Maximizar")
        func_obj = item[-1]
        
    for elemento in func_obj:
        if(elemento.startswith("Z")):
            z = elemento
        #elif(elemento.find("=")):
            #print(elemento)


    

   
   
   
        


def main():
    leArquivo()
    separaElementos()
    # String que contém a equação
    equacao = "Z = 4x1 + 3x2 + 8x3"

    # Use expressões regulares para encontrar os coeficientes e variáveis
    padrao = r'([+-]?\d*)?([a-zA-Z]\w*)'

    matches = re.findall(padrao, equacao)

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
    
    chaves = []
    for i in coeficientes:    
        chaves.append(i)
    print(chaves)
    
    
main()