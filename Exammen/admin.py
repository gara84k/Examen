from account import Account

class Admin(Account):
    idAdmin = int
    def __init__(self, cedula, nombre, genero, telefono, edad, correo, clave, idAdmin):
        super().__init__(cedula, nombre, genero, telefono, edad, correo, clave)
        self.idAdmin = idAdmin