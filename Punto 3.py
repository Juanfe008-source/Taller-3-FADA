class PilaConColas:
    def __init__(self):
        self.q = Cola()

    def estaVaciaPilaConColas(self):
        return self.q.estaVaciaPilaConColas()

    def pushPilaConColas(self, objeto):
        self.q.encolar(objeto)

    def popPilaConColas(self):
        if self.estaVaciaPilaConColas():
            print("Pila vacía")
            return None

        for _ in range(self.q.obtener_tamano() - 1):
            desencolado = self.q.desencolar()
            self.q.encolar(desencolado)
        return self.q.desencolar()

    def mostrarPilaConColas(self):
        elementos = []
        while not self.estaVaciaPilaConColas():
            elemento = self.q.desencolar()
            elementos.append(elemento)

        for i in range(len(elementos) - 1, -1, -1):
            print(elementos[i])

        for elemento in elementos:
            self.q.encolar(elemento)


class Cola:
    def __init__(self):
        self.items = []
        self.tamano = 0

    def estaVaciaPilaConColas(self):
        return self.items == []

    def encolar(self, objeto):
        self.tamano += 1
        self.items.append(objeto)

    def desencolar(self):
        if self.estaVaciaPilaConColas():
            return None
        self.tamano -= 1
        return self.items.pop(0)

    def obtener_tamano(self):
        return self.tamano

#--------------------------------------------------------------------------------------------------------------------
# Ejemplos:
 
print("--------------------")
print("Ejemplo 1: Valores Numericos")
print("")
pila = PilaConColas()
pila.pushPilaConColas(1) #Primer elemento
pila.pushPilaConColas(27) #Segundo elemento
pila.pushPilaConColas(3) #Tercer elemento
pila.pushPilaConColas(40) #Cuarto elemento
pila.mostrarPilaConColas() #Imprime pila
print("")
pila.popPilaConColas() #Elimina 40
pila.mostrarPilaConColas() #Imprime
print("")
pila.popPilaConColas() #Elimina 3
pila.popPilaConColas() #Elimina 27
pila.popPilaConColas() #Elimina 1
pila.popPilaConColas() #Pila vacia
print("--------------------")

print("Ejemplo 2: Cadenas de texto")
print("")
pila = PilaConColas()
pila.pushPilaConColas("Hola")
pila.pushPilaConColas("mundo")
pila.pushPilaConColas("!")
pila.mostrarPilaConColas()
print("")
pila.popPilaConColas()
pila.mostrarPilaConColas()
print("")
print("Pila vacia?", pila.estaVaciaPilaConColas()) 
print("--------------------")

print("Ejemplo 3: Booleanos")
print("")
pila = PilaConColas()
pila.pushPilaConColas(True)
pila.pushPilaConColas(False)
pila.pushPilaConColas(True)
pila.pushPilaConColas(False)
pila.pushPilaConColas(True)
pila.mostrarPilaConColas()
print("")
pila.popPilaConColas()
pila.popPilaConColas()
pila.popPilaConColas()
pila.mostrarPilaConColas()
print("")
print("Pila vacia?", pila.estaVaciaPilaConColas()) 
print("--------------------")




