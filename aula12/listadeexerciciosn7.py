import math
vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)
media = sum(vendas) / len(vendas)
variancia = sum((x - media) ** 2 for x in vendas) / len(vendas)
desvio_padrao = math.sqrt(variancia)
print("Média:", media)
print("Variância:",variancia)
print("Desvio padrão", desvio_padrao)