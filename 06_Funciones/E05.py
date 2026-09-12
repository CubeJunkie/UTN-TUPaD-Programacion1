# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se importa la función requerida desde el módulo de conversiones del proyecto
from calculos.conversiones import segundos_a_horas

# Se muestra en pantalla el encabezado
print('\n---EJERCICIO N.º 5 - Conversión de segundos a horas---')

# INGRESO DE SEGUNDOS
# Se hace un llamado a la función definida para ingresar enteros mayores o iguales que cero
segundos = ing.int_positivo_o_cero('Segundos')

# Se hace un llamado a la función que convierte segundos a horas
horas = segundos_a_horas(segundos)

# Se muestra el resultado por pantalla
print('---------------------------')
print(f'{segundos} segundos equivalen a {horas:.2f} horas\n')