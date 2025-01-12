# Creando una función simple
def saludar():
    print("Hola Gustavo , como andas?")

# Ejecutando la función
saludar()

#######################################
#######################################
#######################################

# Creando una función que tenga parametros

# Un parámetro es una variable que se define en la declaración de una función 
# y que recibe un valor cuando la función es llamada. Los parámetros permiten 
# que una función trabaje con diferentes valores sin necesidad de cambiar su código.

def saludo(nombre, sexo):
    sexo = sexo.lower()  # Convertimos 'sexo' a minúsculas para hacer la comparación insensible a mayúsculas.

    # Usamos condicionales para asignar un adjetivo basado en el 'sexo'.
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "titan"
    else:
        adjetivo = 'amor'  # Este adjetivo se usa para cualquier otro caso, como 'no binario'.
    
    print(f"Hola {nombre}, mi {adjetivo} ¿Cómo andas?")

saludo("Pedro" , "Hombre")
saludo("Nacho" , "Hombre")

#######################################
#######################################
#######################################

# Creando una función que nos retorne valores

def generar_contraseña(num):
    caracteres = "abcdefghijk"
    numEntero = str(num)
    num = int(numEntero[0])
    
    c1 = num - 2
    c2 = num
    c3 = num - 5

    contraseña = f"{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}"
    return contraseña,num

# desempaquetamos la función
password , primer_num = generar_contraseña(981)
print(f"Tu contraseña nueva es: {password}")
print(f"El número utilizado para crearla fue: {primer_num}")


