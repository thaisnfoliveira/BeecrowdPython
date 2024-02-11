i = 0
par = 0
while i<5:
    num = int(input())
    if num%2==0:
        par += 1
    i +=1
print(f"{par} valores pares")