# Definición de listas en Python:
# Las listas en Python son estructuras de datos ordenadas, mutables, heterogéneas y dinámicas.
# - **Ordenadas:** Los elementos tienen un orden específico que se mantiene.
# - **Mutables:** Se pueden modificar después de su creación (añadir, eliminar, cambiar elementos).
# - **Heterogéneas:** Pueden contener elementos de diferentes tipos de datos.
# - **Dinámicas:** Su tamaño puede crecer o disminuir.
# - **Indexadas:** Se accede a sus elementos mediante índices numéricos (empezando desde 0).

# 1. Creación de listas:
# - Las listas pueden ser creadas usando corchetes [] o la función list().
# - Pueden contener diferentes tipos de datos: números, cadenas, booleanos, etc.

# a. Usando corchetes []:
mi_lista = [1, 2, 3, "hola", 3.14, True]  # Listas pueden contener diferentes tipos de datos
print("Lista creada con []:", mi_lista)

# b. Usando la función list():
otra_lista = list((4, 5, 6))  # Convirtiendo una tupla a lista
print("Lista creada con list():", otra_lista)

# c. Convertir una cadena en una lista de caracteres:
cadena = "Python"
lista_desde_cadena = list(cadena)  # Convierte una cadena en una lista de caracteres
print("Lista creada desde una cadena:", lista_desde_cadena)

# d. Lista vacía:
lista_vacia = []  # Lista vacía
print("Lista vacía:", lista_vacia)


# 2. Acceso a los elementos:
# - Las listas permiten acceder a sus elementos mediante índices.
# - El primer elemento está en el índice 0, y se pueden usar índices negativos para acceder desde el final.

print("\n--- Acceso a elementos ---")
print("Primer elemento:", mi_lista[0])  # Índices comienzan desde 0
print("Último elemento:", mi_lista[-1])  # Índice negativo para acceder desde el final
print("Sublista (slicing):", mi_lista[1:4])  # Desde el índice 1 hasta el 3 (no inclusive)
print("Sublista desde el inicio:", mi_lista[:3])  # Desde el inicio hasta el índice 2
print("Sublista hasta el final:", mi_lista[2:])  # Desde el índice 2 hasta el final
print("Sublista con paso:", mi_lista[::2])  # Desde el inicio hasta el final con paso 2
print("Sublista con paso negativo:", mi_lista[::-1])  # Invierte la lista


# 3. Modificación de listas:
# - Las listas son mutables, por lo que se pueden modificar: agregar, eliminar, o cambiar elementos.

print("\n--- Modificación de listas ---")
mi_lista[0] = 10  # Modificando un elemento
print("Lista con elemento modificado:", mi_lista)

mi_lista.append("nuevo elemento")  # Añadiendo un elemento al final
print("Lista con append():", mi_lista)

mi_lista.insert(2, "elemento insertado")  # Insertando un elemento en una posición específica
print("Lista con insert():", mi_lista)

otra_lista.extend([7, 8, 9])  # Añadiendo múltiples elementos al final
print("Lista con extend():", otra_lista)


# 4. Eliminación de elementos:
# - Los elementos de una lista pueden ser eliminados de varias maneras: por índice, por valor, o limpiando la lista.

print("\n--- Eliminación de elementos ---")
del mi_lista[3]  # Eliminando un elemento por índice
print("Lista con del:", mi_lista)

elemento_eliminado = mi_lista.pop(1)  # Eliminando un elemento por índice y obteniendo su valor
print("Elemento eliminado con pop():", elemento_eliminado)
print("Lista después de pop():", mi_lista)

mi_lista.remove(3.14)  # Eliminando un elemento por valor (solo la primera ocurrencia)
print("Lista con remove():", mi_lista)

mi_lista.clear()  # Elimina todos los elementos de la lista
print("Lista con clear():", mi_lista)

mi_lista = [1, 2, 3, 4, 5]  # Recreamos la lista para los siguientes ejemplos


# 5. Operaciones con listas:
# - Las listas permiten realizar varias operaciones, como concatenación, repetición, y cálculos básicos como suma, longitud, máximo y mínimo.

print("\n--- Operaciones con listas ---")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenación de listas:
lista_concatenada = lista1 + lista2  
print("Listas concatenadas:", lista_concatenada)

# Repetición de listas:
lista_repetida = lista1 * 3  
print("Lista repetida:", lista_repetida)

# Cálculos básicos:
print("Longitud de la lista:", len(lista1))  # Longitud
print("Máximo de la lista:", max(lista1))  # Máximo (solo para tipos comparables)
print("Mínimo de la lista:", min(lista1))  # Mínimo (solo para tipos comparables)
print("Suma de la lista:", sum(lista1))  # Suma (solo para tipos numéricos)


# 6. Búsqueda en listas:
# - Podemos verificar si un elemento está en la lista, buscar su índice o contar las veces que aparece.

print("\n--- Búsqueda en listas ---")
if 2 in lista1:
    print("El número 2 está en la lista.")

print("Índice del número 3:", lista1.index(3))  # Devuelve el índice de la primera ocurrencia

print("Cantidad de veces que aparece el número 2:", lista1.count(2))  # Cuenta las ocurrencias


# 7. Ordenamiento de listas:
# - Las listas pueden ser ordenadas de manera ascendente o descendente.

print("\n--- Ordenamiento de listas ---")
lista_desordenada = [5, 1, 4, 2, 8]

# Ordenamiento in-place (modificando la lista original):
lista_desordenada.sort()  
print("Lista ordenada con sort():", lista_desordenada)

# Ordenamiento creando una nueva lista:
lista_desordenada = [5, 1, 4, 2, 8]
lista_ordenada = sorted(lista_desordenada)  
print("Lista original:", lista_desordenada)
print("Lista ordenada con sorted():", lista_ordenada)

# Ordenar de forma descendente:
lista_desordenada.sort(reverse=True)  
print("Lista ordenada descendentemente:", lista_desordenada)


# 8. Listas anidadas (matrices):
# - Las listas pueden contener otras listas, formando una estructura similar a una matriz.

print("\n--- Listas anidadas (matrices) ---")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:", matriz)
print("Elemento en la fila 1, columna 2:", matriz[1][2])  # Accedemos al número 6


# 9. Comprensión de listas:
# - Las comprensiones de listas permiten crear nuevas listas aplicando una expresión a los elementos existentes de manera concisa.

print("\n--- Comprensión de listas ---")
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]  # Crear una lista con los cuadrados de los números
print("Lista de cuadrados:", cuadrados)

pares = [x for x in numeros if x % 2 == 0]  # Crear una lista con los números pares
print("Lista de números pares:", pares)


# 10. Copia de listas:
# - Se puede crear una copia de una lista usando el método copy(), lo que genera una copia independiente de la lista original.

lista_original = [1, 2, 3]
copia_lista = lista_original.copy()  # Crea una copia independiente
copia_lista[0] = 10  # Modificando la copia
print("\nLista original:", lista_original)
print("Copia de la lista:", copia_lista)
