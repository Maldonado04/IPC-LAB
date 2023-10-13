#Laboratorio de pensamiento computacional, seccion 17
#10/10/2023
#Daniel Maldonado
#Objetivo: Crear funciones necesarias para convertir una cantidad en cm a otras unidades de medida
#Entrada: Crear un modulo principal de la cantidad en cm a conversiones
#Proceso: Conversiones de las diferentes unidades de medida
#Salida: Unidades de medida

def centimetrosAmetros(cantidad):
    metros=cantidad/100
    return metros

def centimetrosAkilometros(cantidad):
    kilometros=cantidad/100000
    return kilometros

def centimetrosApulgadas(cantidad):
    pulgadas=cantidad/2.54
    return pulgadas

def centimetrosApies(cantidad):
    pies=cantidad/30.48
    return pies