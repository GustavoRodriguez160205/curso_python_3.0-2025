# Variables en Python

# Una variable es un nombre que se refiere a una ubicación en la memoria donde se almacenan datos.
# Python infiere el tipo de dato según el valor asignado.

# Declaración y Asignación
nombre = "Juan"         # Cadena (str)
edad = 30              # Entero (int)
altura = 1.75          # Flotante (float)
es_estudiante = True    # Booleano (bool)
frutas = ["manzana", "banana"] # Lista (list)
coordenadas = (10, 20)      # Tupla (tuple)
persona = {"nombre": "Ana", "edad": 25} # Diccionario (dict)
numeros = {1,2,3,4} # Conjunto (set)
complejo = 2 + 3j # Complejo (complex)


# Tipos de Datos en Python
# - Números: int, float, complex
# - Cadenas: str
# - Booleanos: bool (True, False)
# - Listas: list (mutables, ordenadas)
# - Tuplas: tuple (inmutables, ordenadas)
# - Diccionarios: dict (pares clave-valor)
# - Conjuntos: set (elementos únicos, no ordenados)

# Mostrar el tipo de una variable
print(type(nombre))       # <class 'str'>
print(type(edad))         # <class 'int'>
print(type(altura))       # <class 'float'>
print(type(es_estudiante)) # <class 'bool'>
print(type(frutas))       # <class 'list'>
print(type(coordenadas))   # <class 'tuple'>
print(type(persona))     # <class 'dict'>
print(type(numeros))     # <class 'set'>
print(type(complejo))     # <class 'complex'>

# Conversión de Tipos (Casting)
numero_str = "123"
numero_int = int(numero_str)  # str a int
numero_float = float(numero_str) # str a float
numero_bool = bool(numero_int) # (int a bool 0 es False, cualquier otro número es True)
texto_de_numero = str(numero_int) # int a str
print(type(numero_int)) # <class 'int'>
print(type(numero_float)) # <class 'float'>
print(type(numero_bool)) # <class 'bool'>
print(type(texto_de_numero)) # <class 'str'>

# Operadores de Asignación Compuesta
x = 10
x += 5  # x = x + 5 (x ahora es 15)
x -= 3  # x = x - 3 (x ahora es 12)
x *= 2  # x = x * 2 (x ahora es 24)
x /= 4  # x = x / 4 (x ahora es 6.0)
x %= 3  # x = x % 3 (x ahora es 0.0)
x //= 2 # x = x // 2 (x ahora es 0.0)
x **= 2 # x = x ** 2 (x ahora es 0.0)
print(x)

# Concatenación (con f-strings)
nombre = "Elena"
edad = 28
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)

# Eliminación de Variables
y = 20
del y
# print(y) # Genera NameError: name 'y' is not defined

# Operadores de Pertenencia (en cadenas)
texto = "Python es poderoso"
print("Python" in texto)    # True
print("java" in texto)      # False
print("java" not in texto)  # True

# Convenciones de Nombres
nombre_de_variable = "Snake Case"
# nombreDeVariable = "Camel Case" (menos común en Python)

#Ejemplo de uso de in con listas
mi_lista = [1, 2, 3, 4, 5]
print(3 in mi_lista) # True
print(7 in mi_lista) # False