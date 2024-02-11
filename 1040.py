notas = input().split()
n1, n2, n3, n4 = notas
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
print("Media: %0.1f"%media)
if media>=7.0:
    print("Aluno aprovado.")
elif media<5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %0.1f"%exame)
    median = (media+exame)/2
    if median>=5.0:
        print("Aluno aprovado.")
    if median<5.0:
        print("Aluno reprovado")
    print("Media final: %0.1f"%median)