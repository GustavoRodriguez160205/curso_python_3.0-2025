

############################################

# OPERADORES ARITMETRICOS

############################################

# Definimos los números para las operaciones
num1 = 12
num2 = 5
num3 = 4

# Realizamos las operaciones aritméticas
suma = num1 + num2
resta = num1 - num3
multiplicacion = num1 * num2
division = num1 / num2  # División con resultado flotante
potencia = num1 ** num2  # Exponenciación
division_entera = num1 // num2  # División entera (sin decimales)
resto = num1 % num3  # Resto de la división

# Presentación de los resultados
print("=" * 50)
print(" Resultados de Operaciones Aritméticas ".center(50, ' '))
print("=" * 50)

# Mostrar cada operación con claridad
print(f"Suma:                {num1} + {num2} = {suma}")
print(f"Resta:               {num1} - {num3} = {resta}")
print(f"Multiplicación:      {num1} * {num2} = {multiplicacion}")
print(f"División:            {num1} / {num2} = {division:.2f} (con 2 decimales)")
print(f"Potenciación:        {num1} ** {num2} = {potencia}")
print(f"División entera:     {num1} // {num2} = {division_entera}")
print(f"Resto:               {num1} % {num3} = {resto}")

print("=" * 50)




################################################################


# OPERADORES DE COMPARACIÓN


#################################################################


# Operadores de Comparación en Python

# Los operadores de comparación se utilizan para comparar dos valores.
# El resultado de una comparación es un valor booleano: True o False.

# Es mayor que (>)
# Devuelve True si el operando de la izquierda es mayor que el operando de la derecha.
print("3 > 4:", 3 > 4)  # Salida: False

# Es menor que (<)
# Devuelve True si el operando de la izquierda es menor que el operando de la derecha.
print("3 < 4:", 3 < 4)  # Salida: True

# Es mayor o igual que (>=)
# Devuelve True si el operando de la izquierda es mayor o igual que el operando de la derecha.
print("3 >= 4:", 3 >= 4)  # Salida: False

# Es menor o igual que (<=)
# Devuelve True si el operando de la izquierda es menor o igual que el operando de la derecha.
print("4 <= 4:", 4 <= 4)  # Salida: True

# Son iguales (==)
# Devuelve True si ambos operandos son iguales.
print("3 == 4:", 3 == 4)  # Salida: False

# Son distintos (!=)
# Devuelve True si ambos operandos son diferentes.
print("3 != 4:", 3 != 4)  # Salida: True





# Ejemplos adicionales para mayor claridad

# Comparación de cadenas
# Las cadenas se comparan lexicográficamente utilizando el orden alfabético.
print('"apple" < "banana":', "apple" < "banana")  # Salida: True

# Comparación de listas
# Las listas se comparan elemento por elemento.
print('[1, 2, 3] == [1, 2, 3]:', [1, 2, 3] == [1, 2, 3])  # Salida: True
print('[1, 2, 3] != [1, 2, 4]:', [1, 2, 3] != [1, 2, 4])  # Salida: True

# Comparación de números flotantes
# Los números flotantes se comparan de la misma manera que los enteros.
print('3.5 > 2.5:', 3.5 > 2.5)  # Salida: True
print('3.5 < 2.5:', 3.5 < 2.5)  # Salida: False

# Comparación de booleanos
# Los valores booleanos se comparan como enteros: False es 0 y True es 1.
print('True == 1:', True == 1)  # Salida: True
print('False == 0:', False == 0)  # Salida: True


# Calculos Combinados

a = 30
b = 15
c = 20

comparacion = a +  b == c
print(f"El resultado de la comparación es: {comparacion}")


# Comparación de Usuarios

usuariosDeBd = "Gustavo12"
usuarioTipeado = "Gusta"

print(usuariosDeBd == usuarioTipeado)



############################################################



# OPERADORES LÓGICOS



##############################################################


## Operadores Lógicos

#AND

Resultado = True & True #Devolver True
Resultado2 = False & True #Devolver Falso
Resultado3 = True & False #Devolver Falso
Resultado4 = False & False #Devolver Falso

#OR

Resultado5 = True | True #Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True | False #Devolver True
Resultado8 = False | False #Devolver Falso

#NOT

Resultado9 = not True #Devolver Falso
Resultado10 = not False #Devolver True