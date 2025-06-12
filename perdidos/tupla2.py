p1 = []
p2 = []
i = 0
a = int(input("Digite quantidade de alunos da turma:"))
for i in range(a):
    print("Aluno numero:",i + 1)
    nota1 = float(input("Digite a sua nota na primeira prova:"))
    p1.append(nota1)
    nota2 = float(input("Digite a sua nota na segunda prova:"))
    p2.append(nota2)
    media1 = sum(p1) / a
    media2 = sum(p2) / a
print("Média da turma na prova 1:",media1)
print("Média da turma na prova 2:",media2)
if media1 > media2:
    print("A turma obteve melhor nota na prova 1")
else:
    print("A turma obteve melhor nota na prova 2")