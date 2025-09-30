class No:
    def __init__(self,valor):
        self.atual = None
        self.proximo = None
        self.valor = valor


    def mostrarNo(self):
        print(self.valor)


class Lista_encadeada:
    def __init__(self,valor):
        self.primeiro = None
        self.valor = valor

    def inserir_inicio(self,valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if self.primeiro == None:
            print("Lista vazia!")
            return None
        self.atual = self.primeiro
        while self.atual != None:
            self.atual.mostrarNo()
            self.atual = self.atual.proximo

    def excluir_inicio(self):
        if self.primeiro == None:
            print("Lista vazia!")
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp
    
    def pesquisar(self,valor):
        if self.primeiro == None:
            print("Lista vazia!")
            return None
        self.atual = self.primeiro
        while self.atual.valor != valor:
            if self.atual.proximo == None:
                return None
            else:
                self.atual = atual.proximo
                return self.atual
            
            
    def excluir_qualquer_valor(self,valor):
        if self.primeiro == None:
            print("Lista vazia!")
            return None
        self.atual = self.primeiro
        anterior = self.primeiro
        while self.atual.valor != valor:
            if self.atual.proximo == None:
                return None
            else:
                anterior = self.atual
                self.atual = self.atual.proximo
            if self.atual == self.primeiro:
                self.primeiro = self.primeiro.proximo
            else:
                anterior.proximo = self.atual.proximo
                return self.atual

lista = Lista_encadeada(5)

lista.inserir_inicio("S")
lista.inserir_inicio("A")
lista.inserir_inicio("C")
lista.inserir_inicio("U")
lista.inserir_inicio("L")
lista.mostrar()
lista.excluir_inicio()
print("------------------------------------------------------------------------------------------------------------------------------------------------")
lista.mostrar()
print("------------------------------------------------------------------------------------------------------------------------------------------------")
print(lista.pesquisar("S"))