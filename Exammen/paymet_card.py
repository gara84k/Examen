from paymet import Payment
class PaymentCard(Payment):
    cuenta      = int
    banco       = str
    datoTarjeta = []
    
    def __init__(self, id, valor, fecha, cuenta, banco, user, datoTarjeta):
        super().__init__(id, valor, fecha, user)
        self.cuenta      = cuenta
        self.banco       = banco
        self.datoTarjeta = datoTarjeta