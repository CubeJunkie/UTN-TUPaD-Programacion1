# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se importa la funcion requerida desde el modulo de saludos del proyecto
from auxiliar.saludos import informacion_persona

# Se muestra en pantalla el encabezado
print('\n---EJERCICIO N.º 3 - Presentación con datos personales---')

# INGRESO DE NOMBRE
# Se hace un llamado a la función definida para ingresar strings no vacíos
nombre = ing.string_no_vacio('Nombre')

# INGRESO DE APELLIDO
# Se hace un llamado a la función definida para ingresar strings no vacíos
apellido = ing.string_no_vacio('Apellido')

# INGRESO DE EDAD
# Se hace un llamado a la función definida para ingresar enteros mayores o iguales que cero
edad = ing.int_positivo_o_cero('Edad')

# INGRESO DE LUGAR DE RESIDENCIA
# Se hace un llamado a la función definida para ingresar strings no vacíos
residencia = ing.string_no_vacio('Lugar de residencia')

print('---------------------------')

# Se hace un llamado a la función informacion_persona()
informacion_persona(nombre, apellido, edad, residencia)

print('')