# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se importa la función requerida desde el módulo de operaciones del proyecto
from calculos.operaciones import operaciones_basicas

# Se muestra en pantalla el encabezado
print('\n---EJERCICIO N.º 7 - Tupla de suma, resta, multiplicación y división.---')

# INGRESO DE NÚMEROS
# Se llama a la función definida para ingresar enteros mayores que cero
num_1 = ing.int_positivo('Entero positivo N.º 1')
num_2 = ing.int_positivo('Entero positivo N.º 2')

# Se hace un llamado a la función operaciones_basicas() para obtener la tupla
tupla = operaciones_basicas(num_1, num_2)

print('---------------------------')

# Se muestra la tupla en pantalla
print(f'Tupla con suma, resta, multiplicación y división de {num_1} y {num_2}:')
print(tupla)

print('')