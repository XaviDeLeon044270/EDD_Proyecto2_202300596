class Vehiculo:
    def __init__(self, placa, marca, modelo, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f'Placa: {self.placa} - Marca: {self.marca} - Modelo: {self.modelo} - Precio: {self.precio}'