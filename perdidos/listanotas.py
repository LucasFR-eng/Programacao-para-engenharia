lista = list()

x1 = float(input("Digite a primeira nota:"))
x2 = float(input("Digite a segunda nota:"))
x3 = float(input("Digite a terceira nota:"))

lista.append(x1)
lista.append(x2)
lista.append(x3)

z = int(input("1 - nota mais alta, 2 - nota mais baixa, 3 - média das notas:"))

if z == 1:
    lista.sort(reverse=False)
    print("A nota mais alta é:")
    print(max(lista))
    print("Entre essas:",lista)

elif z == 2:
    lista.sort(reverse=False)
    print("A nota mais baixa é:")
    print(min(lista))
    print("Entre essas:",lista)

elif z == 3:
    n = ((x1 + x2 + x3) / 3)
    print("A média das notas deu:",n)
