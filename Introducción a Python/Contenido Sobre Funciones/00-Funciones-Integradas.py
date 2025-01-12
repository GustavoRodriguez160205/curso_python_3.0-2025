# Funciones integradas en Python - Ejemplos

# 1. Encontrar el número mayor y menor en una lista
print("1. Encontrar el número mayor y menor en una lista:")

numeros = [4, 7, 1, 42, 15]
numero_alto = max(numeros)
numero_bajo = min(numeros)

print(f"- El número más alto es: {numero_alto}")  # Output: 42
print(f"- El número más bajo es: {numero_bajo}")  # Output: 1
print()


# 2. Redondear números decimales
print("2. Redondear números decimales:")

numero_decimal = 21.3456
numero_redondeado = round(numero_decimal, 3)  # Redondea a 3 decimales

print(f"- Número original: {numero_decimal}")
print(f"- Número redondeado: {numero_redondeado}")  # Output: 21.346
print()


# 3. Conversión a booleanos con bool()
print("3. Conversión a booleanos con bool():")

print(f"- bool(0): {bool(0)}")               # False
print(f"- bool(''): {bool('')}")             # False
print(f"- bool([1, 2]): {bool([1, 2])}")     # True
print(f"- bool('Hola'): {bool('Hola')}")     # True
print()


# 4. Comprobación con all()
print("4. Comprobación con all():")

resultado_all = all([1, "True", [1]])  # True, todos los elementos son "verdaderos"
print(f"- all([1, 'True', [1]]): {resultado_all}")  # Output: True
print()


# 5. Suma de una lista con sum()
print("5. Suma de una lista usando sum():")

numeros = [12, 44, 11, 99, 11]
suma = sum(numeros)
print(f"- La suma de todos los números es: {suma}")  # Output: 177
print()


# 6. Uso de map() con una función definida
print("6. Elevar números al cuadrado usando una función con map():")

def al_cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(al_cuadrado, numeros))

print(f"- Números originales: {numeros}")
print(f"- Números al cuadrado: {cuadrados}")  # Output: [1, 4, 9, 16, 25]
print()


# 7. Encontrar el valor absoluto con abs()
print("7. Encontrar el valor absoluto usando abs():")

negativo = -15
valor_absoluto = abs(negativo)

print(f"- Número original: {negativo}")
print(f"- Valor absoluto: {valor_absoluto}")  # Output: 15
print()


# 8. Combinar listas con zip()
print("8. Combinar listas usando zip():")

nombres = ["Ana", "Juan", "Luis"]
edades = [25, 30, 22]
combinado = list(zip(nombres, edades))

print(f"- Nombres: {nombres}")
print(f"- Edades: {edades}")
print(f"- Combinado: {combinado}")  # Output: [('Ana', 25), ('Juan', 30), ('Luis', 22)]
print()


# 9. Ordenar elementos con sorted()
print("9. Ordenar elementos usando sorted():")

desordenados = [42, 15, 7, 1, 4]
ordenados = sorted(desordenados)

print(f"- Lista original: {desordenados}")
print(f"- Lista ordenada: {ordenados}")  # Output: [1, 4, 7, 15, 42]
print()


# Descripción de las funciones utilizadas:

# 1. **max(iterable, *args, key=None, default=None)**:
#   - Devuelve el valor más grande del iterable. Si se pasan varios argumentos, devuelve el máximo de esos valores.
#   - Si el iterable está vacío y no se proporciona un valor `default`, lanzará un error `ValueError`.

# 2. **min(iterable, *args, key=None, default=None)**:
#   - Devuelve el valor más pequeño del iterable. Similar a `max`, si el iterable está vacío y no se especifica `default`, lanzará un error.
   
# 3. **round(number, ndigits=None)**:
#   - Redondea un número flotante al número de decimales especificado por `ndigits`. Si no se proporciona, se redondea al número entero más cercano. 
#   - Python sigue el redondeo al par más cercano, conocido como "redondeo bancario".

# 4. **bool(x)**:
#  - Convierte el valor `x` a un valor booleano. Retorna `False` si el valor es considerado "vacío" (como `0`, `None`, `""`, listas vacías, etc.), y `True` en cualquier otro caso.

# 5. **all(iterable)**:
#   - Retorna `True` si todos los elementos del iterable son "verdaderos". Si al menos un elemento es "falso", devuelve `False`.
#   - Si el iterable está vacío, retorna `True`.

# 6. **sum(iterable, /, start=0)**:
#    - Suma los elementos de un iterable (como una lista o tupla). El parámetro `start` se utiliza para definir un valor inicial, que se suma al total (por defecto es `0`).
#    - Se puede usar con cualquier iterable que contenga números.

# 7. **map(function, iterable, ...)**:
#    - Aplica la función `function` a cada elemento del iterable o iterables dados. Retorna un "map object", que puede ser convertido en una lista, tupla o cualquier otro iterable.
 #   - Usado comúnmente para realizar transformaciones masivas sobre los elementos de una secuencia.

# 8. **abs(x)**:
#    - Devuelve el valor absoluto de un número `x`. Si `x` es negativo, devuelve el valor de `x` sin el signo negativo.

# 9. **zip(*iterables)**:
#    - Combina dos o más iterables (listas, tuplas, etc.) en tuplas, emparejando sus elementos en orden. El número de elementos por tupla es igual al número de iterables pasados como argumento.
#    - Si las secuencias tienen longitudes diferentes, el iterador se detendrá cuando se termine el más corto.

# 10. **sorted(iterable, key=None, reverse=False)**:
#     - Devuelve una lista nueva con los elementos de `iterable` ordenados. 
#     - El parámetro `key` se puede usar para ordenar según una función específica, y `reverse=True` invierte el orden (de mayor a menor).

