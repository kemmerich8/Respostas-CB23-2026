# Pilha Encadeada - Nícolas Kemmerich
class _No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        novo_no = _No(item)
        novo_no.proximo = self._topo
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        if self._topo == None:
            raise IndexError("Pilha vazia, não há mais elementos para serem removidos.")
        valor_removido = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1

        return valor_removido

    def esta_vazia(self):
        return self._tamanho == 0

    def topo(self):
        if self.esta_vazia():
            raise IndexError("Esta vazia, não há elementos no topo.")
        return self._topo.valor

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        elementos = []
        atual = self._topo
        while atual is not None:
            elementos.append(repr(atual.valor))
            atual = atual.proximo
        return "Pilha(" + " -> ".join(elementos) +")"