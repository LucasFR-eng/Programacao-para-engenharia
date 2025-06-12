d = []
medias = []
while True:
    nome = input("Digite o seu nome:")
    d.append(nome)
    if nome == "":
       print("Encerrando o programa")
       break
    if nome != "":
        for i in range(5):
            saltos = int(input("Digite a distanca do seu salto:"))
            medias.append(saltos)
            media = sum(medias) / len(medias)
print("atletas:",d)
print("quantidade de saltos somando todos:",len(medias))
print("Média total:",media)