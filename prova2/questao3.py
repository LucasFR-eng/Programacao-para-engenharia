gabarito = ("A","B","C","D","A","B","C","D","A","B")
notas = []
total_alunos = 0
while True:
    respostas = []
    i = 0
    while i < 10:
        resposta = input("Digite a resposta da questao:").upper()
        if resposta in ["A","B","C","D"]:
            respostas.append(resposta)
            i += 1
        else:
            print("Rsposta invalida")
    acertos = 0
    i = 0
    while i < 10:
        if respostas[i] == gabarito[i]:
            acertos += 1
        i += 1
    notas.append(acertos)
    total_alunos += 1
    continuar = input("Outro aluno vai utilizar o sistema S/N:").upper()
    if continuar != "S":
        break
if total_alunos > 0 :
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / total_alunos
    print("total de alunos:", total_alunos)
    print("Maior nota:", maior)
    print("Menor nota:", menor)
    print("Média da turma:",media)
else:
    print("Nenhum aluno utilizou o sistema")
