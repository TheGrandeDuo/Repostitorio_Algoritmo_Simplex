import copy
import tkinter as tk
from tkinter import ttk
import math

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
        print("Problema Sem Fronteira\n")
        exit()  # Encerra o programa

def encontraProblemaDegenerado(resultados_divisao):
    if resultados_divisao.count(min(resultados_divisao)) >= 2:
        print("Sistema Degenerado\n")

def transformaPrimalDual(matriz_primal, minimizacao):
    if minimizacao == 1:
        # Encontrando o número máximo de colunas na matriz original
        num_colunas = max(len(linha) for linha in matriz_primal)

        # Preenchendo as linhas mais curtas com valores vazios
        for linha in matriz_primal:
            while len(linha) < num_colunas:
                linha.append('')

        # Inicialize uma matriz vazia para as colunas
        matriz_dual = []

        # Iterar pelas colunas
        for coluna in range(num_colunas):
            nova_coluna = [linha[coluna] for linha in matriz_primal]
            matriz_dual.append(nova_coluna)

        matriz_dual[-1].pop()

        #print("MC",matriz_dual)
        return matriz_dual
    else:
        return matriz_primal
        
def encontrar_linhaPivot(rest_semValores, rest_valores, indice_coluna_pivot):
      
    resultados_divisao = [1000000 if linha[indice_coluna_pivot] == 0 else rest_valores[i] / linha[indice_coluna_pivot] for i, linha in enumerate(rest_semValores)]

    encontraProblemaSemFronteira(resultados_divisao)
    encontraProblemaDegenerado(resultados_divisao)
    
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
        resultado[i] = float(resultado[i])
        print(f"| {variaveis_basicas[i]} = {round(resultado[i],3)}                          |")

    Z = float(-1 * resultado[-1])
    print(f"| Z = {round(Z,3)}                         |")
    print("+=================================+")

class JanelaEntradaDados:
    def __init__(self, root):
        self.root = root
        self.root.title("Método Simplex")

        self.label_variaveis = tk.Label(root, text="Número de Variáveis:")
        self.label_variaveis.grid(row=0, column=0, padx=10, pady=10)
        
        self.entrada_variaveis = tk.Entry(root)
        self.entrada_variaveis.grid(row=0, column=1, padx=10, pady=10)

        self.label_restricoes = tk.Label(root, text="Número de Restrições:")
        self.label_restricoes.grid(row=1, column=0, padx=10, pady=10)
        
        self.entrada_restricoes = tk.Entry(root)
        self.entrada_restricoes.grid(row=1, column=1, padx=10, pady=10)

        self.botao_obter_valores = tk.Button(root, text="Confirmar", command=self.obter_valores)
        self.botao_obter_valores.grid(row=2, columnspan=4, padx=10, pady=10)
        # Adicione um Combobox à direita
        self.label_selecao = tk.Label(root, text="Selecionar opção:")
        self.label_selecao.grid(row=0, column=2, padx=10, pady=10)

        opcoes_combobox = ["Maximização", "Minimização"]
        self.combobox = ttk.Combobox(root, values=opcoes_combobox, state="readonly")
        self.combobox.set("Maximização")
        self.combobox.grid(row=0, column=3, padx=10, pady=10)

    def obter_valores(self):
        numero_de_variaveis = int(self.entrada_variaveis.get())
        numero_de_restricoes = int(self.entrada_restricoes.get())
        tipo_simplex = self.combobox.get()  # Obtém o valor selecionado no Combobox

        # Fecha a primeira janela
        self.root.destroy()

        # Cria a segunda janela
        self.janela_matriz = JanelaMatrizValores(numero_de_variaveis, numero_de_restricoes, tipo_simplex)

