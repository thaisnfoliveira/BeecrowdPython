import sys

while True:
    try:
        x, y, m = map(int, sys.stdin.readline().split())
        for i in range(m):
            xi, yi = map(int, sys.stdin.readline().split())
            if (xi<= x and yi <= y) or (xi <= y and yi <= x):
                sys.stdout.write("Sim\n")
            else:
                sys.stdout.write("Nao\n")
    except ValueError: 
        # Mudei o EOFError para ValueError no except porque map(int, 
        # sys.stdin.readline().split()) pode levantar um ValueError se 
        # sys.stdin.readline() retornar uma string vazia (EOF).
        break