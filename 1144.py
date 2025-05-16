n = int(input())

c = 1
for i in range(n):
    print(f"{c} {c**2} {c**3}")
    print(f"{c} {(c**2)+1} {(c**3)+1}")
    c+=1