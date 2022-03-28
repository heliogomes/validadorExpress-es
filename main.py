import numpy as np


class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__top = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_vazia(self):
        if self.__top == -1:
            return True
        else:
            return False

    def __pilha_cheia(self):
        if self.__capacidade == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__capacidade == -1:
            print('pilha cheia')
        else:
            self.__top += 1
            self.__valores[self.__top] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha está vazia ')
        else:
            self.__top -= 1

    def ver_top(self):
        if self.__top != -1:
            return self.__valores[self.__top]
        else:
            return -1

#Validador de expressões
expressão = input("Digite a expressão a ser validada:")
x = 0
pilha = []
while x < len(expressão):
    if expressão[x] == "(":
        pilha.append("(")
    if expressão[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")
            break
    if expressão[x] == "{":
        pilha.append("{")
    if expressão[x] == "}":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append("}")
            break
    if expressão[x] == "[":
        pilha.append("[")
    if expressão[x] == "]":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append("]")
            break

    x = x + 1
if len(pilha) == 0:
    print("Está expressão é válida")
else:
    print("Está expressão não é válida")


