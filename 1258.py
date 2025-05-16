def tamanho(t):
    if t == "G":
        return 3
    elif t == "M":
        return 2
    else:
        return 1

cont = 0
while True:
    camisas = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        nome = input()
        cor, tam = map(str, input().split())
        camisas.append((cor, tam, nome))
    
    camisas.sort(key=lambda x: (x[0], tamanho(x[1]), x[2]))

    if cont!=0:
        print()
    for c in camisas:
        print(c[0], c[1], c[2])
    cont+=1
