
# Definición de la función lambda 'primos_hasta' que toma un argumento 'num'
primos_hasta = lambda num: list(
    # Usamos 'filter' para filtrar los números primos en el rango de 2 hasta 'num - 1'
    filter(
        # Función lambda que recibe cada número 'x' del rango
        lambda x: all(
            # 'all' verifica que todos los resultados sean True
            # Comprobamos que 'x' no sea divisible por ningún número entre 2 y la raíz cuadrada de 'x'
            x % i != 0
            for i in range(2, int(x ** 0.5) + 1)  # Iteramos desde 2 hasta la raíz cuadrada de 'x'
        ),
        # Rango de números a comprobar: de 2 hasta 'num - 1'
        range(2, num)
    )
)

# Llamamos a la función con el argumento 15 y mostramos el resultado
print(primos_hasta(20)) 
