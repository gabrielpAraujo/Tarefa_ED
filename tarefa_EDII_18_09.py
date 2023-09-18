import time
import timeit

# adicionando valores a lista
def add_lista():
    lista = []
    for it, i in enumerate(range(0,10000000)):
        lista.append(it)   

    return lista 

lista = add_lista()

def busca_linear(elemento, lista):
    for i, num in enumerate(lista):
        if num == elemento:
            return f'Elemento {elemento} encontrado na posicao {i}'
    return f'Elemento {elemento} nao encontrado'
    
def busca_binaria(lista, elemento, inicio, fim):
    if inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == elemento:
            return f'Resultado encontrado na posicao {meio}!'
        elif lista[meio] < elemento:
            return busca_binaria(lista, elemento, meio + 1, fim)
        else:
            return busca_binaria(lista, elemento, inicio, meio - 1)

    else:
        return f'Elemento {elemento} não encontrado.'
    
def calcula_tempo_funcao(funcao):
    inicio = timeit.default_timer()
    print(funcao)
    fim = timeit.default_timer()
    print(f'Tempo utilizado: {round((fim - inicio) * 100000, 2)}') # multipliquei para que não resultasse em um número muito pequeno

# ENTRADA DE DADOS

print("TESTE LINEAR")
calcula_tempo_funcao(busca_linear(0, lista))

print()
print()

print("TESTE BINARIO")
calcula_tempo_funcao(busca_binaria(lista, 0, 0, len(lista) - 1))