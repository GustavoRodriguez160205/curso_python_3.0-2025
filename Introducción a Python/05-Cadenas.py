# Guía de Métodos de Cadenas en Python
# ====================================

# Crear una cadena de ejemplo
cadena = "Hola Mundo"

# Modificar cadenas
print("Minúsculas:", cadena.lower())          # "hola mundo"
print("Mayúsculas:", cadena.upper())          # "HOLA MUNDO"
print("Primera letra mayúscula:", cadena.capitalize())     # "Hola mundo"
print("Cada palabra mayúscula inicial:", cadena.title())          # "Hola Mundo"
print("Invierte mayúsculas/minúsculas:", cadena.swapcase())       # "hOLA mUNDO"
print("Elimina espacios al inicio y al final:", cadena.strip())          # "Hola Mundo"
print("Reemplaza 'a' por 'e':", cadena.replace("a", "e"))  # "Helo Mundo"

# Propiedades de las cadenas
print("Inicia con 'Hola':", cadena.startswith("Hola"))  # True
print("Termina con 'Mundo':", cadena.endswith("Mundo"))    # True
print("Todo en minúsculas:", cadena.islower())            # False
print("Todo en mayúsculas:", cadena.isupper())            # False
print("Cada palabra inicia con mayúscula:", cadena.istitle())            # True
print("Solo letras:", cadena.isalpha())            # False
print("Solo números:", cadena.isdigit())            # False
print("Letras y/o dígitos:", cadena.isalnum())            # False
print("Solo espacios:", cadena.isspace())            # False

# Dividir y unir cadenas
print("Dividir por espacios:", cadena.split())             # ["Hola", "Mundo"]
print("Unir con guiones:", "-".join(["Hola", "Mundo"]))  # "Hola-Mundo"
print("Particionar por espacio:", cadena.partition(" "))      # ("Hola", " ", "Mundo")

# Buscar y contar
print("Primera ocurrencia de 'o':", cadena.find("o"))           # 1
print("Última ocurrencia de 'o':", cadena.rfind("o"))          # 9
print("Cuenta ocurrencias de 'o':", cadena.count("o"))          # 2

# Ajustar formato
print("Centrar con guiones:", cadena.center(20, "-"))      # "----Hola Mundo-----"
print("Alinear izquierda:", cadena.ljust(20, "-"))       # "Hola Mundo---------"
print("Alinear derecha:", cadena.rjust(20, "-"))       # "---------Hola Mundo"
print("Rellenar con ceros:", cadena.zfill(15))            # "00000Hola Mundo"

# Codificar y decodificar
print("Codifica en bytes:", cadena.encode("utf-8"))      # b"Hola Mundo"
print("Decodifica bytes:", b"Hola Mundo".decode("utf-8"))  # "Hola Mundo"

# Otros métodos
print("Minúsculas más agresivas:", cadena.casefold())          # "hola mundo"
print("Formato personalizado:", "{0} tiene {1} años".format("Juan", 30))  # "Juan tiene 30 años"
