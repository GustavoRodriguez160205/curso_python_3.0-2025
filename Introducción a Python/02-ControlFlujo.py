###################################################

## ESTRUCTURAS DE CONTROL DE FLUJO

###################################################


## 01 - CONDICIONALES



# - Son estructuras de código que permiten tomar decisiones basadas en ciertas condiciones.
# - Si una condición se cumple (es `True`), se ejecuta un bloque de código específico.
# - Si la condición es `False`, ese bloque no se ejecuta (aunque puede haber un bloque alternativo que sí lo haga, como con `else`).


edad = 18

if edad >= 18:
    print("Podes pasar.")  

else:
    print("No podes pasar.")  


print("No forma parte de ninguna condición.")


## B ) ELSE - IF

# Los 'elif' (abreviatura de "else if") son condiciones adicionales que se evalúan después de un 'if'. 
# Permiten agregar múltiples escenarios dentro de una estructura condicional, ejecutando solo el bloque correspondiente 
# a la primera condición verdadera encontrada.

ingresoMensual = 80500
gastoMensual = 20000


if ingresoMensual > 10000:
    if ingresoMensual - gastoMensual < 0:
        print("Estás en deficit") 
    elif ingresoMensual - gastoMensual > 3000: 
        print("Estás bien pa.")  
    else:
        print("Estás gastando mucho")  

elif ingresoMensual > 1000:  
    print("Estás bien en latinoamérica.")  


elif ingresoMensual > 500:  
    print("Estás bien en Argentina.")  


elif ingresoMensual > 200:  
    print("Estás bien en Venezuela.") 


else:
    print("Sos pobre.")



#########################################################


#########################################################


#########################################################


# 02 - BUCLE FOR