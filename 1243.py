import re

while True:
    try:
        linha = input()  # Lê uma linha do enunciado
        simbolos = linha.strip().split()  # Separa os símbolos por espaço

        total_letras = 0
        total_palavras = 0

        for simbolo in simbolos:
            # Verifica se o símbolo é uma palavra válida (letras com ou sem ponto final)
            if re.fullmatch(r'[a-zA-Z]+\.?', simbolo):
                # Remove o ponto final, se existir
                if simbolo.endswith('.'):
                    simbolo = simbolo[:-1]
                total_letras += len(simbolo)
                total_palavras += 1

        # Se nenhuma palavra válida, média = 0
        if total_palavras == 0:
            media = 0
        else:
            media = total_letras // total_palavras  # Média inteira

        # Classificação com base na média
        if media <= 3:
            print(250)
        elif media <= 5:
            print(500)
        else:
            print(1000)

    except EOFError:
        break  # Sai do loop quando chegar ao fim da entrada

