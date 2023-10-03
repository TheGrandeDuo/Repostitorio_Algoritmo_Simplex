def funcRestricoes(linha):
    listaRestricoes = []
    listaRestricoes.append(linha)
    return True

# Nome do arquivo de texto que você deseja ler
nome_arquivo = 'teste.txt'

# Inicializa uma matriz vazia para armazenar as linhas do arquivo
matriz = []

# Abre o arquivo para leitura
with open(nome_arquivo, 'r') as arquivo:
    # Itera através das linhas do arquivo
    for linha in arquivo:
        # Remove espaços em branco e caracteres de nova linha (se necessário)
        linha = linha.strip()
        
        # Adiciona a linha à matriz
        matriz.append(linha)

# Agora, 'matriz' contém todas as linhas do arquivo como elementos individuais
# Você pode acessar e manipular a matriz como desejar



for linha in matriz:
    if ("<=" or ">=") in linha:
        funcRestricoes(linha)
        print("Encontrei uma linha de restricoes")
    
    print(linha)
    

