import re

# Expresiones Regulares (Regex):
#
# Las expresiones regulares son secuencias de caracteres que forman un patrón de búsqueda.
# Se utilizan para encontrar, manipular o validar cadenas de texto que cumplen con un
# cierto formato. En Python, el módulo 're' proporciona las herramientas para trabajar
# con expresiones regulares.

texto = '''Hola maestro. esta es la cadena 1, como estás mi capitan
Esta es la segunda linea de texto.
y Esta es la final definitiva mi capitan.'''

print(f"Texto original:\n{texto}")

# Búsqueda simple de la palabra "Esta"
resultado = re.findall("Esta", texto)
print(f"\nBúsqueda simple de 'Esta': {resultado}")
# 'findall' regresa una lista con TODAS las coincidencias encontradas.


# Metacaracteres y Secuencias especiales:


# \d => Busca dígitos numéricos del 0 al 9
resultado = re.findall(r'\d', texto)
print(f"Dígitos numéricos en la cadena: {resultado}")
# Encuentra el número "1" en la cadena.



# \D => Busca todo MENOS dígitos numéricos
resultado = re.findall(r'\D', texto)
print(f"Caracteres NO numéricos (longitud: {len(resultado)}). Ejemplo: '{resultado[:10]}...'")
# Incluye letras, espacios, puntuación, saltos de línea, etc.



# \w => Busca caracteres alfanuméricos [a-z A-Z 0-9 _]
resultado = re.findall(r'\w', texto)
print(f"Caracteres alfanuméricos (longitud: {len(resultado)}). Ejemplo: '{resultado[:10]}...'")
# Incluye letras (mayúsculas y minúsculas), números y el guión bajo.


# \W => Busca todo MENOS caracteres alfanuméricos
resultado = re.findall(r'\W', texto)
print(f"Caracteres NO alfanuméricos (longitud: {len(resultado)}). Ejemplo: '{resultado[:10]}...'")
# Incluye espacios, puntuación, caracteres especiales, etc.




# \s => Busca espacios en blanco: espacios, tabs, saltos de línea
resultado = re.findall(r'\s', texto)
print(f"Espacios en blanco (longitud: {len(resultado)}): {resultado}")
# Muestra los espacios, tabulaciones y saltos de línea encontrados.



# \S => Busca todo MENOS espacios en blanco
resultado = re.findall(r'\S', texto)
print(f"Caracteres NO espacios en blanco (longitud: {len(resultado)}). Ejemplo: '{resultado[:10]}...'")




# . => Busca TODO MENOS saltos de línea (\n)
resultado = re.findall(r'.', texto)
print(f"Todos los caracteres EXCEPTO saltos de línea (longitud: {len(resultado)}). Ejemplo: '{resultado[:20]}...'")
# El punto coincide con casi cualquier carácter, excepto el salto de línea.




# \n => Busca saltos de línea
resultado = re.findall(r'\n', texto)
print(f"Saltos de línea (longitud: {len(resultado)}): {resultado}")




# \. => Cancela el carácter especial del punto. Busca puntos literales.
resultado = re.findall(r'\.', texto)
print(f"Puntos literales: {resultado}")
# La barra invertida "\" se utiliza para "escapar" caracteres especiales,
# permitiendo buscarlos de forma literal.




# Ejemplo de busqueda de palabras que terminan en "an" usando word boundary
resultado = re.findall(r"\w+an\b", texto)
print(f"Palabras que terminan en 'an': {resultado}")
# \w+ busca uno o más caracteres alfanuméricos.
# \b es un "anchor" que indica un límite de palabra (word boundary). Asegura que "an" esté al final de una palabra completa, no dentro de otra palabra como "banana".




# Ejemplo de busqueda de palabras que contienen "es"
resultado = re.findall(r"\bes\w*", texto)
print(f"Palabras que comienzan con 'es': {resultado}")
# \w* busca cero o más caracteres alfanuméricos.