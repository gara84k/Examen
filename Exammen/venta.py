from user import User
from producto import Producto
from paymet import Payment


class Venta(Producto, Payment):
    idventa = int
    user  = User("", "", "", "", "", "", "", "")
    producto = Producto("", "", "", "", "")
    paymet = Payment("", "", "", "")
    
    def __init__(self, idventa, user, producto, payment):
        self.idventa  = idventa
        self.user     = user
        self.producto = producto
        self.paymet   = payment