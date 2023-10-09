matriz = [[1, 2, 3],
          [4, 5, 6]]

lista_restante = [7,8,9]

fatores = [-2,-3]

matriz_copia = [[1, 2, 3],
                [4, 5, 6]]

matriz_copia[0][0] *= fatores[0]
matriz_copia[0][1] *= fatores[0]
matriz_copia[0][2] *= fatores[0]

matriz_copia[1][0] *= fatores[1]
matriz_copia[1][1] *= fatores[1]
matriz_copia[1][2] *= fatores[1]

print("Matriz Copia:", matriz_copia)

# Funciona mas tem que revisar, esta estatico
quantidade = 1
multiplicado = False
for fator in range(len(fatores)):
    for linha in range(len(matriz)):
        for valor in range(len(matriz[linha])):
            print(f"Matriz[{fator}][{valor}]", matriz[fator][valor], "Quantidade: ",quantidade)
            quantidade += 1
            if ((quantidade >= 1) and (quantidade <= 3)):
                matriz[fator][valor] *= fatores[fator]
            if ((quantidade >= 7) and (quantidade <= 10)):
                matriz[fator][valor] *= fatores[fator]
            else:
                matriz[fator][valor] = matriz[fator][valor]
            
            # if (quantidade >= 3) and (quantidade <= 5):
            #     matriz[fator][valor] *= fatores[fator]
            #     print(f"Matriz[{fator}][{valor}]: ",matriz[fator][valor])
            #     quantidade += 1
            #     print(quantidade)
            # if (quantidade >= 6) and (quantidade <= 8):
            #     matriz[fator][valor] *= fatores[fator]
            #     print(f"Matriz[{fator}][{valor}]: ",matriz[fator][valor])
            #     quantidade += 1
            #     print(quantidade)
            # else:
            #     quantidade += 1
                
print(matriz)