class Aluno:
    def __init__(self,nomec,notac,cpfc):
        self.nome = nomec
        self.nota = notac
        self.cpf = cpfc

    def mostrar(self):
        print(self.nome,self.nota,self.cpf)

lucas = Aluno("lucas",2 ,47507129478)

lucas.mostrar()