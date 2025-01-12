# Falto el profesor y los pibes van a armar la clase
# Pedimos el nombre y la edad de los compñaeros que vinieron hoy a clase

def obtener_compñaeros(cantidad_de_compñaeros):
    compañeros = []
    # Bucle que se ejecutara 5 veces hasta que llege a 5
    for i in range(cantidad_de_compñaeros):

        # Pedimos los datos
        nombre = input(" Ingrese el nombre del compañero: ")
        edad = int(input(" Ingrese la edad del compañero: "))

        # Creamos la tupla
        compñaero = (nombre,edad) 
        # Agregamos a la lista
        compañeros.append(compñaero) 
    
    # Key es un parametro opcional, ordenamos de menor a mayor según edad.
    compañeros.sort(key = lambda x:x[1]) 

    # Compañero[x] devuelve una tupla (nombre,edad) , y después accedemos al nombre
    # para definir al asistenye y al profesor.

    asistente = compañeros[0][0] # [ (1,2), (1,2) , (1 , 2)]
    profesor = compañeros[-1][0]  

    return asistente , profesor


asistente,profesor = obtener_compñaeros(5)
print(f"El profesor es: {profesor} y su asistente es: {asistente}")