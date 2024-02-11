i = 0
positivo = 0
soma = 0
while i<6:
    num = float(input())
    if num>0:
        positivo += 1
        soma = soma+num
    i +=1
media = soma/positivo
print(f"{positivo} valores positivos")
print(media)