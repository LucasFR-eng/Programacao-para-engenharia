frase = input("Digite uma frase:")
contagem = {}
i = 0
while i < len(frase):
    caractere = frase[i]
    if caractere in contagem:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1
    i += 1
print("Contagem de caracteres:")
for caractere in contagem:
    print({caractere: contagem[caractere] for caractere in contagem})