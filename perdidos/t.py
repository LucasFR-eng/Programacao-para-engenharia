valor = int(input("Digite a quantidade recebida:"))
notas = (100 , 50 , 20 , 10 , 5 , 2)

notas100 = int(valor / notas[0])
valor = valor % notas[0]
print("Entregar",notas100,"notas de",notas[0])

notas50 = int(valor / notas[1])
valor = valor % notas[1]
print("Entregar",notas50,"notas de",notas[1])

notas20 = int(valor / notas[2])
valor = valor % notas[2]
print("Entregar",notas20,"notas de",notas[2])

notas10 = int(valor / notas[3])
valor = valor % notas[3]
print("Entregar",notas10,"notas de",notas[3])

notas5 = int(valor / notas[4])
valor = valor % notas[4]
print("Entregar",notas5,"notas de",notas[4])

notas2 = int(valor / notas[5])
valor = valor % notas[5]
print("Entregar",notas2,"notas de",notas[5])