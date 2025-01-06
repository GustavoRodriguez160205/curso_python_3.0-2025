# Descripción:
# Los conjuntos en Python son colecciones desordenadas de elementos únicos, es decir, no pueden tener valores repetidos.
# Los conjuntos son mutables, lo que significa que podés agregar o eliminar elementos.
# Hay un tipo especial de conjunto llamado frozenset que no se puede modificar una vez creado.
# Además, se pueden hacer varias operaciones matemáticas como la unión, intersección y diferencia entre conjuntos.



# -----------------------------------------------
# 1. Creación de un conjunto básico

# Para crear un conjunto en Python usamos la función set().
# Los conjuntos no permiten elementos duplicados, por lo que si intentamos agregar un elemento repetido, Python lo ignorará.

conjunto = set([1, 2, 3, 4, 5])
print("Conjunto básico:", conjunto)




# -----------------------------------------------
# 2. Creación de un conjunto inmutable (frozenset)

# Si necesitamos un conjunto que no se pueda modificar, usamos frozenset.
# Es como un conjunto normal, pero con la diferencia de que no podemos agregar ni eliminar elementos después de crearlo.

conjunto_inmutable = frozenset([6, 7, 8])
print("Conjunto inmutable (frozenset):", conjunto_inmutable)




# -----------------------------------------------
# 3. Uso de frozenset dentro de un conjunto mutable

# Aunque un frozenset no se puede modificar, podemos usarlo dentro de un conjunto común (mutable).
# Esto es posible porque los frozensets son inmutables, por lo que pueden estar dentro de otros conjuntos.

conjunto_con_frozen = {conjunto_inmutable, "Dato extra", 9}
print("Conjunto con frozenset dentro de un set:", conjunto_con_frozen)




# -----------------------------------------------
# 4. Operaciones de Conjuntos: Subconjunto, Superconjunto y Disjoint

# Ahora vamos a ver algunas operaciones que podemos hacer con conjuntos.

# Definimos dos conjuntos para trabajar.
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 5, 7, 9, 10}

# 4.1 Verificando si un conjunto es subconjunto de otro
# Un conjunto es subconjunto de otro si todos sus elementos están dentro del segundo conjunto.

es_subconjunto = conjunto1.issubset(conjunto2)
print("¿conjunto1 es subconjunto de conjunto2?", es_subconjunto)

# 4.2 Verificando si un conjunto es superconjunto de otro
# Un conjunto es superconjunto de otro si contiene todos los elementos del segundo conjunto (y puede tener más).

es_superconjunto = conjunto1.issuperset(conjunto2)
print("¿conjunto1 es superconjunto de conjunto2?", es_superconjunto)

# También podemos usar los operadores <= (subconjunto) y >= (superconjunto) para hacer las mismas verificaciones.

subconjunto_operador = conjunto1 <= conjunto2
superconjunto_operador = conjunto1 >= conjunto2

print("¿conjunto1 es subconjunto de conjunto2? (usando operador <=):", subconjunto_operador)
print("¿conjunto1 es superconjunto de conjunto2? (usando operador >=):", superconjunto_operador)

# 4.3 Verificando si los conjuntos no tienen elementos en común (Disjoint)
# Usamos la función isdisjoint para saber si dos conjuntos no tienen elementos en común.

no_comun = conjunto1.isdisjoint(conjunto2)  # Si retorna True, significa que no tienen elementos en común.
print("¿Los conjuntos conjunto1 y conjunto2 tienen elementos en común?", not no_comun)




# -----------------------------------------------
# 5. Otras operaciones comunes con conjuntos

# 5.1 Unión de conjuntos
# La unión de dos conjuntos combina todos sus elementos, pero sin duplicados.

union = conjunto1.union(conjunto2)  # O usando el operador |
print("Unión de conjunto1 y conjunto2:", union)

# 5.2 Intersección de conjuntos
# La intersección de dos conjuntos da como resultado un nuevo conjunto con los elementos comunes entre ellos.

interseccion = conjunto1.intersection(conjunto2)  # O usando el operador &
print("Intersección de conjunto1 y conjunto2:", interseccion)

# 5.3 Diferencia de conjuntos
# La diferencia de dos conjuntos da como resultado los elementos que están en el primer conjunto, pero no en el segundo.

diferencia = conjunto1.difference(conjunto2)  # O usando el operador -
print("Diferencia de conjunto1 y conjunto2 (conjunto1 - conjunto2):", diferencia)

# 5.4 Diferencia simétrica
# La diferencia simétrica nos da los elementos que están en uno u otro conjunto, pero no en ambos.

diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)  # O usando el operador ^
print("Diferencia simétrica de conjunto1 y conjunto2:", diferencia_simetrica)
