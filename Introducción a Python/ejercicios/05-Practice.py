# Creando una función que muestre la serie de fibonacci

def fibonacci(num):
    # Definimos los dos primeros números de la sucesión de Fibonacci.
    a, b = 0, 1  
    # Creamos una lista para almacenar los números de la sucesión, comenzando con el primer número (0).
    fibonacci_lista = [0]  

    # Iteramos un número de veces definido por 'num'.
    for i in range(num):
        # Si el siguiente número 'b' es mayor que el límite dado, devolvemos la lista actual.
        if b > num:  
            return fibonacci_lista  
        else:
            # Agregamos el valor actual de 'b' a la lista.
            fibonacci_lista.append(b)  
            # Actualizamos 'a' con el valor de 'b' y 'b' con la suma de los dos anteriores.
            a, b = b, a + b  

# Generamos la sucesión de Fibonacci hasta 34 y mostramos el resultado.
resultado = fibonacci(34)
print(resultado)
