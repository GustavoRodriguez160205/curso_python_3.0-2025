# Guía de Métodos de Cadenas en Python
# ====================================

# Crear una cadena de ejemplo
cadena = "Hola Mundo"



# 1. Modificar cadenas
print(cadena.lower())          # Minúsculas: "hola mundo"
print(cadena.upper())          # Mayúsculas: "HOLA MUNDO"
print(cadena.capitalize())     # Primera letra mayúscula: "Hola mundo"
print(cadena.title())          # Cada palabra mayúscula inicial: "Hola Mundo"
print(cadena.swapcase())       # Invierte mayúsculas/minúsculas: "hOLA mUNDO"
print(cadena.strip())          # Elimina espacios al inicio y al final
print(cadena.replace("a", "e"))  # Reemplaza "a" por "e": "Helo Mundo"



# 2. Propiedades de las cadenas
print(cadena.startswith("Hola"))  # Verifica si inicia con "Hola": True
print(cadena.endswith("Mundo"))    # Verifica si termina con "Mundo": True
print(cadena.islower())            # Minúsculas: False
print(cadena.isupper())            # Mayúsculas: False
print(cadena.istitle())            # Cada palabra inicia con mayúscula: True
print(cadena.isalpha())            # Solo letras: False
print(cadena.isdigit())            # Solo números: False
print(cadena.isalnum())            # Letras y/o dígitos: False
print(cadena.isspace())            # Solo espacios: False



# 3. Dividir y unir cadenas
print(cadena.split())             # Divide por espacios: ["Hola", "Mundo"]
print("-".join(["Hola", "Mundo"]))  # Une con guiones: "Hola-Mundo"
print(cadena.partition(" "))      # Divide en 3 partes: ("Hola", " ", "Mundo")

# 4. Buscar y contar
print(cadena.find("o"))           # Primera ocurrencia de "o": 1
print(cadena.rfind("o"))          # Última ocurrencia de "o": 9
print(cadena.count("o"))          # Cuenta ocurrencias de "o": 2

# 5. Ajustar formato
print(cadena.center(20, "-"))      # Centrar: "----Hola Mundo-----"
print(cadena.ljust(20, "-"))       # Alinear izquierda: "Hola Mundo---------"
print(cadena.rjust(20, "-"))       # Alinear derecha: "---------Hola Mundo"
print(cadena.zfill(15))            # Rellenar con ceros: "00000Hola Mundo"

# 6. Codificar y decodificar
print(cadena.encode("utf-8"))      # Codifica en bytes
print(b"Hola Mundo".decode("utf-8"))  # Decodifica bytes a cadena

# 7. Otros métodos
print(cadena.casefold())          # Minúsculas más agresivas
print("{0} tiene {1} años".format("Juan", 30))  # Formato: "Juan tiene 30 años"