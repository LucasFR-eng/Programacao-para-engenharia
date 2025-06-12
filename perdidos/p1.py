def menu():
    print("Responda com sabedoria:")
    print("1 - Sim")
    print("2 - Não")
    
while True:
    menu()
    resposta = int(input(":"))

    if resposta == 1:
        print("resposta certa!")
        break

    if resposta == 2:
        print("Acho q o  é vc mn, Tente novamente!")

    
    else:
        print("ERROR!")