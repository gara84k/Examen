from user import User

class Payment(User):
    id    = str
    valor = str
    fecha = int
    user  = User("", "", "", "", "", "", "", "")
    
    def __init__(self, id, valor, fecha, user):
        self.id    = id
        self.valor = valor
        self.fecha = fecha
        self.user  = user