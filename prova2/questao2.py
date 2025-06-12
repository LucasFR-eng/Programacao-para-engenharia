carros = []
consumos = []
quantidade = 5
preco_gasolina = 6.25
i = 0
while i < quantidade:
    modelo = input("Digite o modelo do carro:")
    if modelo == "":
        print("Modelo nao pode ser vazio")
    else:
        carros.append(modelo)
        while True:
            consumo_str = input("quantos km por litro:")
            if consumo_str.replace('.',"",1).isdigit():
                consumo = float(consumo_str)
                if consumo > 0:
                    consumos.append(consumo)
                    break
                else:
                    print("o consumo deve ser maior que zero")
            else:
                print("Digite um numero valido")
        i += 1
print("Relatorios de consumo")
i = 0
menor = consumos[0]
mais = carros[0]
while i < quantidade:
    litros = 1000 / consumos[1]
    custo = litros + preco_gasolina
    if consumos[i] > menor:
        menor = consumos[i]
        mais = carros[i]
    i += 1
print("O carro mais economico é:",mais)
print("Com o menor consumo de:",menor)