# Solicitar al usuario una frase para calcular el tiempo que tomaría decirla
frase = input("Decime una frase y te calculo cuánto tardarías en decirla: ")

# Dividir la frase en palabras y contar la cantidad total
pal_separadas = frase.split(" ")  # Divide la frase en una lista de palabras
cant_palabras = len(pal_separadas)  # Calcula el número total de palabras

# Calcular el tiempo estimado para decir la frase
tiempo_usuario = cant_palabras / 2  # Asumiendo que el usuario dice 2 palabras por segundo
tiempo_dalto = cant_palabras * 100 // 2 * 1.3 / 100  # Velocidad estimada de Dalto (30% más rápido)

# Mostrar resultados al usuario
print(f"Dijiste {cant_palabras} palabras, y tardarías {tiempo_usuario:.2f} segundos en decirlo.")
print(f"Dalto lo diría en: {tiempo_dalto:.2f} segundos.")

# Validar si el número de palabras supera un límite razonable
if cant_palabras > 120:
    print("¡Pará, no te pedí un testamento!")
