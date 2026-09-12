# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se importa la función requerida desde el módulo de tablas de cálculos del proyecto
from calculos.tablas import tabla_multiplicar

# Se muestra en pantalla el encabezado
print('\n---EJERCICIO N.º 6 - Tabla de multiplicar---')

# INGRESO DE NÚMERO
# Se hace un llamado a la función definida para ingresar enteros mayores o iguales que cero
numero = ing.int_positivo_o_cero('Número')

# Se hace un llamado a la función que muestra la tabla de multiplicar por pantalla
tabla_multiplicar(numero)

print('')