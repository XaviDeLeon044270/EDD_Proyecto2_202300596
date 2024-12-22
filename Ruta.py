class Ruta:
    def __init__(self, origen, destino, tiempo):
        self.origen = origen
        self.destino = destino
        self.tiempo = tiempo

    def __str__(self):
        return f'Lugar de origen: {self.origen} - Lugar de destino: {self.destino} - Tiempo de ruta: {self.tiempo}'
