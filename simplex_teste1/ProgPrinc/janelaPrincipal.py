import tkinter as tk
from tkinter import ttk

class JanelaEntradaDados:
    def __init__(self, root):
        self.root = root
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
        self.botao_obter_valores.grid(row=2, columnspan=4, padx=10, pady=10)
        # Adicione um Combobox à direita
        self.label_selecao = tk.Label(root, text="Selecionar opção:")
        self.label_selecao.grid(row=0, column=2, padx=10, pady=10)

        opcoes_combobox = ["Maximização", "Minimização"]
        self.combobox = ttk.Combobox(root, values=opcoes_combobox, state="readonly")
        self.combobox.set("Maximização")
        self.combobox.grid(row=0, column=3, padx=10, pady=10)

    def obter_valores(self):
        numero_de_variaveis = int(self.entrada_variaveis.get())
        numero_de_restricoes = int(self.entrada_restricoes.get())
        tipo_simplex = self.combobox.get()  # Obtém o valor selecionado no Combobox

        # Fecha a primeira janela
        self.root.destroy()

        # Cria a segunda janela
        self.janela_matriz = JanelaMatrizValores(numero_de_variaveis, numero_de_restricoes, tipo_simplex)

class JanelaMatrizValores:
    def __init__(self, numero_de_variaveis, numero_de_restricoes, tipo_simplex):
        self.tipo_simplex = tipo_simplex
        self.segunda_janela = tk.Tk()
        self.segunda_janela.title("Método Simplex")
        self.segunda_janela.geometry("500x300")  # Defina o tamanho da segunda janela
        self.matriz_de_inputs = []

        # Adicione as linhas para as restrições
        for i in range(numero_de_restricoes):
            linha = []
            for j in range(numero_de_variaveis + 2):  # Adiciona 2 colunas extras (uma com "<=" e outra com entrada)
                if j < numero_de_variaveis:
                    if (j != 0):
                        label_variavel = tk.Label(self.segunda_janela, text=f"+  x{j + 1}")
                        label_variavel.grid(row=i, column=j * 2, padx=5, pady=5, sticky='e')
                    else:
                        label_variavel = tk.Label(self.segunda_janela, text=f"x{j + 1}")
                        label_variavel.grid(row=i, column=j * 2, padx=5, pady=5, sticky='e')
                    entrada = tk.Entry(self.segunda_janela, width=5)
                    entrada.grid(row=i, column=j * 2 + 1, padx=5, pady=5)
                    linha.append(entrada)
                elif j == numero_de_variaveis:
                    if(tipo_simplex == "Maximização"):
                        label_sinal = tk.Label(self.segunda_janela, text="<=")
                    else:
                        label_sinal = tk.Label(self.segunda_janela, text=">=")
                    label_sinal.grid(row=i, column=j * 2, padx=5, pady=5)
                else:  # Última coluna para entrada
                    entrada = tk.Entry(self.segunda_janela, width=5)
                    entrada.grid(row=i, column=j * 2 + 1, padx=5, pady=5)
                    linha.append(entrada)
            self.matriz_de_inputs.append(linha)

        # Adicione a linha Z (coeficientes objetivos)
        linha_z = []

        # Adicione "Z:" como o primeiro elemento
        if(tipo_simplex == "Maximização"):
            label_variavel_z = tk.Label(self.segunda_janela, text="Z:")
        else:
            label_variavel_z = tk.Label(self.segunda_janela, text="C:")
        label_variavel_z.grid(row=numero_de_restricoes, column=0, padx=5, pady=5, sticky='e')

        for j in range(numero_de_variaveis):
            if (j != 0):
                label_variavel = tk.Label(self.segunda_janela, text=f"+  x{j + 1}")
            else:
                label_variavel = tk.Label(self.segunda_janela, text=f"x{j + 1}")
            label_variavel.grid(row=numero_de_restricoes, column=(j * 2) + 1, padx=5, pady=5, sticky='e')

            entrada = tk.Entry(self.segunda_janela, width=5)
            entrada.grid(row=numero_de_restricoes, column=(j * 2) + 2, padx=5, pady=5)
            linha_z.append(entrada)
        self.matriz_de_inputs.append(linha_z)

        botao_imprimir = tk.Button(self.segunda_janela, text="Imprimir Valores", command=self.pega_valores_tipo)
        botao_imprimir.grid(row=numero_de_restricoes + 1, columnspan=(numero_de_variaveis + 2) * 2, padx=10, pady=10)

        self.segunda_janela.mainloop()


    def pega_valores_tipo(self):
        listaIn = []
        for i in range(len(self.matriz_de_inputs)):
            linha = []
            for j in range(len(self.matriz_de_inputs[i])):
                valor = self.matriz_de_inputs[i][j].get()
                linha.append(valor)
            listaIn.append(linha)
        linhas_mais_z = []
        for linha in listaIn:
            linhas_mais_z.append(linha)
        # self.segunda_janela.destroy()  # Fecha a segunda janela
        print(linhas_mais_z, self.tipo_simplex)
        return linhas_mais_z, self.tipo_simplex
        # return linhas_mais_z, tipo_simplex
def main():
    root = tk.Tk()
    root.geometry("700x300")  # Defina o tamanho da janela principal
    app = JanelaEntradaDados(root)
    root.mainloop()

if __name__ == "__main__":
    main()
