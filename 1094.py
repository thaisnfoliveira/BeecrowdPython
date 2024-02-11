rato = 0
sapo = 0
coelho = 0
total = 0
n = int(input())
for i in range(1, n+1, 1):
    caso = input().split()
    quantia, tipo = caso
    quantia = int(quantia)
    if tipo=="C":
        coelho = coelho + quantia
    elif tipo=="R":
        rato = rato+quantia
    elif tipo=="S":
        sapo = sapo + quantia
    total = total + quantia
percentualc = (coelho*100)/total
percentualr = (rato*100)/total
percentuals = (sapo*100)/total
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print("Percentual de coelhos: {:.2f} %".format(percentualc))
print("Percentual de ratos: {:.2f} %".format(percentualr))
print("Percentual de sapos: {:.2f} %".format(percentuals))