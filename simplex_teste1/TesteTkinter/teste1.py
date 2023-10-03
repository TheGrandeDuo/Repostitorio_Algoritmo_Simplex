# main
# Perg_VarRest
# CriaMatrizVarRest
# CalculaSimplex
# 

from tkinter import *

janela = Tk()


class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.criandoBotoes()
        janela.mainloop()
    def tela(self):
        self.janela.title("Metodo Simplex")
        self.janela.configure(background='#1e3743')
        #self.janela.configure(background='lightblue')
        self.janela.geometry("700x500")
        self.janela.resizable(False, False) # Responsavel pela responsividade da tela (False, False) -> Nao e responsiva na (Horiz, Vertic)
        self.janela.maxsize(width=900, height=700) 
        self.janela.minsize(width=400, height=300)
    def criandoBotoes(self):
    
        ### Exemplo para Testes
        # Criacao do botao Limpar
        # self.bt_limpar = Button(self.janela, text="Limpar")
        # self.bt_limpar.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
        
        # Criacao do botao Confirmar
        self.bt_confirmar = Button(self.janela, text="Confirmar")
        self.bt_confirmar.place(relx=0.1, rely=0.8, relwidth=0.15, relheight=0.075)
        
        
    
if __name__ == "__main__":
    Application()
    
    