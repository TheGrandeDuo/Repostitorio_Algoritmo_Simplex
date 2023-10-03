import curses

def create_window(stdscr, num_elements):
    height, width = stdscr.getmaxyx()

    # Define a janela onde os elementos serão exibidos
    window = curses.newwin(3, width, 0, 0)

    # Define a posição inicial para a entrada do usuário
    user_input_x = 4  # Começando após "Z:"

    # Adiciona os elementos estáticos à janela
    window.addstr(1, 0, "Z:")
    for i in range(1, num_elements + 1):
        window.addstr(1, user_input_x, f"x{i}:")
        user_input_x += 4  # Incrementa o espaço para a próxima entrada

    # Atualiza a janela
    window.refresh()

    # Captura a entrada do usuário para os valores x
    user_values = []
    for i in range(num_elements):
        user_input = window.getstr(1, user_input_x).decode('utf-8')
        user_values.append(user_input.strip())
        user_input_x += 4  # Move a posição de entrada para a próxima

    return user_values

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    # Defina o número de elementos estáticos
    num_elements = 3  # Substitua pelo valor desejado

    user_values = create_window(stdscr, num_elements)
    
    # Você pode acessar os valores digitados pelo usuário em user_values
    stdscr.addstr(5, 0, "Valores inseridos:")
    for i, value in enumerate(user_values, 1):
        stdscr.addstr(6 + i, 0, f"x{i}: {value}")

    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
