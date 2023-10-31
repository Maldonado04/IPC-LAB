#Pensamiento computacional, sección 17
#31/10/2023
#Daniel Maldonado 1025323
#Objetivo: Desarrollar una clase con diferentes datos personales de un usuario
#Entrada: Ingresar los datos para la clase
#Procesos: Que el usuario inserte los datos que desee
#Salida: El nombre completo con el apellido del usuario y su edad

from datetime import datetime

class Persona:
    def __init__(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellido_casada = ""
        self.fecha_nacimiento = None

    def insertar_nombres(self, nombres):
        self.nombres = nombres

    def insertar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def insertar_apellido_casada(self, apellido_casada):
        self.apellido_casada = apellido_casada

    def insertar_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        if self.apellido_casada:
            return f"{self.apellidos} de casada {self.apellido_casada}"
        else:
            return self.apellidos

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def obtener_nombre_completo(self):
        return f"{self.nombres} {self.obtener_apellidos()}"

    def obtener_edad(self):
        if self.fecha_nacimiento:
            hoy = datetime.now()
            edad = hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
            return edad
        else:
            return None

persona = Persona()
persona.insertar_nombres(input("Ingresa tu nombre: "))
persona.insertar_apellidos(input("Ingresa tus apellidos: "))
casada = input("¿Tienes apellido de casada? (S/N): ").upper()
if casada == "S":
    persona.insertar_apellido_casada(input("Ingresa tu apellido de casada: "))
dia, mes, anio = map(int, input("Ingresa tu fecha de nacimiento (DD MM AAAA): ").split())
persona.insertar_fecha_nacimiento(datetime(anio, mes, dia))

print("Nombre completo:", persona.obtener_nombre_completo())
print("Edad:", persona.obtener_edad(), "años")