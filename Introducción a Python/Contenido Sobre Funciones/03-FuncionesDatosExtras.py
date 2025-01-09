# Los keyword arguments (kwargs) en Python permiten pasar argumentos a una función utilizando el nombre del parámetro como clave.
# Esto mejora la legibilidad del código y permite cambiar el orden de los argumentos al llamar a la función.

def frase(nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

# Llamada a la función utilizando keyword arguments
frase_resultante = frase(adjetivo="capo", nombre="Lucas", apellido="Dalto")
print(frase_resultante)  # "Hola Lucas Dalto, sos muy capo"

# Ventajas de los keyword arguments:
# 1. Claridad: Al usar keyword arguments, el propósito de cada argumento es claro.
# 2. Flexibilidad: Puedes cambiar el orden de los argumentos sin afectar la llamada a la función.
# 3. Valores por defecto: Puedes combinar keyword arguments con valores por defecto para hacer que los parámetros sean opcionales.

########################################################
########################################################
########################################################

# Los parámetros opcionales son aquellos que no tienen que ser proporcionados al llamar a una función.
# En lugar de exigir un valor al llamar a la función, puedes asignarles un valor por defecto.
# Los valores por defecto permiten establecer un valor inicial para un parámetro en caso de que el usuario no lo proporcione.

def calcular_area(base, altura=10):
    return base * altura

# Llamada a la función proporcionando ambos parámetros
area_resultante = calcular_area(5, 8)
print(f'Área con base 5 y altura 8: {area_resultante}')  # 40

# Llamada a la función proporcionando solo el parámetro 'base'
# Como no se proporciona 'altura', se usará el valor por defecto de 10
area_resultante = calcular_area(5)
print(f'Área con base 5 y altura por defecto (10): {area_resultante}')  # 50
