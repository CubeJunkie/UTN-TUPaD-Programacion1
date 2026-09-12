# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se importa la función requerida desde el módulo de operaciones del proyecto
from calculos.operaciones import calcular_promedio

# Se muestra en pantalla el encabezado
print('\n---EJERCICIO N.º 10 - Calcular el promedio de 3 números.---')

# INGRESO DE NÚMEROS
# Se hace llama a la función definida para ingresar enteros mayores que cero
num_1 = ing.float_valido('Número 1')
num_2 = ing.float_valido('Número 2')
num_3 = ing.float_valido('Número 3')

# Se hace un llamado a la función calcular_promedio() para obtener el promedio
promedio = calcular_promedio(num_1, num_2, num_3)

print('---------------------------')

# Se muestra la tupla en pantalla
print(f'El promedio de {num_1:.2f}, {num_2:.2f} y {num_3:.2f} es igual a {promedio:.2f}')

print('')