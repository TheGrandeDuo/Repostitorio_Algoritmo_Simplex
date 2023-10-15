import tkinter as tk

class JanelaEntradaDados:
    def __init__(self, root):
        self.root = root
        self.root.configure(background='#1e3743')
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
        self.botao_obter_valores.grid(row=2, columnspan=2, padx=10, pady=10)

    def obter_valores(self):
        numero_de_variaveis = int(self.entrada_variaveis.get())
        numero_de_restricoes = int(self.entrada_restricoes.get())

        # Fecha a primeira janela
        self.root.destroy()

        # Cria a segunda janela
        self.janela_matriz = JanelaMatrizValores(numero_de_variaveis, numero_de_restricoes)

class JanelaMatrizValores:
    def __init__(self, numero_de_variaveis, numero_de_restricoes):
        self.segunda_janela = tk.Tk()
        self.segunda_janela.title("Método Simplex")
        self.segunda_janela.configure(background='#1e3743')
        self.segunda_janela.geometry("700x400")  # Defina o tamanho da segunda janela

        self.matriz_de_inputs = []
        for i in range(numero_de_restricoes):
            linha = []
            for j in range(numero_de_variaveis + 2):  # Adiciona 2 colunas extras (uma com "<=" e outra com entrada)
                if j < numero_de_variaveis:
                    label_variavel = tk.Label(self.segunda_janela, text=f"x{j+1}")
                    label_variavel.grid(row=i, column=j*2, padx=5, pady=5, sticky='e')

                    entrada = tk.Entry(self.segunda_janela, width=5)
                    entrada.grid(row=i, column=j*2+1, padx=5, pady=5)
                    linha.append(entrada)
                elif j == numero_de_variaveis:
                    label_sinal = tk.Label(self.segunda_janela, text="<=")
                    label_sinal.grid(row=i, column=j*2, padx=5, pady=5)
                else:  # Última coluna para entrada
                    entrada = tk.Entry(self.segunda_janela, width=5)
                    entrada.grid(row=i, column=j*2+1, padx=5, pady=5)
                    linha.append(entrada)
            self.matriz_de_inputs.append(linha)

        botao_imprimir = tk.Button(self.segunda_janela, text="Imprimir Valores", command=self.montar_lista)
        botao_imprimir.grid(row=numero_de_restricoes, columnspan=(numero_de_variaveis + 2) * 2, padx=10, pady=10)

        self.segunda_janela.mainloop()

    def montar_lista(self):
        listaIn = []
        for i in range(len(self.matriz_de_inputs)):
            for j in range(len(self.matriz_de_inputs[0])):
                valor = self.matriz_de_inputs[i][j].get()
                print(f"Valor x{j+1}[{i}]: {valor}")
                listaIn.append(valor)
        tamanho_pedaço = i+1

        pedaços = [listaIn[i:i + tamanho_pedaço] for i in range(0, len(listaIn), tamanho_pedaço)]

        for pedaço in pedaços:
            print(pedaço)
        print(pedaços)

# def transformaStringInt():
#     listaInt = []
    
#     for num in li
    
#     return listaInt
    

def main():
    root = tk.Tk()
    root.geometry("700x400")  # Defina o tamanho da janela principal
    app = JanelaEntradaDados(root)
    root.mainloop()

if __name__ == "__main__":
    main()
