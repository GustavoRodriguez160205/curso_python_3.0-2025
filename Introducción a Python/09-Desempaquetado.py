# Descripción:
# En Python, el desempaquetado permite asignar elementos de colecciones como tuplas, listas o diccionarios a variables de forma sencilla. 
# Es una técnica útil para acceder a los valores de manera más legible y directa sin tener que utilizar índices. 
# A continuación, se presentan ejemplos de cómo desempaquetar tuplas, listas y diccionarios en Python.

# 1. Desempaquetado en tupla
tupla = ("Lucas", "Dalto", 1000000)

# Desempaquetado de la tupla
nombre, apellido, suscriptores = tupla

# Mostrando resultados
print("Desempaquetado de tupla:")
print(f"Nombre: {nombre}")       # Lucas
print(f"Apellido: {apellido}")   # Dalto
print(f"Suscriptores: {suscriptores}") # 1000000
print()


####################
####################
####################



# 2. Desempaquetado en lista
lista = ["Lucas", "Dalto", 1000000]

# Desempaquetado de la lista
nombre, apellido, suscriptores = lista


print("Desempaquetado de lista:")
print(f"Nombre: {nombre}")       # Lucas
print(f"Apellido: {apellido}")   # Dalto
print(f"Suscriptores: {suscriptores}") # 1000000
print()


####################
####################
####################

# 3. Desempaquetado con un número variable de elementos (usando *)
datos = ["Lucas", "Dalto", 1000000, "Argentina", "YouTube"]

# Desempaquetado, capturando el resto con '*'
nombre, apellido, suscriptores, *otros_datos = datos

# Mostrando resultados
print("Desempaquetado con un número variable de elementos:")
print(f"Nombre: {nombre}")           # Lucas
print(f"Apellido: {apellido}")       # Dalto
print(f"Suscriptores: {suscriptores}") # 1000000
print(f"Otros datos: {otros_datos}")  # ['Argentina', 'YouTube']
print()



####################
####################
####################




# 4. Desempaquetado en diccionarios (claves y valores)
diccionario = {"nombre": "Lucas", "apellido": "Dalto", "suscriptores": 1000000}

# Desempaquetado de claves y valores
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
