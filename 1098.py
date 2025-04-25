i = 0.0
while i <= 2.0 + 1e-9:
    for j in range(1, 4):
        valor_i = round(i, 1)
        valor_j = round(i + j, 1)
        if valor_i.is_integer():
            print(f"I={int(valor_i)} J={int(valor_j)}")
        else:
            print(f"I={valor_i} J={valor_j}")
    i += 0.2
