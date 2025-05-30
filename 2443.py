a, b, c, d = map(int, input().split())

def mdc(x, y):
    if y == 0:
        return x
    return mdc(y, x%y)

if b != d:
    d1 = b
    a *= d
    b*= d
    c *= d1
    d *= d1

numerador = a+c
denominador = b

m = mdc(numerador, denominador)

if m != 1:
    numerador /= m
    denominador /= m

print(int(numerador), int(denominador))