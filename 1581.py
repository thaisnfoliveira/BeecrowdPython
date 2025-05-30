n = int(input())

for _ in range(n):
    k = int(input())
    idiomas = set()
    for _ in range(k):
        nativo = input()
        idiomas.add(nativo)
    if len(idiomas) == 1:
        print(nativo)
    else:
        print("ingles")