q = 0
for i in range(5):
    n = int(input("Digite um número inteiro:"))

    if n % 2 == 0:
        q += 1

print("Quantidade de números pares digitados:", q)