class JanelaMatrizValores:
    def __init__(self, numero_de_variaveis, numero_de_restricoes, tipo_simplex):
        self.tipo_simplex = tipo_simplex
        self.segunda_janela = tk.Tk()
        self.segunda_janela.title("Método Simplex")
        self.segunda_janela.geometry("500x300")  # Defina o tamanho da segunda janela
        self.matriz_de_inputs = []

        # Adicione as linhas para as restrições
        for i in range(numero_de_restricoes):
            linha = []
            for j in range(numero_de_variaveis + 2):  # Adiciona 2 colunas extras (uma com "<=" e outra com entrada)
                if j < numero_de_variaveis:
                    if (j != 0):
                        label_variavel = tk.Label(self.segunda_janela, text=f"+  x{j + 1}")
                        label_variavel.grid(row=i, column=j * 2, padx=5, pady=5, sticky='e')
                    else:
                        label_variavel = tk.Label(self.segunda_janela, text=f"x{j + 1}")
                        label_variavel.grid(row=i, column=j * 2, padx=5, pady=5, sticky='e')
                    entrada = tk.Entry(self.segunda_janela, width=5)
                    entrada.grid(row=i, column=j * 2 + 1, padx=5, pady=5)
                    linha.append(entrada)
                elif j == numero_de_variaveis:
                    if(tipo_simplex == "Maximização"):
                        label_sinal = tk.Label(self.segunda_janela, text="<=")
                    else:
                        label_sinal = tk.Label(self.segunda_janela, text=">=")
                    label_sinal.grid(row=i, column=j * 2, padx=5, pady=5)
                else:  # Última coluna para entrada
                    entrada = tk.Entry(self.segunda_janela, width=5)
                    entrada.grid(row=i, column=j * 2 + 1, padx=5, pady=5)
                    linha.append(entrada)
            self.matriz_de_inputs.append(linha)

        # Adicione a linha Z (coeficientes objetivos)
        linha_z = []

        # Adicione "Z:" como o primeiro elemento
        if(tipo_simplex == "Maximização"):
            label_variavel_z = tk.Label(self.segunda_janela, text="Z:")
        else:
            label_variavel_z = tk.Label(self.segunda_janela, text="C:")
        label_variavel_z.grid(row=numero_de_restricoes, column=0, padx=5, pady=5, sticky='e')

        for j in range(numero_de_variaveis):
            if (j != 0):
                label_variavel = tk.Label(self.segunda_janela, text=f"+  x{j + 1}")
            else:
                label_variavel = tk.Label(self.segunda_janela, text=f"x{j + 1}")
            label_variavel.grid(row=numero_de_restricoes, column=(j * 2) + 1, padx=5, pady=5, sticky='e')

            entrada = tk.Entry(self.segunda_janela, width=5)
            entrada.grid(row=numero_de_restricoes, column=(j * 2) + 2, padx=5, pady=5)
            linha_z.append(entrada)
        self.matriz_de_inputs.append(linha_z)

        botao_imprimir = tk.Button(self.segunda_janela, text="Imprimir Valores", command=self.pega_valores_tipo)
        botao_imprimir.grid(row=numero_de_restricoes + 1, columnspan=(numero_de_variaveis + 2) * 2, padx=10, pady=10)

        self.segunda_janela.mainloop()


    def pega_valores_tipo(self):
        listaIn = []
        for i in range(len(self.matriz_de_inputs)):
            linha = []
            for j in range(len(self.matriz_de_inputs[i])):
                valor = self.matriz_de_inputs[i][j].get()
                linha.append(valor)
            listaIn.append(linha)
        linhas_mais_z = []
        for linha in listaIn:
            linhas_mais_z.append(linha)

        #print( "matriz",linhas_mais_z)
        #print("tipo", self.tipo_simplex)
        
        if (self.tipo_simplex == "Maximização"):
            #print("max")
            minimizacao = 0
        else:
            #print("min")
            minimizacao = 1

        matriz_string = linhas_mais_z

        matriz_primal_dual = transformaPrimalDual(matriz_string, minimizacao)
        
        matriz_selecionada = matriz_primal_dual

        # matriz_dual = transformaPrimalDual(matriz_string_input, minimizacao)
        # print(matriz_dual)
        #matriz_string = matriz_dual
        
        matriz_transformada = transformaStringInt(matriz_selecionada)
        matriz_resultante = adicionaMatrizIdentidade(matriz_transformada)
        
        # print("Matriz_Transformada:", matriz_transformada)
        # print("Matriz_Resultante", matriz_resultante)
        
        matriz = matriz_resultante

        iteracao = 1
        
        valores_variaveis_basicas = encontraValoresVariaveisBasicas(matriz)
        variaveis_basicas = encontraVariaveisBasicas(matriz)
        
        linha_fObj_primeira_iteracao = separaPrimeiraIteracao(matriz)
        linha_variaveis_totais_primeira_iteracao = separaVariaveisPrimeiraIteracao(matriz)
        
        print("Iteracao: ",iteracao-1)
        imprimeMatriz(matriz)
        print("\n")
        
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
        # return linhas_mais_z, tipo_simplex
def main():
    root = tk.Tk()
    root.geometry("700x300")  # Defina o tamanho da janela principal
    app = JanelaEntradaDados(root)
    root.mainloop()
    

if __name__ == "__main__":    
    main()
