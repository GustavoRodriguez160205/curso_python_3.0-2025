# Guía Completa sobre Inputs en Python

# Definición:
# En Python, el *input* es una forma de interactuar con el usuario durante la ejecución de un programa.
# Se utiliza la función `input()` para recibir datos desde la consola. Por defecto, esta función devuelve 
# los datos como cadenas de texto (tipo `str`). Sin embargo, estos datos pueden ser convertidos a otros 
# tipos de datos según sea necesario, como enteros (`int`), flotantes (`float`), listas, etc. Además, 
# es posible manejar errores y validar entradas para asegurar que el programa funcione correctamente.




# 1. Input básico
nombre = input("¿Cuál es tu nombre? ")  # Siempre devuelve una cadena
print(f"Hola, {nombre}!")





# 2. Convertir tipo de dato
edad = int(input("¿Cuántos años tienes? "))  # Convertir a entero
print(f"Tendrás {edad + 1} años el próximo año.")





# 3. Input con flotantes
altura = float(input("¿Cuál es tu altura en metros? "))  # Convertir a flotante
print(f"Tu altura es {altura} metros.")




# 4. Validar datos ingresados
dato = input("Ingresa 'sí' o 'no': ").strip().lower()  # Normalizar el dato
if dato == "sí":
    print("Has ingresado afirmativo.")
elif dato == "no":
    print("Has ingresado negativo.")
else:
    print("Entrada no válida.")



# 5. Input múltiple en una línea
datos = input("Ingresa tu nombre, edad y ciudad separados por comas: ").split(",")
nombre, edad, ciudad = datos[0].strip(), int(datos[1].strip()), datos[2].strip()
print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")




# 6. Uso avanzado: Input en un bucle

while True:
    opcion = input("Ingresa una opción (salir para terminar): ").strip().lower()
    if opcion == "salir":
        print("Saliendo del programa...")
        break
    else:
        print(f"Opción seleccionada: {opcion}")




# 7. Input con listas
numeros = input("Ingresa números separados por espacios: ").split()
numeros = [int(num) for num in numeros]  # Convertir a una lista de enteros
print(f"Números ingresados: {numeros}")
print(f"Suma de los números: {sum(numeros)}")




# 8. Manejo de excepciones
try:
    numero = int(input("Ingresa un número entero: "))
    print(f"Has ingresado el número {numero}")
except ValueError:
    print("Error: Debes ingresar un número entero.")

