class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.itens = [None] * tamanho
        self.topo = -1

    def pilhaVazia(self):
        return self.topo == -1

    def pilhaCheia(self):
        return self.topo == self.tamanho - 1

    def empilhar(self, valor):
        if self.pilhaCheia():
            print(f" Não é possível empilhar '{valor}': Pilha cheia.")
            return False
        else:
            self.topo += 1
            self.itens[self.topo] = valor
            print(f" Empilhado: '{valor}'")
            return True

    def desempilhar(self):
        if self.pilhaVazia():
            print(" Não é possível desempilhar: Pilha vazia.")
            return None
        else:
            valor = self.itens[self.topo]
            self.itens[self.topo] = None
            self.topo -= 1
            print(f" Desempilhado: '{valor}'")
            return valor

    def elementoTopo(self):
        if self.pilhaVazia():
            return None
        return self.itens[self.topo]

    def exibir(self):
        print(" Pilha:", self.itens[:self.topo + 1])

pilha = Pilha(10)        
pilha.desempilhar()       
