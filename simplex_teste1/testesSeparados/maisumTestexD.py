import re

# expressoes = ['1a + 1b <= 5', '2a + 6b - 3c <= 10']
# coeficientes = []

# for expressao in expressoes:
    
#     print(expressao)
#     expressao.strip()
#     expressao.split(" ")
#     coefRest = re.findall(r"-?\d+", expressao)
#     print(coefRest)
#     coeficientes.append(coefRest)

# #print(coefRest)
# print(coeficientes)

import numpy as np

lista1 = [1, 2, 3, 4, 6, 7]
lista2 = [4, 5, 6, 8, 9, 0]
lista3 = [4, 5, 6, 8, 9, 0]
lista4 = [4, 5, 6, 8, 9, 0]

# Combine as duas listas em uma lista de listas
lista_combinada = [lista1, lista2, lista3, lista4]

# Converta a lista combinada em um array NumPy com dtype int
B = np.array(lista_combinada, dtype=int)

print("Tabela B Orig:",B)

expressoes = ['1a + 1b <= 5', '2a + 6b - 3c <= 10']
resultado = []
resultado2 = []

for expressao in expressoes:
    partes = []
    parte_atual = ''
    proximo_sinal = ''

    for caractere in expressao:
        if caractere in ('-'):
            if parte_atual:
                partes.append(int(parte_atual))
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
    
print(resultado)

lista_de_strings = [['1', '1', '5'], ['2', '6', '-3']]

lista_de_strings.append(['1', '2', '3'])

# Converter as strings em inteiros usando compreensão de lista
lista_de_inteiros = [[int(valor) for valor in sublist] for sublist in lista_de_strings]

print(lista_de_strings)

print(lista_de_inteiros)

C = np.array(lista_de_inteiros)

print(C)