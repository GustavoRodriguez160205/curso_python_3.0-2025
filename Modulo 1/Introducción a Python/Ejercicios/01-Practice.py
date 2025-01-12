# Duración de los cursos (en horas)
dalto_curso = 1.5          # Duración del curso de Dalto
otros_cursos_min = 2.5     # Curso más corto de la competencia
otros_cursos_max = 7       # Curso más largo de la competencia
otros_cursos_promedio = 4  # Duración promedio de otros cursos

# Ejercicio A: Comparación de duración entre cursos
# Cálculo de diferencias de duración en porcentaje
dif_min = (1 - dalto_curso / otros_cursos_min) * 100
dif_max = (1 - dalto_curso / otros_cursos_max) * 100
promedio_dif = (1 - dalto_curso / otros_cursos_promedio) * 100


print("-- -- -- -- -- -- --")
print("Comparativa de duración del curso de Dalto:")
print(f"  - {dif_min:.2f}% menos que el más rápido.")
print(f"  - {dif_max:.2f}% menos que el más lento.")
print(f"  - {promedio_dif:.2f}% menos que el promedio.")
print("-- -- -- -- -- -- --")



# Ejercicio B: Comparación de tiempo vacío eliminado
# Tiempo total de grabación de los cursos (horas)
crudo_promedio = 5         # Duración promedio del material bruto
crudo_dalto = 3.5          # Duración del material bruto del curso de Dalto

# Cálculo del porcentaje de tiempo vacío eliminado
tiempo_vacio_prom = 100 - (otros_cursos_promedio / crudo_promedio) * 100
tiempo_dalto = 100 - (dalto_curso / crudo_dalto) * 100


print("Porcentaje de tiempo vacío eliminado:")
print(f"  - Un curso promedio elimina un {tiempo_vacio_prom:.2f}% de tiempo vacío.")
print(f"  - El curso de Dalto elimina un {tiempo_dalto:.2f}% de tiempo vacío.")
print("-- -- -- -- -- -- --")



# Ejercicio C: Comparación de horas vistas
# Cálculo de equivalencias entre cursos
equivalente_otro_curso = 10 * otros_cursos_promedio / dalto_curso
equivalente_dalto_curso = 10 * dalto_curso / otros_cursos_promedio


print("Equivalencias de horas vistas:")
print(f"  - Ver 10 horas del curso de Dalto equivale a {equivalente_otro_curso:.2f} horas de otros cursos.")
print(f"  - Ver 10 horas de otros cursos equivale a {equivalente_dalto_curso:.2f} horas del curso de Dalto.")
print("-- -- -- -- -- -- --")
