"""
Diccionarios en Python: Guía completa desde cero

Los diccionarios son estructuras de datos que almacenan pares clave: valor.
"""

# 1. Creación de diccionarios:

# a. Usando llaves {}:
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}
print("Diccionario creado con {}:", persona)


# b. Usando la función dict():
persona2 = dict(nombre="Pedro", edad=25, ciudad="Barcelona")  # Con argumentos nombrados
print("Diccionario creado con dict() (argumentos):", persona2)

persona3 = dict([("nombre", "Luis"), ("edad", 40), ("ciudad", "Valencia")])  # Con lista de tuplas
print("Diccionario creado con dict() (lista de tuplas):", persona3)


########################################################################


# 2. Acceso a los valores:

nombre = persona["nombre"]
print("\nAccediendo al nombre:", nombre)

# Usando .get() para evitar KeyError:
profesion = persona.get("profesion")  # Devuelve None si la clave no existe
print("Profesión (con .get()):", profesion)

profesion = persona.get("profesion", "Desconocida")  # Devuelve "Desconocida" si la clave no existe
print("Profesión (con .get() y valor por defecto):", profesion)


########################################################################


# 3. Modificación y adición de elementos:

persona["edad"] = 31  # Modificando la edad
print("\nDiccionario con edad modificada:", persona)

persona["profesion"] = "Ingeniera"  # Añadiendo una nueva clave: valor
print("Diccionario con nueva profesión:", persona)


########################################################################

# 4. Eliminación de elementos:

del persona["ciudad"]  # Eliminando la clave "ciudad"
print("\nDiccionario sin ciudad:", persona)

valor_eliminado = persona.pop("edad") #Eliminando la clave "edad" y guardando el valor eliminado en una variable
print("Valor eliminado con .pop():", valor_eliminado)
print("Diccionario despues de usar .pop():", persona)

###########################################################################

# 5. Comprobación de existencia de claves:

print("\n--- Comprobando la existencia de claves ---")

if "nombre" in persona:
    print("'nombre' existe en el diccionario.")

if "ciudad" not in persona:
    print("'ciudad' NO existe en el diccionario.")


############################################################################
# 7. Métodos útiles:

print("\n--- Métodos útiles ---")

print("Número de elementos:", len(persona))  # Cantidad de pares clave: valor
print("Claves del diccionario:", persona.keys())  # Devuelve una vista de las claves
print("Valores del diccionario:", persona.values())  # Devuelve una vista de los valores
print("Pares clave-valor:", persona.items())  # Devuelve una vista de tuplas (clave, valor)

persona_copia = persona.copy() #Crea una copia independiente del diccionario
persona_copia["nueva_clave"] = "Nuevo valor"
print("Diccionario original:", persona)
print("Copia del diccionario:", persona_copia)

persona.clear()  # Elimina todos los elementos del diccionario
print("Diccionario vacío:", persona)