# Métodos de Cadenas en Python (Enfoque en Métodos Solicitados)

cadena1 = "Hola,Maquina,Como,Estas"
cadena2 = "Bienvenido maquinola"
cadena3 = "12345"


####################################################


print("\n--- Métodos de Conversión ---")

# upper(): Convierte la cadena a mayúsculas.
mayusc = cadena1.upper()
print(f"cadena1.upper(): '{cadena1}' -> '{mayusc}'")


# lower(): Convierte la cadena a minúsculas.
minusc = cadena1.lower()
print(f"cadena1.lower(): '{cadena1}' -> '{minusc}'")


# capitalize(): Convierte el primer carácter a mayúscula y el resto a minúsculas.
primer_letra_mayusc = cadena1.capitalize()
print(f"cadena1.capitalize(): '{cadena1}' -> '{primer_letra_mayusc}'")




###############################################################################################


print("\n--- Métodos de Búsqueda ---")

# find(): Busca una subcadena. Devuelve el índice de la primera ocurrencia o -1 si no la encuentra.
busqueda_find = cadena1.find("Como")
print(f"cadena1.find('Como'): '{cadena1}'.find('Como') -> {busqueda_find}")

busqueda_find_no_existe = cadena1.find("Z")
print(f"cadena1.find('Z'): '{cadena1}'.find('Z') -> {busqueda_find_no_existe}")


# index(): Busca una subcadena. Devuelve el índice de la primera ocurrencia. Lanza ValueError si no la encuentra.
try:
    busqueda_index = cadena1.index("H")
    print(f"cadena1.index('H'): '{cadena1}'.index('H') -> {busqueda_index}")
    # Imprime: cadena1.index('H'): 'Hola,Maquina,Como,Estas'.index('H') -> 0
    busqueda_index_error = cadena1.index("Z")  # Esto lanza una excepción
    print(f"cadena1.index('Z'): '{cadena1}'.index('Z') -> {busqueda_index_error}") # Esta línea no se ejecuta si hay error
except ValueError as e:
    print(f"Error (ValueError): {e}")
    # Imprime: Error (ValueError): substring not found


###################################################################################################


print("\n--- Métodos de Verificación ---")

# isnumeric(): Devuelve True si todos los caracteres son numéricos.
es_numerico = cadena1.isnumeric()
print(f"cadena1.isnumeric(): '{cadena1}'.isnumeric() -> {es_numerico}")



es_numerico_cadena3 = cadena3.isnumeric()
print(f"cadena3.isnumeric(): '{cadena3}'.isnumeric() -> {es_numerico_cadena3}")


# isalpha(): Devuelve True si todos los caracteres son alfabéticos.
es_alfanumerico = cadena1.isalpha()
print(f"cadena1.isalpha(): '{cadena1}'.isalpha() -> {es_alfanumerico}")





##########################################################################


print("\n--- Métodos de Conteo y Longitud ---")

# count(): Cuenta las coincidencias de una subcadena dentro de otra.
contar_coincidencias = cadena1.count("ma") # Cuenta "ma" en minuscula
print(f"cadena1.count('ma'): '{cadena1}'.count('ma') -> {contar_coincidencias}")


# len(): Cuenta cuántos caracteres tiene una cadena.
contar_caracteres = len(cadena1)
print(f"len(cadena1): len('{cadena1}') -> {contar_caracteres}")




#######################################################3


print("\n--- Métodos de Verificación (Inicio/Fin) ---")

# startswith(): Verifica si una cadena empieza con otra cadena dada.
empieza_con = cadena1.startswith("H")
print(f"cadena1.startswith('H'): '{cadena1}'.startswith('H') -> {empieza_con}")



# endswith(): Verifica si una cadena termina con otra cadena dada.
termina_con = cadena1.endswith("s")
print(f"cadena1.endswith('s'): '{cadena1}'.endswith('s') -> {termina_con}")





####################################################################


print("\n--- Métodos de Reemplazo y Separación ---")

# replace(): Reemplaza todas las ocurrencias de una subcadena por otra.
cadena_nueva = cadena1.replace(",", " ")
print(f"cadena1.replace(',', ' '): '{cadena1}'.replace(',', ' ') -> '{cadena_nueva}'")



# split(): Separa una cadena en una lista de subcadenas usando un delimitador.
cadena_separada = cadena1.split(",")
print(f"cadena1.split(','): '{cadena1}'.split(',') -> {cadena_separada}")
print(f"Primer elemento de la lista: cadena_separada[0] -> '{cadena_separada[0]}'")
