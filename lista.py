numeros = []
soma = cont = 0
while True:
    M = int(input())
    numeros.append(M)
    N = int(input())
    if N == 0 or M == 0:
        break
    numeros.append(N)
while cont + 1 < len(numeros):
    if numeros[cont] > numeros [cont + 1]:
        maior = numeros[cont]
        menor = numeros[cont + 1]
    for i in range (menor, maior + 1):
        print(i, end=" ")
        soma+=i
    print(f'Sum={soma}')
    soma = 0
    cont+=2
