# Métodos de Cadenas en Python - Explicación Completa

# Introducción:
# Las cadenas son secuencias de caracteres en Python. Son inmutables, lo que significa que no podemos modificar una cadena después de haberla creado, 
# pero podemos aplicar métodos que devuelven nuevas cadenas con modificaciones. 
# En este bloque vamos a ver los métodos más comunes para trabajar con cadenas de texto.

# 1. Transformación de texto
# Estos métodos permiten cambiar el formato del texto.

texto = "hola mundo"
print(texto.upper())       # Convierte todo a MAYÚSCULAS: "HOLA MUNDO"
print(texto.lower())       # Convierte todo a minúsculas: "hola mundo"
print(texto.capitalize())  # Pone la PRIMERA letra en mayúscula: "Hola mundo"
print(texto.title())       # Pone la primera letra de CADA palabra en mayúscula: "Hola Mundo"
print(texto.swapcase())    # Invierte mayúsculas y minúsculas: "HOLA MUNDO"

# 2. Espacios en blanco
# Estos métodos permiten manejar los espacios innecesarios al inicio y al final de una cadena.

texto_espacios = "   hola mundo   "
print(texto_espacios.strip())  # Quita espacios al inicio y al final: "hola mundo"
print(texto_espacios.lstrip()) # Quita espacios SOLO al inicio: "hola mundo   "
print(texto_espacios.rstrip()) # Quita espacios SOLO al final: "   hola mundo"

# 3. Búsqueda y reemplazo
# Estos métodos permiten buscar una subcadena dentro de una cadena y reemplazarla.

texto_buscar = "aprende python, python es genial"
print(texto_buscar.find("python"))  # Encuentra la primera aparición de "python": 8
print(texto_buscar.rfind("python")) # Encuentra la última aparición de "python": 17
print(texto_buscar.replace("python", "JavaScript"))  # Reemplaza todas las apariciones de "python" por "JavaScript": "aprende JavaScript, JavaScript es genial"

# 4. División y unión
# Estos métodos son útiles para dividir una cadena en partes o unir varias partes en una sola cadena.

texto_dividir = "manzana,pera,platano"
print(texto_dividir.split(","))  # Divide la cadena en una lista usando la coma como delimitador: ['manzana', 'pera', 'platano']
texto_unir = ["manzana", "pera", "platano"]
print(",".join(texto_unir))  # Une los elementos de la lista con una coma: "manzana,pera,platano"

# 5. Verificación
# Verificamos propiedades de la cadena, como si está formada solo por letras, si es alfanumérica, etc.

texto_verificar = "python123"
print(texto_verificar.isalpha())  # Devuelve True si solo tiene letras: False
print(texto_verificar.isdigit())  # Devuelve True si solo tiene dígitos: False
print(texto_verificar.isalnum())  # Devuelve True si es alfanumérica (letras y números): True
print(texto_verificar.islower())  # Devuelve True si todos los caracteres son minúsculas: True
print(texto_verificar.isupper())  # Devuelve True si todos los caracteres son mayúsculas: False

# 6. Otros métodos útiles
# - longitud de la cadena, verificar inicio o fin de la cadena.

texto_otro = "python"
print(len(texto_otro))       # Devuelve la longitud de la cadena: 6
print(texto_otro.startswith("py"))  # Devuelve True si la cadena comienza con "py": True
print(texto_otro.endswith("on"))    # Devuelve True si la cadena termina con "on": True

# 7. Formateo de cadenas
# Los métodos de formateo permiten insertar valores en una cadena de texto de manera más flexible.

nombre = "Gustavo"
edad = 20
print("Mi nombre es {} y tengo {} años.".format(nombre, edad))  # Formato clásico
print(f"Mi nombre es {nombre} y tengo {edad} años.")            # Usando f-strings (recomendado)

