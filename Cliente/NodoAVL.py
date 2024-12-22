from .Cliente import Cliente

class NodoAVL:
    def __init__(self, cliente : Cliente):
        self.cliente = cliente
        self.izq = None
        self.der = None

