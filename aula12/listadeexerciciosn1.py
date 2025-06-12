lista = []
soma = []
while True:
    x = int(input("Digite um número inteiro:"))
    if x == -1:
        print("Programa encerrado!")
        break
    soma.append(x)
    soma_total = (sum(soma))
    media = (sum(soma) / len(soma))
print("A soma dos números deu:", soma_total)
print("A média dos números deu:",media)
print("Número menor e maior:",[min(soma), max(soma)])