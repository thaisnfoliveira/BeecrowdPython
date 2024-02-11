n = int(input())
i = 1
a = 0
while i<=n:
    soma = 0
    x, y = map(int, input().split())
    if x>=y:
        for a in range(y+1, x, 1):
            if a%2!=0:
                soma+=a
    else:
        for a in range(x+1, y, 1):
            if a%2!=0:
                soma+=a
    print(soma)