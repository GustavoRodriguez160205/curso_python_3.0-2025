# Condicionales en Python: if, elif, else

# 1. Sentencia if: ejecuta un bloque si la condición es VERDADERA
edad = 20
if edad >= 18:
    print("Mayor de edad")  # Se ejecuta si edad es >= 18






# 2. Sentencia else: ejecuta un bloque si la condición del if es FALSA
edad = 15
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")  # Se ejecuta si edad es < 18






# 3. Sentencia elif (else if): evalúa múltiples condiciones en secuencia
calificacion = 75
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Bueno")
elif calificacion >= 70:
    print("Aprobado")  # Se ejecuta porque 75 >= 70
else:
    print("Reprobado")





# 4. if anidados: un if dentro de otro para condiciones más complejas
edad = 25
tiene_licencia = True
if edad >= 18:
    print("Mayor de edad")
    if tiene_licencia:
        print("Con licencia")  # Se ejecuta si edad >= 18 Y tiene_licencia es True
    else:
        print("Sin licencia")
else:
    print("Menor de edad")

# Ejemplo complejo con if anidados y elif
nivel_agua = 5
if nivel_agua > 10:
    print("Peligro: Nivel muy alto")
elif nivel_agua > 5:
    print("Precaución: Nivel elevado")
    if nivel_agua > 7:
        print("Evacuar zona baja")
    else:
        print("Mantenerse alerta")
elif nivel_agua > 0:
    print("Nivel normal")  # Se ejecuta porque 5 > 0
else:
    print("Nivel bajo")

# Resumen de puntos clave:
# - Indentación (4 espacios) define los bloques de código.
# - Operadores de comparación: ==, !=, >, <, >=, <=
# - Operadores lógicos (para combinar condiciones): and, or, not
#   Ejemplo: if edad > 18 and tiene_licencia: ...