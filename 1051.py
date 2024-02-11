salario = float(input())
if salario<=2000.00:
    print("Isento")
elif salario>2000.00 and salario<=3000.00:
    imposto1 = salario - 2000.00
    imposto1 = 0.08*imposto1
    print("R$ %0.2f"%imposto1)
elif salario>3000.00 and salario<=4500.00:
    imposto1 = salario - 2000.00
    if imposto1 > 1000.00:
        imposto1 = 1000.00
    imposto1 = 0.08*imposto1
    imposto2 = salario - 3000.00
    imposto2 = 0.18*imposto2
    imposto = imposto1+imposto2
    print("R$ %0.2f"%imposto)
elif salario>4500.00:
    imposto1 = salario - 2000.00
    if imposto1 > 1000.00:
        imposto1 = 1000.00
    imposto1 = 0.08*imposto1
    imposto2 = salario - 3000.00
    if imposto2 > 1500.00:
        imposto2 = 1500.00
    imposto2 = 0.18*imposto2
    imposto3 = salario-4500.00
    imposto3 = 0.28*imposto3
    imposto = imposto1+imposto2+imposto3
    print("R$ %0.2f"%imposto)
