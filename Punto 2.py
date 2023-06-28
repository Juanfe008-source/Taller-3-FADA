class Obra:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 1

    def aumentar_cantidad(self):
        self.cantidad += 1

    def disminuir_cantidad(self):
        self.cantidad -= 1


class Nodo_Lista:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Inventario:
    def __init__(self):
        self.inicio = None

    def agregar_replica(self, nombre):
        if self.inicio is None:
            self.inicio = Nodo_Lista(Obra(nombre))
        else:
            actual = self.inicio
            while actual is not None:
                obra = actual.dato
                if obra.nombre == nombre:
                    obra.aumentar_cantidad()
                    return
                actual = actual.siguiente
            nuevo_nodo = Nodo_Lista(Obra(nombre))
            nuevo_nodo.siguiente = self.inicio
            self.inicio = nuevo_nodo

    def vender_replica(self, nombre):
        if self.inicio is None:
            print("el inventario esta vacio")
            return

        if self.inicio.dato.nombre == nombre:
            self.inicio.dato.disminuir_cantidad()
            if self.inicio.dato.cantidad == 0:
                self.inicio = self.inicio.siguiente
            return

        actual = self.inicio
        while actual.siguiente is not None:
            if actual.siguiente.dato.nombre == nombre:
                actual.siguiente.dato.disminuir_cantidad()
                if actual.siguiente.dato.cantidad == 0:
                    actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

        print(f"La obra: {nombre} no existe en el inventario")

    def listar_replicas(self):
        actual = self.inicio
        while actual is not None:
            obra = actual.dato
            print(f"Obra: {obra.nombre}, Cantidad: {obra.cantidad}")
            actual = actual.siguiente


#----------------------------------------------------------------------------------------------------------------------
#Ejemplos:

#Se Crea una lista simplemente enlazada llamada Museo
Museo = Inventario()

#Se agregan varios cuadros a la lista Museo
Museo.agregar_replica("monalisa")
Museo.agregar_replica("monalisa")
Museo.agregar_replica("Venus")
Museo.agregar_replica("El grito")
Museo.agregar_replica("monalisa")

print("------------------------------------------------")
print("Ejemplo de creacion y listado de obras")
Museo.listar_replicas()
print("------------------------------------------------")
print("Ejemplo de venta y relistado de una obra")
Museo.vender_replica("Venus") #Se vende un cuadro de la monalisa

Museo.listar_replicas()
print("------------------------------------------------")
print("Ejemplo de intento de venta de una obra inexistente")
Museo.vender_replica("La ultima Cena")#Se prueba con un cuadro no existente