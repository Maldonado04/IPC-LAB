#Laboratorio de pensamiento computacional, seccion 17
#12/09/2023
#Daniel Maldonado
#Objetivo: Comparar numeros y marcar error si no es numero
#Entrada: Numero entero
#Procesos: "Determinacion de numero postivo o negativo y marcar error si es menor que cero o mayor que siete"
#Salida: Resultado

print("Ejercicio 1")
n1= int(input("Ingrese numero entero"))


if n1>0:
    print(n1, "es positivo")
if n1<0:
    print(n1, "es negativo")
if n1==0:
    print(n1, "es cero")