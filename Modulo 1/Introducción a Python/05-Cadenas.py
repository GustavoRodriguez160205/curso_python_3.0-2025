# Métodos de Cadenas en Python - Aprendizaje Interactivo

cadena_base = "Python es Genial"

# 1. Transformación básica
print("\n--- Transformación básica ---")
cadena_mayusculas = cadena_base.upper()
print(f"Original: {cadena_base}, Mayúsculas: {cadena_mayusculas}")

cadena_minusculas = cadena_base.lower()
print(f"Original: {cadena_base}, Minúsculas: {cadena_minusculas}")



# 2. Búsqueda y Conteo
print("\n--- Búsqueda y Conteo ---")
conteo_e = cadena_base.count("e")
print(f"Cantidad de 'e' en '{cadena_base}': {conteo_e}")

posicion_es = cadena_base.find("es")
print(f"Posición de 'es' en '{cadena_base}': {posicion_es} (Recuerda: -1 si no existe)")


# 3. Eliminación de espacios
print("\n--- Eliminación de espacios ---")
cadena_con_espacios = "   Hola Mundo   "
cadena_sin_espacios = cadena_con_espacios.strip()
print(f"Con espacios: '{cadena_con_espacios}', Sin espacios: '{cadena_sin_espacios}'")



# 4. División y Unión
print("\n--- División y Unión ---")
palabras = cadena_base.split() # Separa por espacios
print(f"Cadena dividida: {palabras}")

cadena_unida = "-".join(palabras) # Une con guiones
print(f"Cadena unida con guiones: {cadena_unida}")



# 5. Reemplazo
print("\n--- Reemplazo ---")
cadena_reemplazada = cadena_base.replace("Genial", "Fantástico")
print(f"Cadena original: {cadena_base}, Cadena reemplazada: {cadena_reemplazada}")




# 6. Formateo con f-strings (¡Muy importante!)
print("\n--- Formateo con f-strings ---")
nombre = "Ana"
edad = 25
mensaje = f"Hola {nombre}, tienes {edad} años. El año que viene tendrás {edad + 1}."
print(mensaje)


# 7. Otros métodos (para explorar)
print("\n--- Otros métodos (para explorar) ---")
# .casefold(), .isalnum(), .isalpha(), .isdigit(), .isspace(), .istitle(), .encode(), .maketrans(), .translate(), .partition(), .rpartition(), .removeprefix(), .removesuffix()
print("Explora estos métodos en la documentación oficial de Python.")

