# import curses
# from curses import wrapper
# from curses.textpad import Textbox, rectangle

# def main(stdscr):
    
#     # Como modificar cores, no caso criar dupla de cores
#     curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
#     BLUE_AND_YELLOW = curses.color_pair(1)
    
#     stdscr.clear()
    
#     # tela_tabelas = curses.newwin(200, 400, 10, 10)

#     stdscr.addstr(2, 10, "METODO SIMPLEX")
#     stdscr.addstr(5, 10, "Quantas variaveis tem o problema: ")
#     stdscr.addstr(8, 10, "Quantas restricoes tem o problema: ")
 
#     # win = curses.newwin(nlines, ncols, uly, ulx)
#     #rectangle(stdscr, 5, 5, 15, 80)
    
#     #rectangle(stdscr, 5, 5, 30, 50)
    

#     # valor = 5
#     # a = valor
#     # b = valor
#     # c = (b * 3)
#     # d = c - (a + b)
        
#     stdscr.refresh()
    
#     while True:
#         key = stdscr.getch()
#         if key == ord('q'):  # Se a tecla 'q' for pressionada, saia do loop
#             break
#     #stdscr.getch()
    
# wrapper(main)

import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    BLUE_AND_YELLOW = curses.color_pair(1)

    stdscr.clear()
    curses.echo()

    stdscr.addstr(2, 10, "METODO SIMPLEX")
    stdscr.addstr(5, 10, "Quantas variaveis tem o problema: ")
    stdscr.addstr(8, 10, "Quantas restricoes tem o problema: ")

    num_variaveis = ""
    num_restricoes = ""
    pergunta_atual = 1

    while True:
        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == curses.KEY_ENTER or key == 10:
            if pergunta_atual == 1:
                pergunta_atual = 2
                stdscr.addstr(5, 10, "Quantas variaveis tem o problema: " + num_variaveis)
                stdscr.addstr(8, 10, "Quantas restricoes tem o problema: ")
                num_variaveis = ""
            elif pergunta_atual == 2:
                pergunta_atual = 3
                stdscr.addstr(8, 10, "Quantas restricoes tem o problema: " + num_restricoes)
                stdscr.refresh()
                num_restricoes = ""
        else:
            if pergunta_atual == 1:
                if key in range(48, 58):
                    num_variaveis += chr(key)
                    stdscr.addstr(5, 10, "Quantas variaveis tem o problema: " + num_variaveis)
                elif key == curses.KEY_BACKSPACE or key == 127:  # Adicione isso para permitir o uso de Backspace
                    num_variaveis = num_variaveis[:-1]
                    stdscr.addstr(5, 10, "Quantas variaveis tem o problema: " + num_variaveis)
            elif pergunta_atual == 2:
                if key in range(48, 58):
                    num_restricoes += chr(key)
                    stdscr.addstr(8, 10, "Quantas restricoes tem o problema: " + num_restricoes)
                elif key == curses.KEY_BACKSPACE or key == 127:
                    num_restricoes = num_restricoes[:-1]
                    stdscr.addstr(8, 10, "Quantas restricoes tem o problema: " + num_restricoes)

wrapper(main)
