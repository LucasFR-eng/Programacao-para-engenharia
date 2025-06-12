lista = []
medias = []
for i in range(10):
    print("Aluno número",i + 1)
    for o in range(4):
        nota = int(input("Digite a nota tirada:"))
        lista.append(nota)
    media = (sum(lista) / 4)
    medias.append(media)
aprovados = 0  
for media in medias:   
    if media >= 7:
       aprovados += 1
print("Número de alunos aprovados:",aprovados)