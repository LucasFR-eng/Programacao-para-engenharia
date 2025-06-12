i = 0
p1 = []
p2 = []
a = int(input("Insira a quantidade de alunos na turma:"))
for i in range(a):
    print("Aluno número",i+ 1)
    nota1 = float(input("Insira a nota tirada na primeira prova:"))
    p1.append(nota1)
    nota2 = float(input("Insira a nota tirada na segunda prova:"))
    p2.append(nota2)
media1 = sum(p1) / a
media2 = sum(p2) / a
print("Média da turma na prova 1:",media1)
print("Média da turma na prova 2:",media2)
if media1 > media2:
    print("A turma obteve a melhor média na prova 1")
elif media1 < media2:
    print("A turma obteve a melhor média na prova 2")
elif media1 == media2:
    print("A média nas duas provas foi a mesma!")
else:
    print("ERROR!")