 #CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO __str__
 #CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO.
 #REALIZAR UNA HERENCIA DENTRO DEL MISMO ARCHIVO DE UNA DE LAS CLASES CREADAS, CREANDO UN METODO STR EN EL HIJO (IMPRMIR UN OBJETO CON ESA CLASE)
 #REALIZAR UNA HERENCIA ENTRE ARCHIVOS CREANDO UN METODO EN EL HIJO
 #REALIZAR UNA HERENCIA EN UNA CLASE QUE CONTENGA VARIOS OBJETOS (2) Y OBJETOS DENTRO DE OBJETOS (2)
 #REALIZAR UNA HERENCIA QUE CONTENGA: VARIOS OBJETOS (2), OBJETOS DENTRO DE OBEJTOS (2) Y OBJETOS DENTRO DE OBJETOS DENTRO DE OBJETOS (2)

from account import Account
from user import User
from admin import Admin
from producto import Producto
from producto_hombres import Hombre
from producto_mujeres import Mujeres
from producto_ninios import Ninios
from paymet import Payment
from paymet_card import PaymentCard
from venta import Venta

 
if __name__ == "__main__":
    print("Usuario")
    usuario1 = User(1755695096, "Enrique Ortiz", "Masculino", 984085110, 20, "kikeortiz925@gmail.com", "12345", 1)
print(vars(usuario1))

print("Admin")
admin1 = Admin(1755694567, "Julio Flores", "Masculino", 984085110, 20, "kikeortiz925@gmail.com", "12345", 1)
print(vars(admin1))

print("Producto")
producto1 = Producto("Camisa", "L", "Negro", 23, "hombre")
print(vars(producto1))

print("Payment")
pago1 = PaymentCard(1.1, 23, 12/12/2022, 22334556, "Pichincha", User(1755695096, "Enrique Ortiz", "Masculino", 984085110, 20, "kikeortiz925@gmail.com", "12345", 1), [1755694096, "12/23", "Enrique Ortiz", 234] )
print(vars(pago1))
print(vars(pago1.user))

print("Venta")
venta1 = Venta(1.1, User(1755695096, "Enrique Ortiz", "Masculino", 984085110, 20, "kikeortiz925@gmail.com", "12345", 1), Producto("Camisa", "L", "Negro", 23, "hombre"), PaymentCard(1.1, 23, 12/12/2022, 22334556, "Pichincha", User(1755695096, "Enrique Ortiz", "Masculino", 984085110, 20, "kikeortiz925@gmail.com", "12345", 1), [1755694096, "12/23", "Enrique Ortiz", 234]))
print(vars(venta1))
print(vars(venta1.user))
print(vars(venta1.producto))
print(vars(venta1.paymet))
