n = int(input())

numbers = set()

for i in range(1, n+1):
    numbers.add(i)

num = list(map(int, input().split()))

for n in numbers:
    if n not in num:
        print(n)
        break