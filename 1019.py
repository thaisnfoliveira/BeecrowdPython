n = int(input())
horas = n//3600
tempo = n - horas*3600
minutos = tempo//60
tempo = tempo-minutos*60
print(f"{horas}:{minutos}:{tempo}")