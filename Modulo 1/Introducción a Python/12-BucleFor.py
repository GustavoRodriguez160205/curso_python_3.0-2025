# Ejemplos de Iteración en Python

# 1. Iterando una lista directamente (forma más común y eficiente)
animales = ["Perro", "Loro", "Cocodrilo", "Serpiente"]
print("\n1. Iteración directa de la lista animales:")
for animal in animales:
    print(f"Ahora la variable animal es: {animal}")

#########################################################
#########################################################
#########################################################

# 2. Iterando y modificando elementos (creando una nueva lista)
numeros = [20, 52, 12, 72]
print("\n2. Iterando y multiplicando números (creando una nueva lista):")
resultados = [numero * 10 for numero in numeros]  # Usando comprensión de listas
print(f"Los resultados son: {resultados}")

#########################################################
#########################################################
#########################################################

# 3. Iterando dos listas simultáneamente con zip
print("\n3. Iterando dos listas con zip:")

animales = ["Perro", "Loro", "Cocodrilo", "Serpiente"]
numeros = [20, 52, 12, 72]
for animal, numero in zip(animales, numeros):
    print(f"{animal} tiene el número asociado: {numero}")

# zip con listas de diferente longitud:

nombres = ["Ana", "Juan", "Pedro"]
edades = [25, 30]
print("\nzip con listas de diferente longitud (se detiene en la más corta):")
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")

#########################################################
#########################################################
#########################################################

# 4. Iterando con range (para generar secuencias numéricas)

print("\n4. Iterando con range:")

for num in range(10):  # Por defecto comienza en 0
    print(f"Número: {num}")

print("\nrange con inicio y fin:")

for num in range(1, 11):  # Desde 1 hasta 10 (el 11 no se incluye)
    print(f"Número: {num}")

print("\nrange con inicio, fin y paso:")

for num in range(0, 21, 2):  # Desde 0 hasta 20, con pasos de 2
    print(f"Número par: {num}")

#########################################################
#########################################################
#########################################################

# 5. Usando else en un bucle for (se ejecuta si el bucle termina normalmente, NO si se interrumpe con break)
print("\n5. Usando else en for:")

for numero in numeros:
    print(f"Valor actual: {numero}")
else:
    print("El bucle ha terminado normalmente.")

# 5.1 Ejemplo con break (el else NO se ejecuta)
print("\nEjemplo con break (el else NO se ejecuta):")

for numero in numeros:
    if numero == 12:
        break  # Se interrumpe el bucle
    print(f"Valor actual: {numero}")
else:
    print("Este mensaje NO se imprimirá porque se usó break.")

#########################################################
#########################################################
#########################################################

# 6. Iterando con índice usando enumerate (forma idiomática y recomendada)
print("\n6. Iterando con índice usando enumerate:")

for indice, valor in enumerate(numeros):
    print(f"Índice: {indice}, Valor: {valor}")

#########################################################
#########################################################
#########################################################

# 7. Iterando con índice usando range y len (menos idiomático y menos eficiente)
print("\n7. Iterando con índice usando range y len (menos recomendado):")

for indice in range(len(numeros)):
    print(f"Índice: {indice}, Valor: {numeros[indice]}")

#########################################################
#########################################################
#########################################################

# #########################################
# Más ejemplos de control de flujo en bucles

# Evitando que se coma una pera con la sentencia continue

frutas = ["Banana", "Pera", "Manzana", "Uva", "Ciruela"]
print("\nEvitar comer una pera con continue:")
for fruta in frutas:
    if fruta == "Pera":
        continue  # Saltea la iteración
    print(f"Me voy a comer una: {fruta}")

# Evitar que el bucle siga ejecutándose. (El else no se ejecuta)

print("\nEvitar seguir el bucle con break:")

for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")
    if fruta == "Pera":
        break  # Termina el bucle
else:
    print("Terminado")

# Recorriendo una cadena de texto

print("\nIterando una cadena de texto:")

cadena = "hola"
for letra in cadena:
    print(letra)

# #########################################
# Iterando un diccionario

productos = {'manzana': 2, 'banana': 3, 'cereza': 5}

# Iterar sobre las claves

print("\nIterando sobre las claves:")
for clave in productos.keys():
    print(clave)

# Iterar sobre los valores

print("\nIterando sobre los valores:")
for valor in productos.values():
    print(valor)

# Iterar sobre claves y valores

print("\nIterando sobre las claves y los valores:")
for clave, valor in productos.items():
    print(f"Clave: {clave}, Valor: {valor}")

################################
################################
################################

# For en una sola linea de código

print("\nFor en una sola línea de código:")
numeros_dupli = [x * 2 for x in numeros]  # Usando comprensión de listas
print(f"Los números duplicados serán: {numeros_dupli}")
