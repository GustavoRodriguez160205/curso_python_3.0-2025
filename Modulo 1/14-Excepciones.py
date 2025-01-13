"""
Guía completa sobre el manejo de excepciones en Python

Las excepciones son eventos que interrumpen el flujo normal de un programa Python.
Ocurren cuando el intérprete se encuentra con una situación que no puede manejar
directamente.

Esta guía cubre los siguientes temas:
1. Manejo básico de excepciones: try, except
2. Manejo de múltiples excepciones
3. El bloque else
4. El bloque finally
5. Excepciones comunes y sus ejemplos
"""

# 1. Manejo básico de excepciones: try, except
print("\n--- 1. Manejo básico de excepciones ---")
try:
    resultado = 10 / 0  # Esto causa un ZeroDivisionError
    print("Esto NO se imprimirá si hay una excepción")
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero.")

print("El programa continúa después del manejo de la excepción.")
# Explicación: Este ejemplo muestra el manejo básico de una excepción.
# Se intenta dividir 10 entre 0, lo cual genera un ZeroDivisionError.
# El bloque 'except' captura esta excepción y ejecuta el código dentro de él.


#####################################
#####################################
#####################################


# 2. Manejo de múltiples excepciones
print("\n--- 2. Manejo de múltiples excepciones ---")
try:
    x = int(input("Ingrese un número: "))
    resultado = 10 / x
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Entrada inválida. Debe ingresar un número entero.")
except Exception as e:  # Captura cualquier OTRA excepción
    print(f"Error inesperado: {e}")
else:
    print(f"El resultado es: {resultado}")

# Explicación: Este ejemplo maneja múltiples excepciones. Si el usuario
# ingresa algo que no es un número entero, se captura un ValueError. Si
# ingresa 0, se captura un ZeroDivisionError. 'Exception as e' captura
# cualquier otra excepción no prevista. El bloque 'else' se ejecuta solo si
# no hubo ninguna excepción.


#####################################
#####################################
#####################################


# 3. El bloque else
print("\n--- 3. El bloque else ---")
try:
    num = int(input("Ingrese un número positivo: "))
    if num < 0:
        raise ValueError("El número debe ser positivo.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Número válido.")

# Explicación: El bloque 'else' se ejecuta solo si el bloque 'try' se completa
# sin lanzar ninguna excepción. En este caso, si el usuario ingresa un número
# positivo, el mensaje "Número válido" se imprimirá.

#####################################
#####################################
#####################################


# 4. El bloque finally
print("\n--- 4. El bloque finally ---")
try:
    f = open("archivo_ejemplo.txt", "r")
    contenido = f.read()
    print(contenido)
except FileNotFoundError:
    print("Error: El archivo no se encontró.")
finally:
    try:
        f.close()
        print("Intentando cerrar el archivo (si fue abierto).")
    except NameError:
        print("El archivo no se abrio por lo tanto no se puede cerrar")

# Explicación: El bloque 'finally' se ejecuta siempre, independientemente de si
# se produce una excepción o no. Se utiliza para tareas de limpieza, como cerrar
# archivos. En este caso se implemento un try except dentro del finally para evitar un error en caso de que el archivo nunca se abra.

#####################################
#####################################
#####################################


# 5. Excepciones comunes y sus ejemplos
print("\n--- 5. Excepciones comunes y sus ejemplos ---")

# TypeError
print("\n--- TypeError ---")
try:
    resultado = 5 + "hola"
except TypeError:
    print("Error: No se puede sumar un entero y una cadena.")
# Explicación: TypeError ocurre cuando se intenta realizar una operación
# incompatible entre tipos de datos, como sumar un entero y una cadena.

# NameError
print("\n--- NameError ---")
try:
    print(variable_inexistente)
except NameError:
    print("Error: La variable no está definida.")
# Explicación: NameError ocurre cuando se intenta acceder a una variable que
# no ha sido definida previamente.

#####################################
#####################################
#####################################

# AttributeError
print("\n--- AttributeError ---")
try:
    lista = [1, 2, 3]
    lista.appendd(4)  # Intentando usar un método inexistente
except AttributeError:
    print("Error: El objeto no tiene ese atributo o método.")
# Explicación: AttributeError ocurre cuando se intenta acceder a un atributo o
# método que no existe en un objeto.

#####################################
#####################################
#####################################


# IndexError
print("\n--- IndexError ---")
try:
    lista = [1, 2, 3]
    print(lista[5])  # Índice fuera de rango
except IndexError:
    print("Error: Índice fuera de rango.")
# Explicación: IndexError ocurre cuando se intenta acceder a un índice que está
# fuera de los límites de una secuencia (lista, tupla, cadena).

#####################################
#####################################
#####################################

# KeyError
print("\n--- KeyError ---")
try:
    diccionario = {"a": 1, "b": 2}
    print(diccionario["c"])
except KeyError:
    print("Error: La clave no existe en el diccionario.")
# Explicación: KeyError ocurre cuando se intenta acceder a una clave que no
# existe en un diccionario.

# FileNotFoundError
print("\n--- FileNotFoundError ---")
try:
    with open("archivo_que_no_existe.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("Error: Archivo no encontrado.")
# Explicación: FileNotFoundError ocurre cuando se intenta abrir un archivo que
# no existe en la ubicación especificada.

#####################################
#####################################
#####################################

# KeyboardInterrupt
print("\n--- KeyboardInterrupt ---")
print("Intenta ejecutar este código en la terminal y presiona Ctrl+C:")
try:
    while True:
        pass  # Bucle infinito (simulación)
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")
# Explicación: KeyboardInterrupt ocurre cuando el usuario interrumpe la
# ejecución del programa con Ctrl+C (o la combinación de teclas equivalente).


#####################################
#####################################
#####################################



# OSError (ejemplo con PermissionError)
print("\n--- OSError (ejemplo con PermissionError) ---")
try:
    # Intenta crear un directorio en una ubicación donde no tienes permisos
    import os
    os.makedirs("/root/nuevo_directorio") #Esto fallara si no se ejecuta como root
except PermissionError:
    print("Error: Permiso denegado para crear el directorio.")
except OSError as e: #Captura otros errores de sistema
    print(f"Error del sistema operativo: {e}")
# Explicación: OSError es una excepción base para errores del sistema
# operativo. PermissionError es una subclase de OSError que ocurre cuando se
# intenta realizar una operación para la que no se tienen permisos, como crear
# un directorio en una ubicación restringida.