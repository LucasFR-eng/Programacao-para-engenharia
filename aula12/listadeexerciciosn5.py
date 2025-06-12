lista = []
a = int(input("Insira o tamanho da lista:"))
for i in range(a):
    x = int(input("Digite um número:"))
    lista.append(x)
    if  x % 2 != 0:
        lista.remove(x)
print(lista)