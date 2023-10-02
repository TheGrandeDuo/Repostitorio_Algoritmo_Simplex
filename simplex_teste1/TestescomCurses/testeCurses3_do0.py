import curses

def main(stdscr):
    curses.curs_set(1)  # Exibe o cursor
    stdscr.clear()
    stdscr.refresh()

    # Inicializa a matriz de valores
    num_restricoesI = 2  # Número de restrições (R1 e R2 no exemplo)
    num_variaveisI = 2  # Número de variáveis (x1 e x2 no exemplo)
    
    # num_restricoesI = num_restricoes + 1
    # num_variaveisI = num_variaveis + 1
    valores = [['' for _ in range(num_variaveisI)] for _ in range(num_restricoesI)]

    # Exibe os títulos iniciais
    janela_inicial = curses.newwin(3,20)
    janela_inicial.addstr(0, 0, "Digite o valor das variaveis: ")
    
    lista_valores = []
    
    while True:
        c = stdscr.getkey()
        if c == ord('q'):  # Tecla 'q' para sair
            break
        elif c == 10:  # Tecla Enter para avançar para a próxima variável ou restrição
            break
        else: 
            lista_valores.append(int(c))
        stdscr.refresh()
        
    print(lista_valores)
    
    # stdscr.addstr(0, 0, "Digite os valores para as variáveis nas restrições (pressione Enter para avançar, 'q' para sair):")
    # stdscr.addstr(2, 0, "Z")
    # stdscr.addstr(3, 0, "R1")
    # stdscr.addstr(4, 0, "R2")
    # stdscr.refresh()
    # stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
