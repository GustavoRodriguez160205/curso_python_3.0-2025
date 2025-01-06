"""
Guía completa de Diccionarios en Python

Un diccionario en Python es una estructura de datos que almacena pares clave-valor.
Son mutables, lo que significa que se pueden modificar después de su creación.
A partir de Python 3.7, los diccionarios mantienen el orden de inserción.

Características principales:

*   **Claves únicas:** Cada clave en un diccionario debe ser única.
*   **Mutables:** Se pueden agregar, modificar y eliminar elementos.
*   **Indexados por clave:** Se accede a los valores mediante sus claves, no por índice.
*   **Diversidad de tipos:** Las claves pueden ser de tipos inmutables (ej., cadenas, números, tuplas),
    y los valores pueden ser de cualquier tipo (incluyendo otros diccionarios, listas, etc.).

"""

# Creación de diccionarios

# 1. Usando llaves {}
diccionario1 = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print("Diccionario 1:", diccionario1)

# 2. Usando la función dict()
diccionario2 = dict(nombre="Ana", edad=25, ciudad="Barcelona")
print("Diccionario 2:", diccionario2)

# 3. A partir de una lista de tuplas
pares = [("a", 1), ("b", 2), ("c", 3)]
diccionario3 = dict(pares)
print("Diccionario 3:", diccionario3)

# 4. Diccionario vacío
diccionario_vacio = {}
print("Diccionario vacío:", diccionario_vacio)

# Acceso a los elementos

nombre = diccionario1["nombre"]  # Acceder al valor asociado a la clave "nombre"
print("Nombre:", nombre)

# Si la clave no existe, se produce un KeyError. Para evitarlo:

# 1. Usando el método get()
edad = diccionario1.get("edad")  # Si la clave no existe, devuelve None
print("Edad:", edad)
pais = diccionario1.get("pais", "Desconocido") # Si la clave no existe, devuelve "Desconocido"
print("País:", pais)

#####################################
#####################################
#####################################

# Modificación de diccionarios


diccionario1["edad"] = 31  # Modificar el valor asociado a la clave "edad"
print("Diccionario 1 modificado:", diccionario1)

diccionario1["profesion"] = "Ingeniero"  # Agregar un nuevo par clave-valor
print("Diccionario 1 con nueva clave:", diccionario1)

#######################################
#######################################
#######################################


# Eliminación de elementos

del diccionario1["ciudad"]  # Eliminar el par clave-valor con la clave "ciudad"
print("Diccionario 1 sin ciudad:", diccionario1)

valor_eliminado = diccionario1.pop("profesion")  # Elimina y retorna el valor de la clave "profesion"
print("Valor eliminado:", valor_eliminado)
print("Diccionario 1 sin profesion:", diccionario1)

##########################################
##########################################
##########################################

# Métodos útiles de los diccionarios

# keys(): Retorna una vista de las claves
claves = diccionario1.keys()
print("Claves:", claves)
print(list(claves)) #convertir a lista para acceder por índice

# values(): Retorna una vista de los valores
valores = diccionario1.values()
print("Valores:", valores)
print(list(valores)) #convertir a lista para acceder por índice

# items(): Retorna una vista de los pares clave-valor (como tuplas)
items = diccionario1.items()
print("Items:", items)
print(list(items)) #convertir a lista para acceder por índice

# len(): Retorna la cantidad de elementos en el diccionario
longitud = len(diccionario1)
print("Longitud:", longitud)

# in: Verifica si una clave existe en el diccionario
existe_nombre = "nombre" in diccionario1
print("¿Existe la clave 'nombre'?:", existe_nombre)

existe_ciudad= "ciudad" in diccionario1
print("¿Existe la clave 'ciudad'?:", existe_ciudad)

# copy(): Crea una copia superficial del diccionario
diccionario_copia = diccionario1.copy()
print("Diccionario copia:", diccionario_copia)

# update(): Actualiza el diccionario con los elementos de otro diccionario o iterable de pares clave-valor
diccionario1.update({"ciudad": "Valencia", "pais": "España"})
print("Diccionario 1 actualizado:", diccionario1)

diccionario1.update([("codigo_postal", 46000)]) #Actualiza con una lista de tuplas
print("Diccionario 1 actualizado con lista de tuplas:", diccionario1)



# Iteración sobre diccionarios

# Iterar sobre las claves
print("\nIterando sobre claves:")
for clave in diccionario1:  # Equivalente a: for clave in diccionario1.keys():
    print(clave, ":", diccionario1[clave])

# Iterar sobre los valores
print("\nIterando sobre valores:")
for valor in diccionario1.values():
    print(valor)

# Iterar sobre los items (pares clave-valor)
print("\nIterando sobre items:")
for clave, valor in diccionario1.items():
    print(f"Clave: {clave}, Valor: {valor}")

# Comprensión de diccionarios (Dict Comprehension)

# Crear un diccionario elevando al cuadrado los números del 1 al 5
cuadrados = {x: x**2 for x in range(1, 6)}
print("\nDiccionario de cuadrados:", cuadrados)

# Crear un diccionario invirtiendo clave y valor de otro diccionario
diccionario_invertido = {valor: clave for clave, valor in diccionario1.items()}
print("\nDiccionario invertido:", diccionario_invertido)

print("\nFin de la guía de diccionarios.")