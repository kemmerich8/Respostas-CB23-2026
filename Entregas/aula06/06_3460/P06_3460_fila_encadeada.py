# Fila encadeada - Nícolas Kemmerich
import importlib

modulo_pilha = importlib.import_module("06_3460_pilha_encadeada")
PilhaEncadeada = modulo_pilha.PilhaEncadeada

class FilaEncadeada:
    def __init__(self):
        self._pilha_entrada = PilhaEncadeada()
        self._pilha_saida = PilhaEncadeada()

    def enfileirar(self, item):
        self._pilha_entrada.push(item)


    def esta_vazia(self):
        return self._pilha_entrada.esta_vazia() and self._pilha_saida.esta_vazia()
            

    def transferir_se_precisar(self):
        if self._pilha_saida.esta_vazia():
            while not self._pilha_entrada.esta_vazia():
                self._pilha_saida.push(self._pilha_entrada.pop())

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("Fila vazia, não há elementos.")
        self.transferir_se_precisar()
        return self._pilha_saida.pop()

    def frente(self):
        if self.esta_vazia():
            raise IndexError("Fila vazia, não há elementos na frente.")
        self.transferir_se_precisar()
        return self._pilha_saida.topo()

    def __len__(self):
        return len(self._pilha_entrada) + len(self._pilha_saida)

    def __repr__(self):
        elementos_saida = []
        atual = self._pilha_saida._topo
        while atual is not None:
            elementos_saida.append(repr(atual.valor))
            atual = atual.proximo

        elementos_entrada = []
        atual = self._pilha_entrada._topo
        while atual is not None:
            elementos_entrada.insert(0, repr(atual.valor))
            atual = atual.proximo       

        todos = elementos_saida + elementos_entrada
        return "Fila (" + " -> ".join(todos) + ")"