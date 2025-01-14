"""
Guía completa del bucle while en Python.

Este script cubre:
- Sintaxis básica
- Funcionamiento con ejemplos
- Bucle infinito (y cómo evitarlo)
- Inicialización de variables
- Uso de break y continue
- while con else
"""




# 1. Sintaxis básica:
print("\n--- 1. Sintaxis básica ---")
contador = 0  # Inicialización de la variable contador

while contador < 5:  # Condición: mientras contador sea menor que 5
    print(f"Contador: {contador}")  # Imprime el valor del contador
    contador += 1  # Incrementa el contador (¡ESENCIAL para evitar bucles infinitos!)

print("Fin del bucle while básico.\n")





# 2. Funcionamiento (explicado en el código):
print("\n--- 2. Funcionamiento ---")
numero = 10

print("Comienza el bucle:")

while numero > 0:  # Condición: mientras numero sea mayor que 0
    print(f"Número actual: {numero}")
    numero -= 2  # Restamos 2 en cada iteración
    print("Se resta 2 al número.")

print("La condición 'numero > 0' ya no se cumple. Fin del bucle.\n")





# 3. Bucle infinito (¡CUIDADO!):
print("\n--- 3. Bucle infinito (¡CUIDADO!) ---")
# Descomenta el siguiente bloque para ver un bucle infinito en acción:
# contador_infinito = 0
# while contador_infinito < 5:
#     print("¡Esto se imprimirá indefinidamente!")
#     # ¡Falta el incremento! contador_infinito += 1 (Comenta la linea anterior y descomenta esta para que funcione)

print("Recuerda SIEMPRE incrementar/modificar la variable de control dentro del bucle para evitar bucles infinitos.\n")

# 4. Inicialización de variables:
print("\n--- 4. Inicialización de variables ---")
variable_control = 7  # Inicialización CORRECTA

while variable_control > 2:
    print(f"Valor de la variable: {variable_control}")
    variable_control -= 1

print("Bucle finalizado.\n")




# Ejemplo de error (comentado):
# print("\n--- 4. Ejemplo de error de inicialización (comentado) ---")
# while otra_variable < 10:  # Error: NameError (otra_variable no está definida)
#     print("Esto generará un error")
# print("Este código genera un error porque 'otra_variable' no fue inicializada.\n")

# 5. Uso de break:
print("\n--- 5. Uso de break ---")
i = 0
while i < 10:
    print(i)
    if i == 5:
        break  # Sale del bucle cuando i es 5
    i += 1

print("Salimos del bucle con 'break'.\n")





# 6. Uso de continue:
print("\n--- 6. Uso de continue ---")
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:  # Si x es par
        continue  # Salta a la siguiente iteración (no ejecuta el print de abajo)
    print(f"Número impar: {x}")

print("Bucle finalizado (con 'continue').\n")



# 7. while con else
print("\n--- 7. while con else ---")
num = 1
while num <= 5:
    print(f"Número: {num}")
    num += 1
else:  # Se ejecuta si el bucle termina normalmente (sin break)
    print("El bucle while ha terminado normalmente (sin 'break').")

print("\n--- 7. while con else y break ---")
n = 1
while n <= 5:
    print(f"n: {n}")
    if n == 3:
        break # sale del bucle
    n += 1
else: # No se ejecuta porque el bucle se interrumpió con break
    print("Este mensaje NO se imprimirá porque se usó 'break'.")
print("Fin del ejemplo con 'break'\n")

print("\n--- FIN DE LA GUÍA ---\n")
