# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se declara un diccionario para almacenar nombres y notas de alumnos
alumnos = {}

# Se le pide al usuario ingresar los nombres y notas de 3 alumnos, para agregarlo a un diccionario
for i in range(3):
    print(f'---Alumno N.º {i + 1}---')
    string_nombre = ing.string_alpha_espacios('Nombre')
    nota_1 = ing.float_cero_a_diez('Nota 1')
    nota_2 = ing.float_cero_a_diez('Nota 2')
    nota_3 = ing.float_cero_a_diez('Nota 3')
    # Se crea una tupla con las 3 notas
    tupla_notas = (nota_1, nota_2, nota_3)
    # Se añade el par nombre-tupla al diccionario
    alumnos[string_nombre] = tupla_notas

# Se muestra el diccionario en pantalla
print('------------------------------')
print('REGISTRO DE NOTAS')
print(alumnos)
print('------------------------------')

# Se recorre el diccionario con un lazo for y el método .items()
for nombre, notas in alumnos.items():
    # Se calcula el promedio para cada alumno
    promedio = sum(notas) / len(notas)
    print(f'Nombre: {nombre}\tPromedio: {promedio}')