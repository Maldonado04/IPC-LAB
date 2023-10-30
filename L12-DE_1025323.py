#Pensamiento Computacional, sección 17
#28/10/2023
#Daniel Maldonado 1025323
#Objetivo: Crear una lista de contacto
#Entrada: Declarar variable y solicitar al usuario la cantidad de contactos
#Proceso: Agregar contactos y mostrarlos en una lista, eliminar y agregarlos, ordenarlos en orden alfabético
#Salidad: Mostrar la lista original, actualizada o con los cambios respectivos

# 1. Declarar una variable tipo lista.
contactos = []

# 2. Solicitar al usuario la cantidad de contactos a ingresar.
n = int(input("Ingrese la cantidad de contactos que va a ingresar: "))

# 3. Agregar "n" contactos a la lista.
for _ in range(n):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono del contacto: ")
    contactos.append([nombre, numero])

# 4. Mostrar la lista de contactos completa.
print("Lista de contactos completa:")
for contacto in contactos:
    print(contacto)

# 5. Eliminar un contacto existente por nombre.
nombre_eliminar = input("Ingrese el nombre del contacto que desea eliminar: ")
for contacto in contactos:
    if contacto[0] == nombre_eliminar:
        contactos.remove(contacto)

# 6. Mostrar la lista de contactos actualizada.
print("Lista de contactos actualizada:")
for contacto in contactos:
    print(contacto)

# 7. Ordenar la lista alfabéticamente por nombre.
contactos.sort(key=lambda x: x[0])

# 8. Mostrar la lista ordenada.
print("Lista de contactos ordenada alfabéticamente:")
for contacto in contactos:
    print(contacto)

# 9. Ingresar un nuevo contacto con el nombre en mayúsculas.
nombre_mayusculas = input("Ingrese el nombre del nuevo contacto en mayúsculas: ")
numero_nuevo = input("Ingrese el número de teléfono del nuevo contacto: ")
contactos.append([nombre_mayusculas, numero_nuevo])

# 10. Ingresar un nuevo contacto en una posición específica.
posicion = int(input("Ingrese la posición donde desea agregar el nuevo contacto: "))
nombre_nuevo = input("Ingrese el nombre del nuevo contacto: ")
numero_nuevo = input("Ingrese el número de teléfono del nuevo contacto: ")
contacto_nuevo = [nombre_nuevo, numero_nuevo]
contactos.insert(posicion, contacto_nuevo)

# 11. Mostrar la lista de contactos completa.
print("Lista de contactos completa después de las modificaciones:")
for contacto in contactos:
    print(contacto)

# 12. Crear una copia de la lista de contactos y ordenarla alfabéticamente de forma descendente.
copia_contactos = contactos.copy()
copia_contactos.sort(key=lambda x: x[0], reverse=True)

# 13. Mostrar la lista ordenada de forma descendente y la lista original.
print("Lista de contactos ordenada de forma descendente:")
for contacto in copia_contactos:
    print(contacto)

print("Lista de contactos original:")
for contacto in contactos:
    print(contacto)