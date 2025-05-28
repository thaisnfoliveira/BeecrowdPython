while True:
    a, d = map(int, input().split())
    if a == 0 and d == 0:
        break
    atacantes = list(map(int, input().split()))
    defensores = list(map(int, input().split()))

    defensores.sort()
    penultimo = defensores[1]

    for i in atacantes:
        if i < penultimo:
            print("Y")
            break
    else:
        print("N")