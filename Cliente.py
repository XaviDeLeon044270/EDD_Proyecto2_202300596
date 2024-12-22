class Cliente:
    def __init__(self, dpi, nombres, apellidos, genero, telefono, direccion):
        self.dpi = dpi
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f'DPI: {self.dpi} - Nombre completo: {self.nombres} {self.apellidos} - Género: {self.genero} - Teléfono: {self.telefono} - Dirección: {self.direccion}'

class NodoAVL:
    def __init__(self, cliente : Cliente):
        self.cliente = cliente
        self.izq = None
        self.der = None

class ArbolAVL:
    def __init__(self):
        self.raiz: NodoAVL = None

    def insertarNodo(self, raiz: NodoAVL, nodo: NodoAVL):

        if raiz == None:
            self.raiz = nodo
            raiz = nodo
            return

        if nodo.cliente.dpi < raiz.cliente.dpi:
            self.insertarNodo(raiz.izq, nodo)
        else:
            self.insertarNodo(raiz.der, nodo)
        

        return 
    
    def insertarCliente(self, cliente : Cliente):
        nuevoNodo = NodoAVL(cliente)
        self.insertarNodo(self.raiz, nuevoNodo)

        return

    def esHoja(self, nodo) -> bool:
        return nodo.izq == None and nodo.der == None
