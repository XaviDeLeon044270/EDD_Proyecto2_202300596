from .NodoAVL import NodoAVL
from .Cliente import Cliente

class ArbolAVL:
    def __init__(self):
        self.raiz: NodoAVL = None

    def insertarNodo(self, raiz: NodoAVL, nodo: NodoAVL):

        if raiz == None:
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
