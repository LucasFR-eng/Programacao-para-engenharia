lista = list()
for i in range(10):
    x = float(input("Digite um numero da sua escolha:"))
    lista.append(x)
    lista.sort(reverse=True)
print("Lista em forma decrescente:")
print(lista) 