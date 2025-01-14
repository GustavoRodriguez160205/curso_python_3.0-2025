# 01. Sumar dos números
# Pide al usuario que ingrese dos números y muestra la suma.

numero1 = int(input("Ingresa un número:"))
numero2 = int(input("Ingresa un número:"))
print(f"La suma es: {numero1 + numero2}")



# 02. Mayor de dos números
# Pide dos números y muestra cuál es mayor o si son iguales.

numero1 = int(input("Dame un número: "))
numero2 = int(input("Dame otro número: "))

if numero1 > numero2:
    print(f"El primer número es mayor: {numero1}")
elif numero1 == numero2:
    print("Los núemros son iguales.")

else:
    print("No se ingresaron números.")


# 03. Par o impar
# Pide un número y muestra si es par o impar.


numero1 = int(input("Dame un número y te diré si es par o no: "))
es_par = lambda x: x % 2 == 0 
print(f"Es número par?: {es_par(numero1)}") 




# 04. Conversor de temperatura
# Convierte una temperatura de Celsius a Fahrenheit.

numero1 = float(input("Ingresa una temperatura en Celsius y la convertiremos a Fahrenheit: "))
conversion = (numero1 * 9/5) + 32
print(f"La temperatura en Fahrenheit es: {conversion}")




# 05. Número positivo o negativo
# Pide un número y muestra si es positivo, negativo o cero.

numero1 = int(input(" Decime un número y te dire si es positivo , negativo o cero. "))

if numero1 > 0:
    print("El número es positivo.")

elif numero1 < 0:
    print("El número es negativo.")

elif numero1 == 0:
    print("El número es neutro.")

else:
    print("Se termino.")