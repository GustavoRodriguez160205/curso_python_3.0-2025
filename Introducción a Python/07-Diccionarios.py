## Diccionarios en Python

# Los diccionarios en Python son estructuras de datos clave-valor, donde cada valor está asociado a una clave única e inmutable (como cadenas, números o tuplas). Son mutables, lo que significa que se pueden modificar, agregar o eliminar elementos.

# Características Clave:
# - Pares Clave-Valor: Un diccionario se compone de elementos en los que cada clave única se asocia a un valor.
# - Indexación por Clave: A diferencia de las listas, se accede a los valores a través de sus claves en lugar de índices numéricos.
# - Mutabilidad: Los diccionarios pueden modificarse (añadir, eliminar o cambiar elementos).
# - Ordenación: Desde Python 3.7+, los diccionarios mantienen el orden de inserción de los elementos. En versiones anteriores, el orden no estaba garantizado.


#########################

## Creación de Diccionarios

# 1. Usando llaves {}
info = {
    "Nombre": "Ana",
    "Edad": 25,
    "Ciudad": "Barcelona"
}

print("Diccionario 'info':", info)

# 2. Usando dict()
mi_diccionario = dict(nombre="Marcos", edad=15, ciudad="Madrid")
mi_diccionario = dict([("nombre", "Leonel"), ("edad", 18), ("ciudad", "Colombia")])  # Lista de tuplas

print("Diccionario 'mi_diccionario':", mi_diccionario)



#########################


## Acceso a Elementos

# 1. Con corchetes []
nombre = info["Ciudad"]  # Devuelve el valor asociado a la clave "Ciudad"
print("Acceso con corchetes: 'Ciudad' =", nombre)

# 2. Usando el método get()
ciudad = mi_diccionario.get("ciudad")  # Devuelve "None" si no existe la clave
profesion = mi_diccionario.get("profesion", "Desconocida")  # Devuelve "Desconocida" si no existe la clave
print("Acceso con get() - Ciudad:", ciudad)
print("Acceso con get() - Profesión:", profesion)



#########################

## Modificación de Diccionarios

# Añadir un nuevo par
mi_diccionario["profesion"] = "Programadora"
print("Diccionario después de añadir 'profesion':", mi_diccionario)

# Modificar un valor
mi_diccionario["edad"] = 26
print("Diccionario después de modificar 'edad':", mi_diccionario)


#########################


## Eliminación de Elementos

# 1. Usando del
del mi_diccionario["ciudad"]  # Elimina la clave "ciudad" y su valor
print("Diccionario después de eliminar 'ciudad':", mi_diccionario)

# 2. Usando pop
edad = mi_diccionario.pop("edad")  # Elimina la clave "edad" y devuelve su valor (26)
ciudad = mi_diccionario.pop("ciudad", "No existe")  # Si no existe la clave, devuelve el valor por defecto
print("Valor de 'edad' después de pop:", edad)
print("Valor de 'ciudad' después de pop (no existe):", ciudad)
print("Diccionario después de eliminar 'edad' y 'ciudad':", mi_diccionario)


#########################


## Métodos Útiles

# 1. keys(): Devuelve una vista de las claves
claves = mi_diccionario.keys()  # Retorna un objeto tipo dict_keys
lista_claves = list(mi_diccionario.keys())  # Obtener una lista de las claves
print("Claves del diccionario:", claves)
print("Lista de claves:", lista_claves)

# 2. values(): Devuelve una vista de los valores
valores = mi_diccionario.values()  # Retorna un objeto tipo dict_values
lista_valores = list(mi_diccionario.values())  # Obtener una lista de los valores
print("Valores del diccionario:", valores)
print("Lista de valores:", lista_valores)

# 3. items(): Devuelve una vista de los pares clave-valor (tuplas)
items = mi_diccionario.items()  # Retorna un objeto tipo dict_items
lista_items = list(mi_diccionario.items())  # Obtener una lista de tuplas (clave, valor)
print("Pares clave-valor del diccionario:", items)
print("Lista de pares clave-valor:", lista_items)

