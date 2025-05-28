n = int(input())
arr = list(map(int, input().split()))
somatotal = sum(arr)//2
soma = 0
for i in range(n):
    soma += arr[i]
    if soma == somatotal:
        print(i+1)
        break