# Métodos de las listas en Python: Guía completa

# 1. Creación de listas
print("\n--- 1. Creación de listas ---")


lista_original = ["Hola", "Gustavo", 19, True, 3.14]  # Lista con varios tipos de datos
print("Lista original:", lista_original)

lista_vacia = []  # Lista vacía
print("Lista vacía:", lista_vacia)

# 2. Obtener la longitud de una lista
print("\n--- 2. Longitud de una lista ---")
longitud = len(lista_original)
print("Longitud de lista_original:", longitud)
longitud_vacia = len(lista_vacia)
print("Longitud de lista_vacia:", longitud_vacia)





###################################

###################################

###################################



# 3. Añadir elementos a una lista
print("\n--- 3. Añadir elementos ---")

# a) append(elemento): Añade un elemento al final de la lista
lista_original.append("Python")
print("Lista con append('Python'):", lista_original)

# b) insert(índice, elemento): Inserta un elemento en un índice específico
lista_original.insert(2, "Nuevo valor")  # Inserta "Nuevo valor" en el índice 2
print("Lista con insert(2, 'Nuevo valor'):", lista_original)

# c) extend(iterable): Añade múltiples elementos de un iterable (como otra lista, tupla o string) al final
lista_original.extend([False, 2025, "Otro más"])
print("Lista con extend([False, 2025, 'Otro más']):", lista_original)
lista_original.extend("ABC") #Extend también funciona con strings, agregando cada caracter como un elemento
print("Lista con extend('ABC'):", lista_original)
lista_original.extend((1,2)) #Extend también funciona con tuplas
print("Lista con extend((1,2)):", lista_original)



#####################################

#####################################

#####################################



# 4. Eliminar elementos de una lista
print("\n--- 4. Eliminar elementos ---")

# a) pop(índice): Elimina el elemento en el índice dado y lo retorna. Si no se especifica índice, elimina y retorna el último.
elemento_eliminado = lista_original.pop(3)  # Elimina el elemento en el índice 3
print("Lista con pop(3):", lista_original)
print("Elemento eliminado con pop(3):", elemento_eliminado)

ultimo_elemento = lista_original.pop()  # Elimina y retorna el último elemento
print("Lista con pop():", lista_original)
print("Último elemento eliminado con pop():", ultimo_elemento)

# b) remove(valor): Elimina la *primera* ocurrencia del valor dado. Lanza ValueError si el valor no está.
try:
    lista_original.remove("Gustavo")
    print("Lista con remove('Gustavo'):", lista_original)
    lista_original.remove("Valor que no existe")  # Provocará un ValueError
except ValueError as e:
    print(f"Error al usar remove(): {e}")

# c) del lista[índice]: Elimina el elemento en el índice dado (similar a pop pero no retorna el valor)
del lista_original[0]
print("Lista con del lista[0]:", lista_original)

# d) clear(): Elimina *todos* los elementos de la lista
lista_copia = lista_original[:] # Creamos una copia de la lista para no perder los datos
lista_copia.clear()
print("Lista con clear():", lista_copia)



###################################################

# 5. Ordenar listas
print("\n--- 5. Ordenar listas ---")

lista_numeros = [1, 2, 3, 4, 5, 912, 12, 1]

# a) sort(): Ordena la lista *in-place* (modifica la lista original).
lista_numeros.sort()  # Orden ascendente (por defecto)
print("Lista ordenada con sort():", lista_numeros)

lista_numeros.sort(reverse=True)  # Orden descendente
print("Lista ordenada descendentemente con sort():", lista_numeros)

# b) sorted(iterable): Crea una *nueva* lista ordenada, dejando la original intacta.
lista_desordenada = [5, 2, 8, 1, 9]
lista_ordenada = sorted(lista_desordenada)
print("Lista original (desordenada):", lista_desordenada)
print("Nueva lista ordenada con sorted():", lista_ordenada)

lista_ordenada_desc = sorted(lista_desordenada, reverse=True)
print("Nueva lista ordenada descendentemente con sorted():", lista_ordenada_desc)

# c) Ordenar strings y con key
print("\n--- 5.c Ordenar strings y con key ---")
lista_palabras = ["manzana", "banana", "cereza", "dátil", "arándano"]
lista_palabras.sort(key=len)  # Ordena por longitud de palabra
print("Lista ordenada por longitud de palabra:", lista_palabras)

lista_palabras = ["manzana", "banana", "cereza", "dátil", "arándano"]
lista_palabras.sort()  # Ordena alfabéticamente (por defecto)
print("Lista ordenada alfabéticamente:", lista_palabras)





# 6. Otros métodos útiles (mención breve)
print("\n--- 6. Otros métodos útiles (mención breve) ---")

lista_ejemplo = [1, 2, 2, 3, 2, 4]

# count(valor): Cuenta cuántas veces aparece un valor en la lista
cantidad_de_dos = lista_ejemplo.count(2)
print("Cantidad de veces que aparece el 2:", cantidad_de_dos)

# index(valor): Devuelve el índice de la *primera* ocurrencia del valor. Lanza ValueError si no está.
indice_del_tres = lista_ejemplo.index(3)
print("Índice de la primera aparición del 3:", indice_del_tres)

# copy(): Crea una copia superficial de la lista
copia_lista = lista_ejemplo.copy()
print("Copia de la lista:", copia_lista)