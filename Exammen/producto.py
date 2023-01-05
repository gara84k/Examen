class Producto:
    
    nombre = str
    talla  = str
    color  = str
    precio = int
    tipo   = str
    
    def __init__(self, nombre, talla, color, precio, tipo):
        self.nombre = nombre
        self.talla  = talla
        self.color  = color
        self.precio = precio
        self.tipo   = tipo
    
    