# Creando una función que nos devuelva los números primos
# Entre 0 y el argumento que le pasemos.

# Función para verificar si un número es primo
def es_primo(num):
    # Comprobamos si el número es divisible por algún número entre 2 y num - 1.
    # Si encontramos un divisor, el número no es primo.
    for i in range(2, num):
        if num % i == 0:
            return False  # No es primo, salimos del bucle
    # Si no se encuentra ningún divisor, el número es primo
    return True

# Función para generar una lista de números primos hasta un número dado
def primos_hasta(num):
    primos = []  # Lista para almacenar los números primos
    for i in range(2, num + 1):
        if es_primo(i):  # Verificamos si el número actual es primo
            primos.append(i)  # Lo agregamos a la lista si es primo
    return primos

# Ejemplo de uso: lista de números primos hasta 98
resultado = primos_hasta(98)
print(f"Números primos hasta 98: {resultado}")
