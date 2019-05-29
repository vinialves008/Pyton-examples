import random as r

def geraListaAleatoria(tam):
    lista  = []
    for i in range(tam):
        lista.append(r.randint(0,tam))
    return lista
