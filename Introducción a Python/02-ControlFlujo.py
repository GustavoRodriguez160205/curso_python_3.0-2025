

# --------------------------------------------------
# CONDICIONALES (if)
# --------------------------------------------------

print("\n--- CONDICIONALES (if) ---\n")

# Los condicionales 'if' permiten ejecutar un bloque de código solo si una condición es verdadera (True).

edad = 18

print(f"Edad: {edad}")

if edad >= 18:
    print("Podes pasar. # Se ejecuta porque la edad es mayor o igual a 18.")
else:
    print("No podes pasar. # No se ejecuta en este caso.")

print("Esta línea se ejecuta siempre, independientemente de la condición.")

print("\n--------------------------------------------------\n")

# --------------------------------------------------
# CONDICIONALES (if, elif, else)
# --------------------------------------------------

print("\n--- CONDICIONALES (if, elif, else) ---\n")

# 'elif' (else if) se utiliza para evaluar múltiples condiciones en secuencia.
# Solo se ejecuta el bloque de código correspondiente a la PRIMERA condición verdadera.
# 'else' se ejecuta si NINGUNA de las condiciones anteriores es verdadera.

ingresoMensual = 80500
gastoMensual = 20000

print(f"Ingreso mensual: {ingresoMensual}")
print(f"Gasto mensual: {gastoMensual}")

if ingresoMensual > 10000:
    print("\n--- Ingreso mayor a 10000 ---") 
    if ingresoMensual - gastoMensual < 0:
        print("Estás en déficit. # Ingresos menores a gastos.")
    elif ingresoMensual - gastoMensual > 3000:
        print("Estás bien pa. # Ingresos significativamente mayores a gastos.")
    else:
        print("Estás gastando mucho. # Ingresos mayores a gastos, pero no significativamente.")

elif ingresoMensual > 1000:
    print("Estás bien en Latinoamérica. # Ingresos entre 1000 y 10000.")

elif ingresoMensual > 500:
    print("Estás bien en Argentina. # Ingresos entre 500 y 1000.")

elif ingresoMensual > 200:
    print("Estás bien en Venezuela. # Ingresos entre 200 y 500.")

else:
    print("Sos pobre. # Ingresos menores a 200.")

print("\n--------------------------------------------------\n")