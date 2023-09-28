import re

valores = ['a', '+', '2b', '-', '3c', '<=', '10']

primeira_lista = []
segunda_lista = []

coeficiente_atual = 0

padrao = r'(-?\d*)([a-zA-Z])'

for valor in valores:
    match = re.match(padrao, valor)
    if match:
        coeficiente = match.group(1)
        variavel = match.group(2)
        if coeficiente:
            coeficiente_atual += int(coeficiente)
        else:
            coeficiente_atual += 1
    else:
        if coeficiente_atual != 0:
            primeira_lista.append(coeficiente_atual)
            coeficiente_atual = 0
        segunda_lista.append(valor)

if coeficiente_atual != 0:
    primeira_lista.append(coeficiente_atual)

print("PrimeiraLista ->", primeira_lista)
print("SegundaLista ->", segunda_lista)
