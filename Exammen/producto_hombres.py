from producto import Producto

class Hombre(Producto):
    def __init__(self, nombre, talla, color, precio, tipo):
        super().__init__(nombre, talla, color, precio, tipo)