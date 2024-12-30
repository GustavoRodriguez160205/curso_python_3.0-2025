

# --------------------------------------------------
# OPERADORES ARITMÉTICOS
# --------------------------------------------------

print("\n--- OPERADORES ARITMÉTICOS ---\n")

num1 = 12
num2 = 5
num3 = 4

print(f"{num1} + {num2} = {num1 + num2}  # Suma: {num1} más {num2}")
print(f"{num1} - {num3} = {num1 - num3}  # Resta: {num1} menos {num3}")
print(f"{num1} * {num2} = {num1 * num2}  # Multiplicación: {num1} por {num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}  # División: {num1} entre {num2} (resultado decimal)")
print(f"{num1} // {num2} = {num1 // num2}  # División entera: Cociente de {num1} entre {num2}")
print(f"{num1} % {num3} = {num1 % num3}  # Módulo (resto): Residuo de {num1} entre {num3}")
print(f"{num1} ** {num2} = {num1 ** num2}  # Potencia: {num1} elevado a la {num2}")

print("\n--------------------------------------------------\n")

# --------------------------------------------------
# OPERADORES DE COMPARACIÓN
# --------------------------------------------------

print("\n--- OPERADORES DE COMPARACIÓN ---\n")

print("3 > 4:", 3 > 4, " # Mayor que: ¿3 es mayor que 4?")
print("3 < 4:", 3 < 4, " # Menor que: ¿3 es menor que 4?")
print("3 >= 4:", 3 >= 4, " # Mayor o igual que: ¿3 es mayor o igual que 4?")
print("4 <= 4:", 4 <= 4, " # Menor o igual que: ¿4 es menor o igual que 4?")
print("3 == 4:", 3 == 4, " # Igualdad: ¿3 es igual a 4?")
print("3 != 4:", 3 != 4, " # Desigualdad: ¿3 es diferente de 4?")

print("\n--- Otros ejemplos de comparación ---\n")

print('"apple" < "banana":', "apple" < "banana", " # Cadenas: Orden alfabético")
print('[1, 2, 3] == [1, 2, 3]:', [1, 2, 3] == [1, 2, 3], " # Listas: Comparación elemento a elemento")
print('3.5 > 2.5:', 3.5 > 2.5, " # Flotantes: Comparación numérica")
print('True == 1:', True == 1, " # Booleanos: True es 1, False es 0")

print("\n--- Comparación de cadenas (ejemplo de usuario) ---\n")

usuarios_bd = "Gustavo12"
usuario_tipeado = "Gusta"
print(f'"{usuarios_bd}" == "{usuario_tipeado}": {usuarios_bd == usuario_tipeado} # No coinciden')

usuario_tipeado = "Gustavo12"
print(f'"{usuarios_bd}" == "{usuario_tipeado}": {usuarios_bd == usuario_tipeado} # Coinciden')

print("\n--------------------------------------------------\n")

# --------------------------------------------------
# OPERADORES LÓGICOS
# --------------------------------------------------

print("\n--- OPERADORES LÓGICOS ---\n")

print("--- AND (y) ---")
print("True and True:", True and True, " # Ambas verdaderas")
print("False and True:", False and True, " # Una falsa")
print("True and False:", True and False, " # Una falsa")
print("False and False:", False and False, " # Ambas falsas")

print("\n--- OR (o) ---")
print("True or True:", True or True, " # Al menos una verdadera")
print("False or True:", False or True, " # Al menos una verdadera")
print("True or False:", True or False, " # Al menos una verdadera")
print("False or False:", False or False, " # Ambas falsas")

print("\n--- NOT (no) ---")
print("not True:", not True, " # Invierte True a False")
print("not False:", not False, " # Invierte False a True")

print("\n--------------------------------------------------\n")