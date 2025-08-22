
M = 1
N = 1
soma = 0
cont = 0
numeros = []
while M != 0 and N != 0:
    M = int(input())
    if M != 0:
        numeros.append(M)
    else:
        break
    N = int(input())
    if N != 0:
        numeros.append(N)
    else:
        break
menor = min(numeros)
maior = max(numeros)

while True:
    if cont <= len(numeros) - 1:
        if numeros[cont] == 0 or numeros[cont + 1] == 0:
            break
        elif numeros[cont] > numeros[cont + 1]:
            maior = numeros[cont]
            menor = numeros[cont + 1]
        else:
            maior = numeros[cont + 1]
            menor = numeros[cont]
        for i in range (menor, maior + 1):
            print(i, end=" ")
            soma+=i
        print(f'Sum={soma}')
        soma = 0
        cont+=2
    else:
        break
"""
for i in range (menor, maior):
    print(menor + i, end=" ")
    soma+=i
print("Sum=".format(soma))
"""

