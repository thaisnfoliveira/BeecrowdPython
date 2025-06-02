n = int(input())

lista = list(map(int, input().split()))

resp = 0
maior = 0
for i in range(n):
    maior = max(0, maior + lista[i])
    resp = max(resp, maior)

print(resp)