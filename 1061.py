datainicio = int(input("Dia "))
horai, minutoi, segundoi = map(int, input().split(" : "))
datafim = int(input("Dia "))
horaf, minutof, segundof = map(int, input().split(" : "))
dia = datafim - datainicio
horas = horaf - horai
minutos = minutof - minutoi
segundos = segundof - segundoi
print(f"{dia} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")