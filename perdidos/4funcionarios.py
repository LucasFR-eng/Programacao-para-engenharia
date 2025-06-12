f = {}
for i in range(4):
    x = input("Insira o nome do funcionário:")
    y = int(input("Insira o número:"))
    f[y] = {"nome": x, "Número": y}
d = int(input("Digite o número do funcionário q deseja demitir:"))
if d in f:
    demitido = f.pop(d)
    print(f"Funcionário {demitido["nome"]} demitido")
    print("Número de funcionários restantes:", len(f))
else:
    print("ERROR")