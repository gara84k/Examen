from producto import Producto

class Ninios(Producto):
    def __init__(self, nombre, talla, color, precio, tipo):
        super().__init__(nombre, talla, color, precio, tipo)