'''
matriz_base2 = [ ['1','2','3'],
                ['4','5','6'],
                ['7','8','9'],
                ['10','20'] ]

matriz_base3 = [ ['0.7','1','630'],
                ['0.5','0.84','600'],
                ['1','0.67','700'],
                ['10','9'] ]

matriz_base = [ ['2','1','100'],
                ['1','1','80'],
                ['1','0','40'],
                ['3','2'] ]

matriz_inteiros = [[float(element) for element in row] for row in matriz_base]

# Agora, matriz_inteiros contém os valores como inteiros
for linha in matriz_inteiros:
    print(linha)
    
linha_funcObj = matriz_inteiros.pop(-1)
print("Linha Func Obj:", linha_funcObj)

print("Matriz Inteiros Mod", matriz_inteiros)

primeiros_elementos = []  # Lista para armazenar os primeiros n-1 elementos
ultimos_valores = []      # Lista para armazenar os últimos valores

for linha in matriz_inteiros:
    primeiros_elementos.append(linha[:-1])  # Adiciona todos os elementos, exceto o último
    ultimos_valores.append(linha[-1]) 
    
print("Primeiros Elementos", primeiros_elementos)
print("Ultimos Valores", ultimos_valores)

# Obtenha o número de linhas (neste caso, o tamanho da matriz identidade)
num_linhas = len(matriz_inteiros)

# Crie a matriz identidade
matriz_identidade = [[1 if i == j else 0 for j in range(num_linhas)] for i in range(num_linhas)]

# Combine a matriz original com a matriz identidade
matriz_resultado = [linha + identidade for linha, identidade in zip(primeiros_elementos, matriz_identidade)]

print("Matriz Resultado", matriz_resultado)

# Adicione os últimos valores ao final de cada lista na matriz
matriz_resultado2 = [linha + [valor] for linha, valor in zip(matriz_resultado, ultimos_valores)]
        
print("Matriz Resultado 2", matriz_resultado2)

tamanho_matriz2 = len(matriz_resultado2[0])
print(tamanho_matriz2)

while len(linha_funcObj) < tamanho_matriz2:
    linha_funcObj.append(0)

print("Linha Func Obj", linha_funcObj)

matriz_resultado2.append(linha_funcObj)

print("\n")
print("Matriz Resultante")
for linha in matriz_resultado2:
    print(linha)

matriz = [ [2.0, 1.0, 1, 0, 0, 100.0],
           [1.0, 1.0, 0, 1, 0, 80.0],
           [1.0, 0.0, 0, 0, 1, 40.0],
           [3.0, 2.0, 0, 0, 0, 0] ]



# Obtenha o número de colunas na matriz
num_colunas = len(matriz[0])

# Crie legendas
legendas = [f'x{i}' for i in range(1, num_colunas)] + ['b']

# Imprima as legendas
for legenda in legendas:
    print(legenda, end="\t")
print()

# Imprima os valores da matriz
for linha in matriz:
    for valor in linha:
        print(valor, end="\t")
    print()
print(legendas)

indice = 1

# 3 restricoes 
# tam = len(matriz[0])
# tam_rest = len(matriz_das_restricoes)



# resut = tam - tam_rest = 3

# while tam(var_basica) < tam
    # x{result}
    # result 

# 2 restricoes = [x3, x4]

var_basica = ['x3','x4','x5']

var_basica.pop(indice)
var_basica.insert(indice, legendas[indice])

print(var_basica)

'''

# Pega o tamanho da matriz total (elementos_coluna)
# Pega o tamanho da matriz de restricoes (quant_linhas)

# matriz_total = 5
# matriz_restricoes = 2
# quantidade x = (matriz_total - matriz_restricoes)

# preencher ate o tamanho de matriz_restricoes (quant_linhas)
#(x3, x4)


matriz_total = [[1,2,1,0,3],
                [4,5,0,1,6]]

matriz_restricoes = [[1, 2, 3],
                     [4, 5, 6]]

var_basica = [10, 20]

tamanho_matriz_total = len(matriz_total[0])
tamanho_matriz_restricoes = len(matriz_restricoes)

tamanho_var = tamanho_matriz_total - tamanho_matriz_restricoes

print("Tamanho Matriz Total",tamanho_matriz_total)
print("Tamanho Matriz Restricoes",tamanho_matriz_restricoes)
print("Tamanho Var",tamanho_var)

var_fdf = []

while tamanho_var < tamanho_matriz_total:
    var_fdf.append("x" + str(tamanho_var))
    tamanho_var += 1
    
print(var_fdf)