sal = float(input())
if sal<=400.00:
    new = sal*0.15
    sal = new+sal
    reaj = 15
elif sal>400.00 and sal<=800.00:
    new = sal*0.12
    sal = new+sal
    reaj = 12
elif sal>800.00 and sal<=1200.00:
    new = sal*0.1
    sal = new+sal
    reaj = 10
elif sal>1200.00 and sal<=2000.00:
    new = sal*0.07
    sal = new+sal
    reaj = 7
else:
    new = sal*0.04
    sal = new+sal
    reaj = 4
print("Novo salario: %0.2f"%sal)
print("Reajuste ganho: %0.2f"%new)
print(f"Em percentual: {reaj} %")