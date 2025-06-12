lista1 = []
lista2 = []
lista3 = []

for i in range(5):
    numeros1 = int(input("Digite um número para a primeira lista:"))
    lista1.append(numeros1)

for i in range(5):
    numeros2 = int(input("Digite um número para a segunda lista:"))
    lista2.append(numeros2)


lista3 = []
for i in range(5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
    
print("Primeira lista:",lista1)
print("Segunda lista:",lista2)
print("Lista misturada:",lista3)
