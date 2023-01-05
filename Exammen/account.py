class Account:
    cedula   = int
    nombre   = str
    genero   = str
    telefono = int
    edad     = int
    correo   = str
    clave    = str
    
    def __init__(self, cedula, nombre, genero, telefono, edad, correo, clave):
        self.cedula    = cedula
        self.nombre    = nombre
        self.genero    = genero
        self.telefono  = telefono
        self.edad      = edad
        self.correo    = correo
        self.clave     = clave