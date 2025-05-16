while True:
    m, n = map(int, input().split())
    if m!=0 and n != 0:
        break
    lista = []
    menor = min(m, n)
    maior = max(m, n)
    soma = 0
    for i in range(menor, maior+1):
        lista.append(i)
        soma += i
    
    result = " ".join(lista)+" Sum="+soma
    print(result)
