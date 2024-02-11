numeros = input().split()
a, b, c = numeros
a = float(a)
b = float(b)
c = float(c)
if a+b>c and b+c>a and a+c>b:
    perimetro = a+b+c
    print("Perimetro = %0.1f"%perimetro)
else:
    area = ((a+b)*c)/2
    print("Area = %0.1f"%area)
    