positivo = 0
soma = 0
for i in range(6):
    num = float(input())
    if num>0:
        positivo += 1
        soma = soma+num
media = soma/positivo
print(f"{positivo} valores positivos")
print(f"{media:.1f}")