n = int(input())

for _ in range(n):
    dieta = input()
    cafe = input()
    almoco = input()

    contagem = {}
    for a in dieta:
        contagem[a] = contagem.get(a, 0)+1
    
    for a in cafe:
        if a not in contagem or contagem[a] == 0:
            print("CHEATER")
            break
        contagem[a] -= 1
    else:
        for a in almoco:
            if a not in contagem or contagem[a] == 0:
                print("CHEATER")
                break
            contagem[a] -= 1
        else:
            jantar = []
            for a, qtd in contagem.items():
                jantar.extend([a]*qtd)
            
            jantar.sort()
            print(''.join(jantar))
    