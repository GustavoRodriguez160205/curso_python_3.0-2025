"""" Las listas en Python son:
- **Ordenadas:** Los elementos tienen un orden específico que se mantiene.
- **Mutables:** Se pueden modificar después de su creación (añadir, eliminar, cambiar elementos).
- **Heterogéneas:** Pueden contener elementos de diferentes tipos de datos.
- **Dinámicas:** Su tamaño puede crecer o disminuir.
- **Indexadas:** Se accede a sus elementos mediante índices numéricos (empezando desde 0).

"""

# 1. Creación de listas:

# a. Usando corchetes []:
mi_lista = [1, 2, 3, "hola", 3.14, True]  # Listas pueden contener diferentes tipos de datos
print("Lista creada con []:", mi_lista)

# b. Usando la función list():
otra_lista = list((4, 5, 6))  # Convirtiendo una tupla a lista
print("Lista creada con list():", otra_lista)

cadena = "Python"
lista_desde_cadena = list(cadena) #Convierte una cadena en una lista de caracteres
print("Lista creada desde una cadena:", lista_desde_cadena)

lista_vacia = [] #Lista vacía
print("Lista vacía:", lista_vacia)

# 2. Acceso a los elementos:

print("\n--- Acceso a elementos ---")
print("Primer elemento:", mi_lista[0])  # Índices comienzan desde 0
print("Último elemento:", mi_lista[-1])  # Índice negativo para acceder desde el final
print("Sublista (slicing):", mi_lista[1:4])  # Desde el índice 1 hasta el 3 (no inclusive)
print("Sublista desde el inicio:", mi_lista[:3]) #Desde el inicio hasta el índice 2
print("Sublista hasta el final:", mi_lista[2:]) #Desde el índice 2 hasta el final
print("Sublista con paso:", mi_lista[::2]) #Desde el inicio hasta el final con paso 2
print("Sublista con paso negativo:", mi_lista[::-1]) #Invierte la lista

# 3. Modificación de listas:

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

print("\n--- Eliminación de elementos ---")
del mi_lista[3]  # Eliminando un elemento por índice
print("Lista con del:", mi_lista)

elemento_eliminado = mi_lista.pop(1)  # Eliminando un elemento por índice y obteniendo su valor
print("Elemento eliminado con pop():", elemento_eliminado)
print("Lista después de pop():", mi_lista)

mi_lista.remove(3.14)  # Eliminando un elemento por valor (solo la primera ocurrencia)
print("Lista con remove():", mi_lista)

mi_lista.clear() #Elimina todos los elementos de la lista
print("Lista con clear():", mi_lista)

mi_lista = [1, 2, 3, 4, 5] #Recreamos la lista para los siguientes ejemplos

# 5. Operaciones con listas:

print("\n--- Operaciones con listas ---")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2  # Concatenación
print("Listas concatenadas:", lista_concatenada)

lista_repetida = lista1 * 3  # Repetición
print("Lista repetida:", lista_repetida)

print("Longitud de la lista:", len(lista1))  # Longitud
print("Máximo de la lista:", max(lista1))  # Máximo (solo para tipos comparables)
print("Mínimo de la lista:", min(lista1))  # Mínimo (solo para tipos comparables)
print("Suma de la lista:", sum(lista1)) #Suma (solo para tipos numéricos)

# 6. Búsqueda en listas:

print("\n--- Búsqueda en listas ---")
if 2 in lista1:
    print("El número 2 está en la lista.")

print("Índice del número 3:", lista1.index(3))  # Devuelve el índice de la primera ocurrencia

print("Cantidad de veces que aparece el número 2:", lista1.count(2))  # Cuenta las ocurrencias

# 7. Ordenamiento de listas:

print("\n--- Ordenamiento de listas ---")
lista_desordenada = [5, 1, 4, 2, 8]
lista_desordenada.sort()  # Ordena la lista IN-PLACE (modifica la lista original)
print("Lista ordenada con sort():", lista_desordenada)

lista_desordenada = [5, 1, 4, 2, 8]
lista_ordenada = sorted(lista_desordenada) #Crea una NUEVA lista ordenada
print("Lista original:", lista_desordenada)
print("Lista ordenada con sorted():", lista_ordenada)

lista_desordenada.sort(reverse=True) #Ordena la lista de forma descendente
print("Lista ordenada descendentemente:", lista_desordenada)

# 8. Listas anidadas (matrices):

print("\n--- Listas anidadas (matrices) ---")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:", matriz)
print("Elemento en la fila 1, columna 2:", matriz[1][2]) #Accedemos al número 6

# 9. Comprensión de listas:

print("\n--- Comprensión de listas ---")
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print("Lista de cuadrados:", cuadrados)

pares = [x for x in numeros if x % 2 == 0]
print("Lista de números pares:", pares)

#10. Copia de listas
lista_original = [1, 2, 3]
copia_lista = lista_original.copy() #Crea una copia independiente
copia_lista[0] = 10
print("\nLista original:", lista_original)
print("Copia de la lista:", copia_lista)

