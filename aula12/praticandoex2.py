f = {}
for i in range(2):
    x = input("Insira o nome do funcionário: ")
    y = int(input("Insira o número: "))
    z = input("Insira a função: ")
    t = int(input("Insira o tempo em serviço em anos: "))
    f[y] = {"Nome": x, "Número": y, "Função": z, "Tempo": t}

d = int(input("Digite o número do funcionário que deseja demitir: "))   

if d in f:
    demitido = f.pop(d)
    print(f"Funcionário {demitido['Nome']} demitido.")
    print("Número de funcionários restantes:", len(f))
else:
    print("ERROR")