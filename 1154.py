media = 0
cont = 0

while True:
    n = int(input())
    if n < 0:
        break
    media += n
    cont += 1

media = media / cont
print(f"{media:.2f}")