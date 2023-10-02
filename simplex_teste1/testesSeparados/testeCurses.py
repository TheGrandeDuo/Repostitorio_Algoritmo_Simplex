import curses

# Função para criar a tabela
def create_table(stdscr, rows, columns, data):
    # Calcula o tamanho da janela
    max_y, max_x = stdscr.getmaxyx()

    # Calcula o tamanho da célula
    cell_height = max_y // (rows + 2)  # +2 para deixar espaço para o cabeçalho e a borda inferior
    cell_width = max_x // (columns + 1)  # +1 para a última coluna

    # Imprime o cabeçalho
    for i, header in enumerate(data[0]):
        stdscr.addstr(0, i * cell_width, header.center(cell_width))

    # Desenha a linha horizontal que separa o cabeçalho do corpo da tabela
    stdscr.hline(1, 0, curses.ACS_HLINE, max_x)

    # Imprime os dados
    for i, row in enumerate(data[1:], start=1):
        for j, value in enumerate(row):
            stdscr.addstr(i, j * cell_width, str(value).ljust(cell_width))

    # Atualiza a tela
    stdscr.refresh()

def main(stdscr):
    # Define os dados da tabela (substitua esses dados pelos seus próprios)
    table_data = [
        ["Nome", "Idade", "Cidade"],
        ["Alice", 25, "Nova York"],
        ["Bob", 30, "Los Angeles"],
        ["Charlie", 22, "Chicago"],
        ["David", 35, "Houston"],
    ]

    rows = len(table_data)
    columns = len(table_data[0])

    # Inicia o modo curses
    curses.curs_set(0)  # Oculta o cursor
    curses.noecho()  # Não mostra a entrada do teclado
    stdscr.clear()  # Limpa a tela

    # Cria a tabela
    create_table(stdscr, rows, columns, table_data)

    # Aguarda uma tecla antes de sair
    stdscr.getch()

# Inicia o aplicativo curses
if __name__ == "__main__":
    curses.wrapper(main)
