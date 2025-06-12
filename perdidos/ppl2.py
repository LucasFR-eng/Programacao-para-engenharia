lista = list()

print("Insira valores 5 inteiros do seu desejo na lista!")

x1 = int(input("insira o primeiro valor:"))
x2 = int(input("insira o segundo valor:"))
x3 = int(input("insira o terceiro valor:"))
x4 = int(input("insira o quarto valor:"))
x5 = int(input("insira o quinto valor:"))

lista.append(x1)
lista.append(x2)
lista.append(x3)
lista.append(x4)
lista.append(x5)

x = int(input("1 - para lista normal e 2 - para lista inversa 3 - para crescente  4 - para decrescente 5 - para maior , menor ou somatoria da lista:"))

if x == 1:
    print(lista)

elif x == 2:
    lista.reverse()
    print(lista)

elif x == 3:
    lista.sort(reverse=False)
    print(lista)

elif x == 4:
    lista.sort(reverse=True)
    print(lista)

elif x == 5:
    z = int(input("Digite 1 - max,  2 - min,  3 -somatoria:"))
    if z == 1:
        print(max(lista))

    elif z == 2:
        print(min(lista))

    elif z == 3:
        print(sum(lista))

    else:
        print("Valores incorretos!")

else:
    print("Error!")