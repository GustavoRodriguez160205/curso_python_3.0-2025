

# 1. Declara una variable llamada 'nombre' y asígnale tu nombre. Luego, imprime un saludo personalizado usando esta variable.
nombre = "Gustavo"
print(f"Hola, ¿cómo estás, {nombre}?")


# 2. Calcula el área de un triángulo. Solicita al usuario que ingrese la base y la altura, y utiliza la fórmula: área = (base * altura) / 2.
base = float(input("Ingresa la base del triángulo para calcular su área: "))
altura = float(input("Ingresa la altura del triángulo para calcular su área: "))
calculo = (base * altura) / 2
print(f"El área del triángulo es: {calculo}")



# 3. Escribe un programa que solicite al usuario tres números y calcule la media aritmética de esos números.  
# Pista: La media aritmética se calcula como: (n1 + n2 + n3) / 3.
n1 = int(input("Dame el primer número: "))
n2 = int(input("Dame el segundo número: "))
n3 = int(input("Dame el tercer número: "))
resultado = (n1 + n2 + n3) / 3
print(f"La media aritmética de los números es: {resultado}")


# 4. Crea una variable frase que contenga una oración. Declara otra variable que cuente cuántos espacios hay en esa frase usando el método count().
frase =     "Hola a todos como andan  . Aguante Milei carajooo    "
contarEspacios = frase.count("  ")
print(f"Los espacios que hay en esta frase son: {contarEspacios}")



# 5. Calcula el área de un círculo con un radio dado por el usuario.
# Pista: Usa la fórmula área = π * r^2 (usa 3.1416 para π).
radio = float(input("Por favor dame el radio del círculo: "))
pi = 3.1416

area = pi * radio ** 2
print(f"El área de un círculo con radio {radio} es: {area:.2f}")


