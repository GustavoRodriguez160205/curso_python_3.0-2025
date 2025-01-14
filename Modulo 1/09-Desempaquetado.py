# Desempaquetado en Python: Una forma elegante de asignar valores

# El desempaquetado en Python es una técnica que permite asignar los elementos de una colección
# (como tuplas, listas, diccionarios o incluso strings) a variables individuales de una manera concisa y legible.
# Evita tener que acceder a los elementos por índice (ej: mi_lista[0], mi_tupla[1]) haciendo el código más limpio.

# 1. Desempaquetado de tuplas

print("\n--- 1. Desempaquetado de tuplas ---\n")

tupla = ("Lucas", "Dalto", 1000000)

# Desempaquetado: Se asigna cada elemento de la tupla a una variable en el mismo orden.
nombre, apellido, suscriptores = tupla

print(f"Nombre: {nombre}")       # Salida: Nombre: Lucas
print(f"Apellido: {apellido}")    # Salida: Apellido: Dalto
print(f"Suscriptores: {suscriptores}") # Salida: Suscriptores: 1000000

# IMPORTANTE: El número de variables a la izquierda del "=" debe coincidir con el número de elementos de la tupla.
# Si no coinciden, se produce un ValueError.

# Ejemplo de error (descomentar para ver el error):
# nombre, apellido = tupla # Error: ValueError: too many values to unpack (expected 2)

# 2. Desempaquetado de listas

print("\n--- 2. Desempaquetado de listas ---\n")

lista = ["Lucas", "Dalto", 1000000]

# El desempaquetado de listas funciona de forma idéntica al de las tuplas.
nombre, apellido, suscriptores = lista

print(f"Nombre: {nombre}")       # Salida: Nombre: Lucas
print(f"Apellido: {apellido}")    # Salida: Apellido: Dalto
print(f"Suscriptores: {suscriptores}") # Salida: Suscriptores: 1000000


# 3. Desempaquetado con un número variable de elementos (usando *)

print("\n--- 3. Desempaquetado con * ---\n")

datos = ["Lucas", "Dalto", 1000000, "Argentina", "YouTube", "Programación"]

# El operador * permite capturar un número variable de elementos en una lista.
nombre, apellido, suscriptores, *otros_datos = datos

print(f"Nombre: {nombre}")           # Salida: Nombre: Lucas
print(f"Apellido: {apellido}")        # Salida: Apellido: Dalto
print(f"Suscriptores: {suscriptores}")   # Salida: Suscriptores: 1000000
print(f"Otros datos: {otros_datos}")    # Salida: Otros datos: ['Argentina', 'YouTube', 'Programación']

# El * también puede usarse en otras posiciones:

nombre, *datos_intermedios, canal = datos
print(f"\nNombre: {nombre}")            # Salida: Nombre: Lucas
print(f"Datos intermedios: {datos_intermedios}") # Salida: Datos intermedios: ['Dalto', 1000000, 'Argentina', 'YouTube']
print(f"Canal: {canal}")               # Salida: Canal: Programación


# 4. Desempaquetado de diccionarios

print("\n--- 4. Desempaquetado de diccionarios ---\n")

diccionario = {
    "nombre": "Lucas", 
    "apellido": "Dalto", 
    "suscriptores": 1000000
}

# a) Desempaquetado de claves:
claves = diccionario.keys()
print(f"Claves del diccionario: {claves}") #Salida: Claves del diccionario: dict_keys(['nombre', 'apellido', 'suscriptores'])
nombre, apellido, suscriptores = diccionario #Por defecto itera las claves
print(f"Claves desempaquetadas: {nombre}, {apellido}, {suscriptores}") #Salida: Claves desempaquetadas: nombre, apellido, suscriptores

# b) Desempaquetado de valores:
valores = diccionario.values()
print(f"Valores del diccionario: {valores}") #Salida: Valores del diccionario: dict_values(['Lucas', 'Dalto', 1000000])
nombre, apellido, suscriptores = diccionario.values()
print(f"Valores desempaquetados: {nombre}, {apellido}, {suscriptores}") #Salida: Valores desempaquetados: Lucas, Dalto, 1000000


# c) Desempaquetado de items (clave-valor):
print("\nDesempaquetado de items (clave-valor):\n")
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
#Salida:
#nombre: Lucas
#apellido: Dalto
#suscriptores: 1000000

#Una forma mas concisa usando desempaquetado dentro del bucle
for item in diccionario.items():
    clave, valor = item #Desempaquetado dentro del bucle
    print(f"{clave}: {valor}")
#Salida:
#nombre: Lucas
#apellido: Dalto
#suscriptores: 1000000

#Incluso mas concisa
for clave, valor in diccionario.items(): #Desempaquetado directo en el for
    print(f"{clave}: {valor}")
#Salida:
#nombre: Lucas
#apellido: Dalto
#suscriptores: 1000000

# 5. Desempaquetado de strings

print("\n--- 5. Desempaquetado de strings ---\n")

cadena = "Hola"
h, o, l, a = cadena
print(f"Desempaquetado de la cadena: {h}, {o}, {l}, {a}") #Salida: Desempaquetado de la cadena: H, o, l, a
