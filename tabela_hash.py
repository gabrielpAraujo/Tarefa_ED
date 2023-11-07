class Noh:
    def _init_(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.prox = None

class Tabela_de_hash:
    def _init_(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def funcao_de_hash(self, chave):
        return hash(chave) % self.tamanho

    def insert(self, chave, valor):
        indice = self.funcao_de_hash(chave)
        novo_noh = Noh(chave, valor)
        
        if self.tabela[indice] is None:
            self.tabela[indice] = novo_noh
        else:
            atual = self.tabela[indice]
            while atual.prox:
                atual = atual.prox
            atual.prox = novo_noh

    def procurar(self, chave):
        indice = self.funcao_de_hash(chave)
        atual = self.tabela[indice]

        while atual:
            if atual.chave == chave:
                return atual.valor
            atual = atual.prox
        
        return None

    def remove(self, chave):
        indice = self.funcao_de_hash(chave)
        atual = self.tabela[indice]
        anterior = None

        while atual:
            if atual.chave == chave:
                if anterior:
                    anterior.prox = atual.prox
                else:
                    self.tabela[indice] = atual.prox
                return
            anterior = atual
            atual = atual.prox

        raise KeyError(f"Chave não encontrada: {chave}")

tabela_de_hash = Tabela_de_hash(5)
tabela_de_hash.insert("Python", "Linguagem de programação")
tabela_de_hash.insert("Java", "Linguagem de programação")
tabela_de_hash.insert("C++", "Linguagem de programação")

print(tabela_de_hash.procurar("Python"))  
print(tabela_de_hash.procurar("Java"))   
print(tabela_de_hash.procurar("C++"))    

tabela_de_hash.remove("Java")
print(tabela_de_hash.procurar("Java")) 