
n = int(input())

def eh_primo(x):
    if x<=1:
        return False
    if x==2:
        return True
    if x%2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

for _ in range(n):
    x = int(input())
    if eh_primo(x):
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")