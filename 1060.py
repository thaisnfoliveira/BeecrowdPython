i = 0
positivo = 0
while i<6:
    num = float(input())
    if num>0:
        positivo += 1
    i +=1
print(f"{positivo} valores positivos")