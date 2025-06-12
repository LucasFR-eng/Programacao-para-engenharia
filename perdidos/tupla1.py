lista = []
a = int(input("Digite o tamanho da lista:"))
for i in range(a):
    x = int(input("Insira um número desejado:"))
    lista.append(x)
    teste = (x % 2)
    if teste == 0:
        lista.remove(x)
print("Lista após a remoção dos números pares:",lista)