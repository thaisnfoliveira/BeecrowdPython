numeros = input().split()
a, b, c = numeros
a = float(a)
b = float(b)
c = float(c)

triangulo = (a*c)/2
circulo = 3.14159*(c**2)
trapezio = ((a+b)*c)/2
quadrado = b**2
retangulo = a*b

print("TRIANGULO: %0.3f"%triangulo)
print("CIRCULO: %0.3f"%circulo)
print("TRAPEZIO: %0.3f"%trapezio)
print("QUADRADO: %0.3f"%quadrado)
print("RETANGULO: %0.3f"%retangulo)