peca1 = input().split()
peca2 = input().split()

cod1, num1, valor1 = peca1
cod2, num2, valor2 = peca2

valor = (int(num1)*float(valor1)) + (int(num2)*float(valor2))

print("VALOR A PAGAR: R$ %0.2f"%valor)