# Tuplas en Python

# Descripción de las Tuplas
# -------------------------
# En Python, una tupla es una colección ordenada e inmutable de elementos.
# A diferencia de las listas, las tuplas no pueden modificarse una vez que han sido creadas.
# Esto las convierte en una opción ideal cuando necesitas garantizar que los datos no cambien accidentalmente durante la ejecución del programa.
# Las tuplas pueden almacenar elementos de cualquier tipo, como números, cadenas, listas u otras tuplas.
# Son útiles para almacenar datos constantes, como coordenadas, fechas o configuraciones.

# Características de las Tuplas:
# ------------------------------
# - Inmutabilidad: Una vez creada, una tupla no puede modificarse. Esto significa que no puedes agregar, eliminar ni cambiar los elementos.
# - Ordenada: Los elementos de una tupla están en un orden específico y puedes acceder a ellos mediante índices.
# - Heterogénea: Las tuplas pueden contener diferentes tipos de datos, como enteros, cadenas, listas e incluso otras tuplas.



# Ejemplos de creación de tuplas:
# ------------------------------

# 1. Creando una tupla con paréntesis
tupla = ("Dato1", "Dato2")
print(tupla)  # Salida: ('Dato1', 'Dato2')

# 2. Creando una tupla sin paréntesis (tupla implícita)
tupla = "Dato1", "Dato2"
print(tupla)  # Salida: ('Dato1', 'Dato2')

# 3. Creando una tupla con un solo elemento
tupla = "Dato",  # Nota la coma al final para indicar que es una tupla
print(tupla)  # Salida: ('Dato',)

# 4. Creando una tupla a partir de una lista
lista = ["Dato1", "Dato2"]
tupla = tuple(lista)
print(tupla)  # Salida: ('Dato1', 'Dato2')



# Métodos de las Tuplas
# ---------------------
# Las tuplas son inmutables, por lo que sus métodos son limitados. Solo permiten consultar el contenido.

# 1. count(x) -> Devuelve el número de veces que el elemento x aparece en la tupla.
tupla = (1, 2, 3, 2, 4)
print(tupla.count(2))  # Salida: 2

# 2. index(x[, start[, end]]) -> Devuelve el índice de la primera aparición del elemento x.
print(tupla.index(2))  # Salida: 1



# Funciones estándar que puedes usar con tuplas:
# ------------------------------------------------
# Las tuplas, al ser colecciones inmutables, también pueden utilizar algunas funciones estándar de Python.

# 1. len(tupla) -> Devuelve el número de elementos en la tupla.
# 2. min(tupla) -> Devuelve el valor mínimo de la tupla (si contiene elementos comparables).
# 3. max(tupla) -> Devuelve el valor máximo de la tupla (si contiene elementos comparables).
# 4. sum(tupla) -> Devuelve la suma de los elementos de la tupla (si contiene números).

# Usando funciones estándar con tuplas
tupla = (1, 2, 3, 4, 5)
print(len(tupla))  # Salida: 5
print(min(tupla))  # Salida: 1
print(max(tupla))  # Salida: 5
print(sum(tupla))  # Salida: 15

