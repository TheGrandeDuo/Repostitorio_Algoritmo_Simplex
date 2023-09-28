import re

expressoes = ['1a + 1b <= 5', '2a + 6b - 3c <= 10']
coeficientes = []

for expressao in expressoes:
    
    print(expressao)
    expressao.strip()
    expressao.split(" ")
    coefRest = re.findall(r"-?\d+", expressao)
    print(coefRest)
    coeficientes.append(coefRest)

#print(coefRest)
print(coeficientes)