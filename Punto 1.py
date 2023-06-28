class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

def combinar(L1, L2):
    # Verificar si alguna de las listas está vacía
    if not L1:
        return L2
    if not L2:
        return L1

    # Inicializar la lista combinada
    L3 = None

    # Elegir el nodo inicial de L3
    if L1.dato <= L2.dato:
        L3 = L1
        L1 = L1.siguiente
    else:
        L3 = L2
        L2 = L2.siguiente

    # Mantener un puntero al nodo actual de L3
    actual = L3

    # Combinar los nodos de L1 y L2 en L3
    while L1 and L2:
        if L1.dato <= L2.dato:
            actual.siguiente = L1
            L1 = L1.siguiente
        else:
            actual.siguiente = L2
            L2 = L2.siguiente
        actual = actual.siguiente

    # Agregar los nodos restantes de L1 o L2 a L3
    if L1:
        actual.siguiente = L1
    elif L2:
        actual.siguiente = L2

    return L3

def imprimir_lista(lista):
    # Verificar si la lista está vacía
    if not lista:
        print("None")
        return

    # Imprimir los elementos de la lista
    while lista:
        print(lista.dato, end=" -> ")
        lista = lista.siguiente
    print("None")

#----------------------------------------------------------------------------------------------------------------------
#Ejemplos:

print("----------")
print("Ejemplo 1")
print("")
# Lista 1: 1 -> 3 -> 5 -> 7 -> None
nodo1 = Nodo(1)
nodo2 = Nodo(3)
nodo3 = Nodo(5)
nodo4 = Nodo(7)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
lista1 = nodo1

# Lista 2: 2 -> 4 -> 6 -> None
nodo5 = Nodo(2)
nodo6 = Nodo(4)
nodo7 = Nodo(6)
nodo5.siguiente = nodo6
nodo6.siguiente = nodo7
lista2 = nodo5

print("Lista 1: 1 -> 3 -> 5 -> 7 -> None" )
print("Lista 2: 2 -> 4 -> 6 -> None")

# Combinar las listas
resultado = combinar(lista1, lista2)

# Imprimir el resultado: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
print("Lista 3:") 
imprimir_lista(resultado)
print("----------")

print("Ejemplo 2")
print("")
# Lista 1: 1 -> 2 -> 3 -> 3 -> 5 -> None
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(3)
nodo5 = Nodo(5)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
lista1 = nodo1

# Lista 2: 2 -> 3 -> 4 -> 4 -> 6 -> 6 -> None
nodo6 = Nodo(2)
nodo7 = Nodo(3)
nodo8 = Nodo(4)
nodo9 = Nodo(4)
nodo10 = Nodo(6)
nodo11 = Nodo(6)
nodo6.siguiente = nodo7
nodo7.siguiente = nodo8
nodo8.siguiente = nodo9
nodo9.siguiente = nodo10
nodo10.siguiente = nodo11
lista2 = nodo6

print("Lista 1: 1 -> 2 -> 3 -> 3 -> 5 -> None" )
print("Lista 2: 2 -> 3 -> 4 -> 4 -> 6 -> 6 -> None")

# Combinar las listas
resultado = combinar(lista1, lista2)

# Imprimir el resultado: 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 4 -> 4 -> 5 -> 6 -> 6 -> None
print("Lista 3:") 
imprimir_lista(resultado)
print("----------")

print("Ejemplo 3")
print("")
# Lista 1: 2 -> 4 -> 6 -> 8 -> None
nodo1 = Nodo(2)
nodo2 = Nodo(4)
nodo3 = Nodo(6)
nodo4 = Nodo(8)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
lista1 = nodo1

# Lista 2: 1 -> 3 -> 5 -> None
nodo5 = Nodo(1)
nodo6 = Nodo(3)
nodo7 = Nodo(5)
nodo5.siguiente = nodo6
nodo6.siguiente = nodo7
lista2 = nodo5

print("Lista 1: 2 -> 4 -> 6 -> 8 -> None" )
print("Lista 2: 1 -> 3 -> 5 -> None")

# Combinar las listas
resultado = combinar(lista1, lista2)

# Imprimir el resultado: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 8 -> None
print("Lista 3:") 
imprimir_lista(resultado)
print("----------")