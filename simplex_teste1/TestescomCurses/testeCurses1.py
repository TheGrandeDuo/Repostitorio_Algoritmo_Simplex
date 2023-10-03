# import curses
# from curses import wrapper
# from curses.textpad import Textbox, rectangle

# def main(janela_perguntas):
    
#     # Como modificar cores, no caso criar dupla de cores
#     curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
#     BLUE_AND_YELLOW = curses.color_pair(1)
    
#     janela_perguntas.clear()
    
#     # tela_tabelas = curses.newwin(200, 400, 10, 10)

#     janela_perguntas.addstr(2, 10, "METODO SIMPLEX")
#     janela_perguntas.addstr(5, 10, "Quantas variaveis tem o problema: ")
#     janela_perguntas.addstr(8, 10, "Quantas restricoes tem o problema: ")
 
#     # win = curses.newwin(nlines, ncols, uly, ulx)
#     #rectangle(janela_perguntas, 5, 5, 15, 80)
    
#     #rectangle(janela_perguntas, 5, 5, 30, 50)
    

#     # valor = 5
#     # a = valor
#     # b = valor
#     # c = (b * 3)
#     # d = c - (a + b)
        
#     janela_perguntas.refresh()
    
#     while True:
#         key = janela_perguntas.getch()
#         if key == ord('q'):  # Se a tecla 'q' for pressionada, saia do loop
#             break
#     #janela_perguntas.getch()
    
# wrapper(main)

import curses
from curses import wrapper

def main(janela_perguntas):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    BLUE_AND_YELLOW = curses.color_pair(1)

    janela_perguntas = curses.newwin(10, 80, 5, 5)
    janela_obj = curses.newwin(20,100,0,0)

    janela_perguntas.clear()
    curses.echo()

    coefPerg = []

    janela_perguntas.addstr(2, 10, "METODO SIMPLEX")
    janela_perguntas.addstr(5, 10, "Quantas variaveis tem o problema: ")
    janela_perguntas.addstr(8, 10, "Quantas restricoes tem o problema: ")

    num_variaveis = ""
    num_restricoes = ""
    pergunta_atual = 1

    # Melhorias
    # Backspace nao funciona
    
    while True:
        janela_perguntas.refresh()

        key = janela_perguntas.getch()

        if key == ord('q'):
            break
        elif key == curses.KEY_ENTER or key == 10:
            if pergunta_atual == 1:
                pergunta_atual = 2
                janela_perguntas.addstr(5, 10, "Quantas variaveis tem o problema: " + num_variaveis)
                janela_perguntas.addstr(8, 10, "Quantas restricoes tem o problema: ")
                #num_variaveis = ""
            elif pergunta_atual == 2:
                pergunta_atual = 3
                janela_perguntas.addstr(8, 10, "Quantas restricoes tem o problema: " + num_restricoes)
                janela_perguntas.refresh()
                # num_restricoes = ""
                break
        else:
            if pergunta_atual == 1:
                if key in range(48, 58):
                    num_variaveis += chr(key)
                    janela_perguntas.addstr(5, 10, "Quantas variaveis tem o problema: " + num_variaveis)
                elif key == curses.KEY_BACKSPACE or key == 127:  # Adicione isso para permitir o uso de Backspace
                    num_variaveis = num_variaveis[:-1]
                    janela_perguntas.addstr(5, 10, "Quantas variaveis tem o problema: " + num_variaveis)
            elif pergunta_atual == 2:
                if key in range(48, 58):
                    num_restricoes += chr(key)
                    janela_perguntas.addstr(8, 10, "Quantas restricoes tem o problema: " + num_restricoes)
                elif key == curses.KEY_BACKSPACE or key == 127:
                    num_restricoes = num_restricoes[:-1]
                    janela_perguntas.addstr(8, 10, "Quantas restricoes tem o problema: " + num_restricoes)
    coefPerg.append(num_variaveis)
    coefPerg.append(num_restricoes)
    
    for valor in range(2):
        print("Valores: ", valor)
    
    while True:
        janela_perguntas.clear()
        janela_obj.clear()
        janela_obj.addstr(5,2,"Z: ")
        
        print(coefPerg[0])
        print(int(coefPerg[0]))
        for var in range(int(coefPerg[0])):
            print(var)
            janela_obj.addstr(5, 2 + (var * 2), f"x{var}: ")
            janela_obj.refresh()
        key2 = janela_obj.getch()
        if key2 == ord('q'): 
            break
    
    print("Variaveis:",coefPerg[0], " Restricoes:",coefPerg[1])
    
wrapper(main)
