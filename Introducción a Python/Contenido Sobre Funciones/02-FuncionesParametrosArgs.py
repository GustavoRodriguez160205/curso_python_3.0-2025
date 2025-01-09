# Que son los *args?
# Te permiten pasar una cantidad variable de argumentos a una función,
# sin necesidad de definir cada uno individualmente.

# ¿Cómo funcionan?
# Se utiliza un asterisco (*) seguido de un nombre de variable, típicamente *args (pero puede ser cualquier nombre).
# Los argumentos se reciben como una tupla, lo que significa que puedes iterar sobre ellos.

####################

# Suma de números

def suma_numeros(*args):
    resultado = sum(args)
    print(f"La suma es: {resultado}")

# Ejemplos de uso
suma_numeros(1, 2, 3, 4, 5)  # La suma es: 15
suma_numeros(4, 10)          # La suma es: 14

######################

# Encontrar el número máximo

def encontrar_maximo(*args):
    return max(args)

maximo = encontrar_maximo(10,5,12,33)
print(f"El número máximo es: {maximo}")

#######################

# Forma no optima de Sumar valores

def suma_no_optima(lista):
    numeros_sumados = 0 # Se almacenara el resultado de la suma.
    for numero in lista:
        numeros_sumados += numero # Se va acumulando el valor de cada número
    return numeros_sumados

resultado1 = suma_no_optima([5,3,9,10,20])
print(f"Resultado (no optimo): {resultado1}")

#########################

# Forma optima usando *Args

def suma_optima(nombre , *numeros):
    return f"{nombre}, la suma de tus números es: {sum(numeros)}"

resultado3 = suma_optima("Gustavo" , 5 , 3 , 6 , 7 , 8 )
print(f"Resultado (Optimo): {resultado3}")