vetor = []
for i in range(20):
    n = int(input())
    vetor.append(n)

cont = 0
for i in range(len(vetor)-1, -1, -1):
    print(f"N[{cont}] = {vetor[i]}")
    cont+=1