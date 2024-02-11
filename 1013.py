valores = input().split()
a, b, c = valores
a = int(a)
b = int(b)
c = int(c)
maiorab = (a+b+abs(a-b))/2
maior = (maiorab + c + abs(maiorab-c))/2
print(f"{int(maior)} eh o maior")