n = int(input())
i = 0
em = 0
out = 0
while i<n:
    x = int(input())
    if x>=10 and x<=20:
        em += 1
    else:
        out += 1
    i+=1
print(f"{em} in")
print(f"{out} out")