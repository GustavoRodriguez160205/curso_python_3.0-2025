# Introducción a las listas en Python
# Las listas son colecciones ordenadas que permiten almacenar elementos de cualquier tipo. 
# Son útiles para gestionar conjuntos de datos dinámicos y realizar operaciones como agregar, eliminar, buscar y ordenar.

print("\n--- Ejemplos prácticos de métodos y operaciones con listas ---")



# 1. Creación de listas
print("\n--- 1. Creación de listas ---")
nombres = ["Ana", "Luis", "Pedro", "Marta"]  # Lista de cadenas
edades = [18, 25, 30, 40]  # Lista de enteros
mixta = ["Juan", 23, 1.85, True]  # Lista con elementos de diferentes tipos

print("Lista de nombres:", nombres)
print("Lista de edades:", edades)
print("Lista mixta:", mixta)




# 2. Modificar elementos de una lista
print("\n--- 2. Modificar elementos ---")
nombres[1] = "Lucas"  # Cambia el elemento en el índice 1
print("Lista de nombres modificada:", nombres)




# 3. Slicing (rebanado)
print("\n--- 3. Slicing (rebanado) ---")
print("Primeros dos elementos de edades:", edades[:2])  # Elementos en índices 0 y 1
print("Últimos dos elementos de edades:", edades[-2:])  # Últimos dos elementos





# 4. Combinar listas y eliminar duplicados
print("\n--- 4. Combinar listas y eliminar duplicados ---")
lista_a = [1, 2, 3]
lista_b = [3, 4, 5]
combinada = lista_a + lista_b  # Combina las listas
sin_duplicados = list(set(combinada))  # Elimina duplicados convirtiendo a conjunto y luego a lista
print("Lista combinada:", combinada)
print("Lista sin duplicados:", sin_duplicados)




# 5. Iterar sobre una lista
print("\n--- 5. Iterar sobre una lista ---")
for nombre in nombres:
    print(f"Hola, {nombre}!")  # Saluda a cada nombre en la lista





# 6. Operaciones con listas numéricas
print("\n--- 6. Operaciones con listas numéricas ---")
numeros = [10, 20, 30, 40]
suma = sum(numeros)  # Suma de todos los elementos
promedio = suma / len(numeros)  # Promedio
print("Lista de números:", numeros)
print("Suma de números:", suma)
print("Promedio:", promedio)




# 7. Comprobaciones con listas
print("\n--- 7. Comprobaciones con listas ---")
colores = ["rojo", "verde", "azul"]
print("¿'verde' está en colores?", "verde" in colores)
print("¿'amarillo' no está en colores?", "amarillo" not in colores)




# 8. Filtrar listas
print("\n--- 8. Filtrar listas ---")
edades_adultos = [edad for edad in edades if edad >= 18]  # Filtra edades mayores o iguales a 18
print("Edades de adultos:", edades_adultos)


# 9. Ordenar listas con claves personalizadas
print("\n--- 9. Ordenar listas con claves personalizadas ---")
personas = [("Ana", 18), ("Luis", 25), ("Pedro", 22)]
ordenadas_por_edad = sorted(personas, key=lambda x: x[1])  # Ordena por edad (índice 1)
print("Lista de personas ordenada por edad:", ordenadas_por_edad)



# 10. Duplicar y modificar listas
print("\n--- 10. Copia y modificación de listas ---")
original = [1, 2, 3]
copia = original.copy()  # Crea una copia
copia.append(4)  # Modifica la copia
print("Lista original:", original)
print("Copia modificada:", copia)



# 11. Otros métodos útiles
print("\n--- 11. Otros métodos útiles ---")

# Añadir elementos
mi_lista = [1, 2, 3]
mi_lista.append(4)  # Añade 4 al final
print("Lista con append(4):", mi_lista)

mi_lista.insert(2, "Nuevo")  # Inserta "Nuevo" en el índice 2
print("Lista con insert(2, 'Nuevo'):", mi_lista)

mi_lista.extend([5, 6])  # Añade múltiples elementos al final
print("Lista con extend([5, 6]):", mi_lista)




# Eliminar elementos

mi_lista.remove(2)  # Elimina la primera ocurrencia de 2
print("Lista con remove(2):", mi_lista)

elemento_eliminado = mi_lista.pop()  # Elimina y retorna el último elemento
print("Lista con pop():", mi_lista)
print("Elemento eliminado:", elemento_eliminado)

del mi_lista[0]  # Elimina el elemento en el índice 0
print("Lista con del mi_lista[0]:", mi_lista)

mi_lista.clear()  # Elimina todos los elementos
print("Lista con clear():", mi_lista)

# Contar ocurrencias
ejemplo = [1, 2, 2, 3, 3, 3, 4]
conteo = ejemplo.count(3)  # Cuenta cuántas veces aparece el valor 3
print("Cantidad de veces que aparece 3:", conteo)

# Obtener el índice de un elemento
indice = ejemplo.index(2)  # Encuentra el índice de la primera aparición del valor 2
print("Índice de la primera aparición de 2:", indice)

# Revertir la lista
mi_lista = [1, 2, 3, 4]
mi_lista.reverse()  # Reversa la lista
print("Lista revertida:", mi_lista)

# Ordenar la lista
mi_lista = [4, 2, 3, 1]
mi_lista.sort()  # Ordena la lista en el lugar
print("Lista ordenada con sort():", mi_lista)






# 12. Desempaquetado de listas
print("\n--- 12. Desempaquetado de listas ---")
a, b, *resto = [1, 2, 3, 4, 5]
print("a:", a)
print("b:", b)
print("resto:", resto)







# 13. Uso de list() para convertir a lista
print("\n--- 13. Uso de list() para convertir a lista ---")
tupla = (1, 2, 3)
lista_convertida = list(tupla)  # Convierte la tupla en una lista
print("Tupla convertida en lista:", lista_convertida)





# 14. Enumerar elementos de una lista
print("\n--- 14. Enumerar elementos de una lista ---")
for indice, valor in enumerate(nombres):  # Obtiene el índice y el valor
    print(f"Índice {indice}: {valor}")





# 15. Comparaciones entre `sort()` y `sorted()`
print("\n--- 15. Comparación entre sort() y sorted() ---")
# sort() ordena en el lugar y no devuelve nada
numeros = [3, 1, 2]
numeros.sort()
print("Lista ordenada con sort():", numeros)

# sorted() devuelve una nueva lista ordenada sin modificar la original
numeros_original = [3, 1, 2]
numeros_ordenados = sorted(numeros_original)
print("Lista original:", numeros_original)
print("Lista ordenada con sorted():", numeros_ordenados)
