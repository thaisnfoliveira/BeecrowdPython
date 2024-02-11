item = input().split()
cod, quant = item
cod = int(cod)
quant = int(quant)
if cod==1:
    total = 4.0*quant
elif cod==2:
    total = 4.5*quant
elif cod==3:
    total = 5.0*quant
elif cod==4:
    total = 2.0*quant
elif cod==5:
    total = 1.5*quant
print("Total: R$ %0.2f"%total)