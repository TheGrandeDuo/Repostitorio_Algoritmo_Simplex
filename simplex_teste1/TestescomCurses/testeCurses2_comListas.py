import curses


def criar_matriz_identidade(tamanho):
    matriz_identidade = []
    for i in range(tamanho):
        linha_identidade = [0] * tamanho
        linha_identidade[i] = 1
        matriz_identidade.append(linha_identidade)
    return matriz_identidade

def main(stdscr):
    curses.curs_set(1)  # Exibe o cursor
    stdscr.clear()
    stdscr.refresh()

    # Inicializa a matriz de valores
    num_restricoesI = 3  # Número de restrições + Z (Z, R1 e R2 no exemplo)
    num_variaveisI = 3  # Número de variáveis + valor (considerando <=) (x1 e x2 e valor no exemplo)
    
    # num_restricoesI = num_restricoes + 1
    # num_variaveisI = num_variaveis + 1
    valores = [['' for _ in range(num_variaveisI)] for _ in range(num_restricoesI)]

    # Exibe os títulos iniciais
    stdscr.addstr(0, 0, "Digite os valores para as variáveis nas restrições (pressione Enter para avançar, 'q' para sair):")
    stdscr.addstr(4, 0, "R1")
    stdscr.addstr(5, 0, "R2")
    stdscr.addstr(6, 0, "Z")
    stdscr.refresh()

    # Loop para preencher os valores
    restricao_atual = 0
    variavel_atual = 0

    while True:
        c = stdscr.getch()

        if c == ord('q'):  # Tecla 'q' para sair
            break
        elif c == 10:  # Tecla Enter para avançar para a próxima variável ou restrição
            variavel_atual += 1
            if variavel_atual == num_variaveisI:
                variavel_atual = 0
                restricao_atual += 1
                if restricao_atual == num_restricoesI:
                    break
            stdscr.addstr(4 + restricao_atual, 8 + (variavel_atual * 30), f"x{variavel_atual + 1}: {valores[restricao_atual][variavel_atual]}")
        else:
            valores[restricao_atual][variavel_atual] += chr(c)
            stdscr.addstr(4 + restricao_atual, 8 + (variavel_atual * 30), f"x{variavel_atual + 1}: {valores[restricao_atual][variavel_atual]}")

        stdscr.refresh()

    # Imprime a matriz de valores
    print("Valores inseridos:")
    for i, restricao in enumerate(valores):
        print(f"R{i + 1}", end=": ")
        for valor in restricao:
            print(valor, end="  ")
        print()
    print(valores)

    # lista_valores_inteiros = []
    # for item in valores:
    #     for valor in item:
    #         lista_valores_inteiros.append(int(valor))
    
    
    # print(lista_valores_inteiros)

    # valores = [['1', '2', '3'], ['4', '5', '6'], ['8', '9', '2']]

    # # Usar uma list comprehension para converter os valores em inteiros
    lista_de_inteiros = [[int(valor) for valor in sublista] for sublista in valores]

    # Imprimir o resultado
    print(lista_de_inteiros)
    
    a = len(lista_de_inteiros) - 1

    # Exemplo: criar uma matriz identidade 3x3
    tamanho = a
    matriz_identidade = criar_matriz_identidade(tamanho)

    # Imprimir a matriz identidade
    for linha in matriz_identidade:
        print(linha)
    print("MatrizIdenti",matriz_identidade)


    # lista_de_inteiros = [[1, 2, 3], [4, 5, 6], [8, 9, 2]]

    # lista_de_inteiros = [[1, 2, 3], [4, 5, 6], [8, 9, 2]]

    # # Determine o número de colunas na matriz identidade
    # num_colunas = len(lista_de_inteiros[0]) - 1

    # # Inicialize a matriz identidade como uma lista vazia
    # matriz_identidade = []

    # # Crie a matriz identidade
    # for lista in lista_de_inteiros:
    #     linha_identidade = [0] * num_colunas
    #     for i in range(len(lista) - 1):
    #         linha_identidade[i] = lista[i]
    #     matriz_identidade.append(linha_identidade)

    # # Imprima a matriz identidade
    # for linha in matriz_identidade:
    #     print(linha)

    # print("Matriz Ide",matriz_identidade)


    stdscr.getch()  # Aguarda uma tecla antes de sair

if __name__ == "__main__":
    curses.wrapper(main)
