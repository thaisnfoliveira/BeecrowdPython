horas = input().split()
i, f = horas
i = int(i)
f = int(f)
if i>f:
    duracao = (24-i)+f
elif i==f:
    duracao = 24
else:
    duracao = f - i
print(f"O JOGO DUROU {duracao} HORA(S)")