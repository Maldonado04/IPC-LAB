#Laboratorio de pensamiento computacional, seccion 17
#12/09/2023
#Daniel Maldonado
#Objetivo: Nombrar y decir que dia es
#Entrada: Numero indicador de dias
#procesos: "Determinar los dias en numero y si no estra dentro del margen marcar error"
#Salida: El dia de hoy es:

print("Ejercicio 2")

d1= int(input("Ingrese numero de 1 a 7 de acuerdo al dia"))



if d1== 1:
    print("Hoy es lunes")

elif d1== 2:
    print("Hoy es martes")

elif d1== 3:
    print("Hoy es miercoles")

elif d1== 4: 
    print("Hoy es jueves")

elif d1== 5:
    print("Hoy es viernes")

elif d1== 6:
    print("Hoy es sabado")

elif d1== 7:
    print("Hoy es domingo")

else: 
    print("ERROR: ingrese numero entre 1-7")