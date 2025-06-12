lista = []
for i in range(10):
    x = int(input("Digite um número inteiro:"))
    lista.append(x)
lista.sort(reverse=True)
print(lista)