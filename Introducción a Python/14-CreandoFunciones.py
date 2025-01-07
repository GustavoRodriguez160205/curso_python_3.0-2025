# Teoría:
# Las funciones en Python se definen con 'def' y pueden recibir valores llamados parámetros.
# A continuación, se detallan tres tipos de funciones y su uso.

# 1. Función simple: No recibe parámetros y solo realiza una acción predeterminada.
def saludar():
    """
    Esta es una función simple. No recibe parámetros y solo imprime un mensaje de saludo.
    """
    print("Hola Pedro, mi maestro. ¿Cómo andas?")

# Llamada a la función 'saludar', que no necesita ningún valor.
saludar()


# 2. Función con parámetros: Recibe información de fuera de la función (argumentos) para hacer algo con ella.
# En este caso, 'nombre' y 'sexo' se pasan como parámetros para personalizar el saludo.

def saludar(nombre, sexo):
    """
    Esta función recibe dos parámetros: 'nombre' y 'sexo'. 
    Según el valor de 'sexo', se asigna un adjetivo personalizado al saludo.
    """
    # Según el sexo, asignamos un adjetivo adecuado
    if sexo == "Mujer":
        adjetivo = "Reina"
    elif sexo == "Hombre":
        adjetivo = "Titan"
    else:
        adjetivo = "Amor"
    
    # Imprime un saludo personalizado usando los parámetros proporcionados
    print(f"Hola {nombre}, mi {adjetivo}. ¿Cómo andas?")

# Llamada a la función 'saludar' con parámetros ('Camila' y 'Mujer')
saludar("Camila", "Mujer")


# 3. Función que retorna valores: Realiza una operación y devuelve un resultado para usarlo más adelante.
# En este caso, la función genera una contraseña aleatoria basada en el número que se pasa como parámetro.

def crear_random_password(num):
    """
    Esta función genera una contraseña aleatoria utilizando el primer dígito del número pasado como parámetro.
    La contraseña se forma utilizando una cadena de caracteres predefinidos.
    """
    # Cadena de caracteres posibles para la contraseña
    chars = "abcdefghijk"
    
    # Convertir el número a cadena y usar su primer dígito
    num_entero = str(num)
    num = int(num_entero[0])  # Toma el primer dígito del número
    
    # Calculamos índices para crear los caracteres de la contraseña
    c1 = num - 2
    c2 = num
    c3 = num - 5
    
    # Creamos la contraseña utilizando los índices calculados
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}"
    
    # Retornamos la contraseña generada
    return contraseña

# Llamada a la función y almacenaje del valor retornado en la variable 'password'
password = crear_random_password(63)
frase = f"Tu nueva contraseña es: {password}" 

# Imprimir la contraseña generada
print(frase)
