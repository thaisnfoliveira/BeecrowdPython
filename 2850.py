while True:
    try:
        l = input().upper().strip()
        if l == "ESQUERDA":
            print('ingles')
        elif l == "DIREITA":
            print("frances")
        elif l == "NENHUMA":
            print("portugues")
        elif l == "AS DUAS":
            print("caiu")
    except EOFError:
        break