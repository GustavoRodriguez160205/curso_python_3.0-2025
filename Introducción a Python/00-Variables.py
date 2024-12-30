## Variables

# Una variable es un espacio en memoria que se utiliza para almacenar datos.
# Las variables pueden cambiar su valor durante la ejecución del programa.
# Antes de utilizarlas, es necesario declararlas y asignarles un valor inicial.

# Ejemplo de declaración y definición de variables numéricas:
a = 5  # Asignamos el valor 5 a la variable 'a'.
b = 3  # Asignamos el valor 3 a la variable 'b'.
c = a + b  # Sumamos los valores de 'a' y 'b' y los almacenamos en 'c'.
print("La suma es:", c)

# Ejemplo de declaración y uso de una variable tipo string:
nombre = "Gustavo"  # Asignamos una cadena de texto a la variable 'nombre'.
print("El nombre es:", nombre)

# Ejemplo de modificación del valor de una variable numérica:
numero = 10  # Asignamos el valor inicial 10 a 'numero'.
# Utilizamos un operador de asignación compuesta para incrementar el valor de 'numero'.
numero += 5  # Esto suma 5 al valor actual de 'numero'.
numero += 5  # Repetimos el incremento sumando otros 5.
print(numero)

## ¿Qué es la concatenación?

# La concatenación es el proceso de unir dos o más cadenas de texto (strings).
# Cada carácter cuenta en la concatenación, incluidos los espacios.
# Para unir cadenas con variables que no son texto, como números o valores booleanos, es recomendable usar f-strings.


# Ejemplo de concatenación con f-strings:
nombre = "Gustavo"
bienvenida = f"Hola {nombre}, ¿cómo estás?"  # Usamos un f-string para incluir la variable 'nombre' en la cadena.
print(bienvenida)


# Ejemplo de concatenación con una variable booleana:
numero = True  # Asignamos un valor booleano a la variable 'numero'.
bienvenida = f"Hola {numero}, ¿cómo estás?"  # Convertimos el valor booleano a texto al concatenarlo.
print(bienvenida)

## Eliminación de variables

# Si deseamos eliminar una variable para que deje de estar definida, podemos usar la instrucción 'del'.
# Ejemplo:
# del bienvenida  # Elimina la variable 'bienvenida'.

## Uso de operadores de pertenencia en cadenas

# Los operadores de pertenencia ('in' y 'not in') permiten verificar si una subcadena está presente en otra cadena.
# Devuelven 'True' si la subcadena se encuentra, o 'False' si no está presente.

# Ejemplo de operador de pertenencia:
print("ola" in bienvenida) # En este caso da True
print("Gustavo" in bienvenida)  # Aca da False


## Convensión de Escritura de variables

nombre_completo = "Gustavo Rodriguez" # Se llama Snake-Case

nombreCompleto = "GustavoRodriguez" # Se llama camel-case