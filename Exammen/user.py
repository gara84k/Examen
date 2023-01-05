from account import Account

class User(Account):
    idUser = int
    def __init__(self, cedula, nombre, genero, telefono, edad, correo, clave, idUser):
        super().__init__(cedula, nombre, genero, telefono, edad, correo, clave)
        self.idUser = idUser