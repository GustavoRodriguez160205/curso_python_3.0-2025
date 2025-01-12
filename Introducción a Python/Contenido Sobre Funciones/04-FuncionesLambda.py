# === EXPLICACIÓN COMPLETA Y EJEMPLOS DE FUNCIONES LAMBDA EN PYTHON ===

# Las funciones lambda son funciones anónimas (sin nombre) definidas en una sola línea.
# Su sintaxis es: lambda argumentos: expresión
# Son útiles para tareas pequeñas y rápidas, donde no necesitas definir una función con 'def'.



# Ejemplo 1: Duplicar un número
duplicar = lambda x: x * 2  # La lambda toma un argumento (x) y devuelve x multiplicado por 2.
print("Duplicar 4 usando lambda:", duplicar(4))  # Salida: 8

# Ejemplo 2: Sumar dos números
sumar = lambda a, b: a + b  # Lambda con múltiples argumentos
print("Suma de 3 y 5:", sumar(3, 5))  # Salida: 8

# Ejemplo 3: Verificar si un número es par
es_par = lambda x: x % 2 == 0  # Devuelve True si el número es divisible por 2.
print("¿Es 4 par?", es_par(4))  # Salida: True
print("¿Es 5 par?", es_par(5))  # Salida: False




# === LAMBDA CON FUNCIONES MAP Y FILTER ===

# Lista de números para aplicar map y filter
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# map(funcion, iterable): Aplica la función a cada elemento del iterable.
# Multiplica cada número de la lista por 2.
multiplicados_por_dos = list(map(lambda x: x * 2, numeros))
print("Números multiplicados por 2:", multiplicados_por_dos)  # Salida: [2, 4, 6, 8, ...]

# filter(funcion, iterable): Filtra los elementos que cumplen una condición.
# Selecciona solo los números pares de la lista.
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", numeros_pares)  # Salida: [2, 4, 6, 8]






# === MÁS EJEMPLOS PRÁCTICOS DE LAMBDA ===

# Ejemplo 4: Ordenar una lista de tuplas por el segundo valor
tuplas = [(1, 'b'), (3, 'a'), (2, 'c')]
# Usamos lambda como key para indicar que queremos ordenar por el segundo elemento (índice 1).
ordenadas = sorted(tuplas, key=lambda x: x[1])
print("Tuplas ordenadas por el segundo valor:", ordenadas)  # Salida: [(3, 'a'), (1, 'b'), (2, 'c')]

# Ejemplo 5: Calcular el cuadrado de un número
cuadrado = lambda x: x ** 2
print("Cuadrado de 5:", cuadrado(5))  # Salida: 25

# === CONCLUSIÓN ===
# 1. Lambdas permiten escribir funciones simples en una línea, mejorando la legibilidad.
# 2. Son útiles con funciones de orden superior como map(), filter(), y sorted().
# 3. Aunque compactas, lambdas son menos legibles para lógica compleja, donde es mejor usar 'def'.
