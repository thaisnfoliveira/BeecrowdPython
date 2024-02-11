n = int(input())
for i in range(1, n+1, 1):
    a, b, c = map(float, input().split(" "))
    mediapond = ((a*2)+(b*3)+(c*5))/10
    print("%0.1f"%mediapond)