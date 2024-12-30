
# -------------------------------------------------
# MÉTODOS DE CADENAS
# --------------------------------------------------


print("\n--- MÉTODOS DE CADENAS (ejemplos concisos) ---\n")

cadena = "Hola Mundo Python"  
print(f"Cadena: '{cadena}'\n")

# 1. upper(): Convierte a mayúsculas.
print(f"cadena.upper(): '{cadena.upper()}'")

# 2. lower(): Convierte a minúsculas.
print(f"cadena.lower(): '{cadena.lower()}'")

# 3. capitalize(): Primera a maýusculas.
print(f"cadena.capitalize(): '{cadena.capitalize()}'")

# 4. find(): Busqueda una cadena, devuelve la posición. 
# - Si no existe nos da -1.
# - Los espacios también cuentan.
print(f"cadena.find():'{cadena.find("Hola")}'")


# 5. index(): Es igual al metodo (4)
# - Si no existe nos tira una excepción.

print(f"cadena.index(): '{cadena.index("n")}'")