#Pensamiento computacional, sección 17
#07/11/2023
#Daniel Maldonado 1025323
#Objetivo: Crear una clase que se llame Automovil y se establezcan atributos con valores
#Entrada: La clase llamada Automivil y sus atributos a contener
#Procesos: Que el usuario llene la información que se le pide sobre el automovil 
#Salida: Marca, Modelo, Precio de venta, Precio en dólares y Disponibilidad

class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = False
        self.tipoCambioDolar = 0.0
        self.descuentoAplicado = 0.0

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInformacion(self):
        precio_en_dolares = self.precio / self.tipoCambioDolar
        disponibilidad = self.MostrarDisponibilidad()
        return (
            f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares ${precio_en_dolares}. {disponibilidad}"
        )

    def AplicarDescuento(self, porcentaje_descuento):
        if porcentaje_descuento >= 0 and porcentaje_descuento <= 100:
            self.descuentoAplicado = porcentaje_descuento
            descuento = (porcentaje_descuento / 100) * self.precio
            self.precio -= descuento

auto = Automovil()
auto.DefinirMarca(input("Ingresa la marca del automóvil: "))
auto.DefinirModelo(int(input("Ingresa el modelo del automóvil: ")))
auto.DefinirPrecio(float(input("Ingresa el precio del automóvil: ")))
auto.DefinirTipoCambio(float(input("Ingresa el tipo de cambio a dólares: ")))

print("El automóvil ha sido registrado con los siguientes datos:")
print(auto.MostrarInformacion())

auto.CambiarDisponibilidad()
print(f"Disponibilidad: {auto.MostrarDisponibilidad()}")

descuento = float(input("Ingresa el porcentaje de descuento (0 si no aplicar descuento): "))
if descuento > 0:
    auto.AplicarDescuento(descuento)
    print(f"Descuento del {descuento}% aplicado. Precio actualizado: Q{auto.precio}")

print("Información actualizada del automóvil:")
print(auto.MostrarInformacion())