n = int(input())
notas = list(map(int, input().split()))

freq = {}
for i in notas:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

maiorf = 0
maior = 0
for nota, f in freq.items():
    if f>maiorf:
        maiorf = f
        maior = nota
    elif f == maiorf:
        if maior < nota:
            maior = nota

print(maior)