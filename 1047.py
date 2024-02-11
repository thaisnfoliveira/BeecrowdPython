horas = input().split()
hi, mi, hf, mf = horas
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)
if hi>hf:
    dh = (24-hi)+hf
elif hi==hf:
    dh = 24
    if mi == mf:
        dm = 0
else:
    dh = hf - hi
if mi>mf:
    dm = (60-mi)+mf
else:
    dm = mf-mi
print(f"O JOGO DUROU {dh} HORA(S) e {dm} MINUTO(S)")