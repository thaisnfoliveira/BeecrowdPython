t = int(input())
lista = list(map(int, input().split()))
cont = 0

for i in lista:
    if i == t:
        cont += 1

print(cont)

