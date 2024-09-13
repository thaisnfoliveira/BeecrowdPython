alcool = 0
gasolina = 0
diesel = 0
n = 0

while(n<1 or n>4 or n!=4):
    n = int(input())
    if n == 1:
        alcool +=1
    elif n == 2:
        gasolina += 1
    elif n == 3:
        diesel +=1

print(f"MUITO OBRIGADO\nAlcool: "+str(alcool)+"\nGasolina: "+str(gasolina)+"\nDiesel: "+str(diesel))
