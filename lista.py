M = 1
N = 1
soma = 0
while M != 0 and N != 0:
    M = int(input())
    if M == 0:
        break
    N = int(input())
    if N == 0:
        break
    if M > N:
        maior = M
        menor = N
    else:
        maior = N
        menor = M
    for i in range (menor, maior + 1):
        print(i, end=" ")
        soma+=i
    print(f'Sum={soma}')
    soma = 0
