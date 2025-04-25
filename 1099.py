n = int(input())
for i in range(n):
    soma = 0
    x, y = map(int, input().split())
    if x == y and x%2==1:
        soma = x
    elif x<y:
        ini = x + 1
        if x%2 == 0:
            ini = x+1
        for a in range(ini, y):
            if a%2!=0:
                soma+=a
    else:
        for a in range(x+1, y, 1):
            if a%2!=0:
                soma+=a
    print(soma)