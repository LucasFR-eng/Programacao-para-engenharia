valor = int(input("Insira o valor recebido:"))
notas = (100 , 50 , 20 , 10 , 5 , 2)
i = 0
while i < len(notas):
    quantidade = int(valor / notas[i])
    valor = valor % notas[i]
    if quantidade != 0:
        print("Entregue",quantidade,"notas de",notas[i])
    i += 1