# FUNCIONES INTEGRADAS EN PYTHON




# 1. Encontrando el número mayor y menor en una lista
print("1. Número mayor y menor en una lista:")
numeros = [4, 7, 1, 42, 15]

numero_alto = max(numeros)
numero_bajo = min(numeros)

print(f"- El número más bajo es: {numero_bajo}")  # Output: 1
print(f"- El número más alto es: {numero_alto}")  # Output: 42
print()





# 2. Redondeando números decimales
print("2. Redondeando números decimales:")
numero_decimal = 21.3456
numero_redondeado = round(numero_decimal, 3)

print(f"- El número redondeado a 3 decimales es: {numero_redondeado}")  # Output: 21.346
print()




# 3. Convirtiendo valores a booleanos con bool()
print("3. Convirtiendo valores a booleanos:")
print(f"- bool(0): {bool(0)}")              # False
print(f"- bool(''): {bool('')}")           # False
print(f"- bool([]): {bool([])}")           # False
print(f"- bool(1): {bool(1)}")             # True
print(f"- bool('Hola'): {bool('Hola')}")   # True
print(f"- bool([1, 2]): {bool([1, 2])}")   # True
print()




# 4. Verificando si todos los elementos son verdaderos con all()
print("4. Verificando si todos los elementos son verdaderos (all):")
print(f"- all([234, 'True', 1, [1]]): {all([234, 'True', 1, [1]])}")  # True
print(f"- all([234, '', 1, [1]]): {all([234, '', 1, [1]])}")          # False
print(f"- all([1, 2, 0]): {all([1, 2, 0])}")                          # False
print()





# 5. Sumando números en una lista con sum()
print("5. Sumando números en una lista:")
numeros = [12, 44, 11, 99, 11]
suma = sum(numeros)
print(f"- La suma de todos los números es: {suma}")  # Output: 177
print()




# 6. Aplicando operaciones a cada elemento con map()
print("6. Aplicando operaciones con map:")
# Duplicar los números de la lista
numeros_duplicados = list(map(lambda x: x * 2, numeros))

print(f"- Números originales: {numeros}")
print(f"- Números duplicados: {numeros_duplicados}")
print()






# 7. Contando elementos en un iterable con len()
print("7. Contando elementos en una lista:")
cantidad_numeros = len(numeros)

print(f"- La cantidad de números en la lista es: {cantidad_numeros}")
print()

# EXPLICACIONES GENERALES:
# - max(iterable): Retorna el valor máximo en un iterable.
# - min(iterable): Retorna el valor mínimo en un iterable.
# - round(numero, ndigits): Redondea un número a la cantidad de decimales especificada.
# - bool(valor): Convierte un valor a booleano.
# - all(iterable): Retorna True si todos los elementos son verdaderos, False en caso contrario.
# - sum(iterable): Suma todos los elementos de un iterable.
# - map(funcion, iterable): Aplica una función a cada elemento de un iterable y devuelve un map object.
# - len(iterable): Retorna la cantidad de elementos en un iterable.
