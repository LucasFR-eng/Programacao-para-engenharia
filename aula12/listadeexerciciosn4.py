lista1 = []
lista2 = []
lista3 = []
for i in range(5):
    n1 = int(input("Digite um número para a primeira lista:"))
    lista1.append(n1)
for i in range(5):
    n2 = int(input("Digite um número para a segunda lista:"))
    lista2.append(n2)
for i in range(5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print("Primeira lista:",lista1)
print("Segunda lista:",lista2)
print("Terceira lista:",lista3)