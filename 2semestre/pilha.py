class Pilha:
    def __init__(self, tamanho_pilha):
        self.tamanho = tamanho_pilha
        self.topo = -1
        self.valores = [None] * tamanho_pilha
    
    def pilha_cheia(self):
        return self.topo == self.tamanho - 1
    
    def empilhar(self, valor):
        if self.pilha_cheia():
            print("Pilha cheia")
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return None
        
    def pilha_vazia(self):
        return self.topo == -1
    
    def desempilhar(self):
        if self.pilha_vazia():
            print("Pilha vazia")
            return None
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor

pilha1 = Pilha(5)

pilha1.empilhar(10)
pilha1.empilhar(20)
pilha1.empilhar(30)
pilha1.empilhar(40)
pilha1.empilhar(50)
print("Antigo topo:",pilha1.ver_topo()) 
print("tirar:",pilha1.desempilhar()) 
print("tirar:",pilha1.desempilhar()) 
print("tirar:",pilha1.desempilhar())
print("tirar:",pilha1.desempilhar())
print("Novo topo:",pilha1.ver_topo())  