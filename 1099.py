n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    maior = max(a, b)
    menor = min(a, b)
    if menor % 2 == 0:
        menor = menor +1
    else:
        menor = menor + 2
    soma = 0
    for c in range(menor, maior, 2):
        soma += c
    print(soma)
        