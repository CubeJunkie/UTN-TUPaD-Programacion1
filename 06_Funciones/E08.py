# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se importa la función requerida desde el módulo de índices del proyecto
from calculos.indices import imc

# Se muestra en pantalla el encabezado
print('\n---EJERCICIO N.º 8 - Índice de masa corporal.---')

# INGRESO DE PESO
# Se hace un llamado a la función definida para ingresar decimales mayores que cero
peso = ing.float_positivo('Peso (kg)')

# INGRESO DE ALTURA
# Se hace un llamado a la función definida para ingresar decimales mayores que cero
altura = ing.float_positivo('Altura (m)')

# Se hace un llamado a la función imc() para obtener el índice de masa corporal
imc = imc(peso, altura)

print('---------------------------')

# Se muestra la tupla en pantalla
print(f'Índice de masa corporal (IMC): {imc:.2f}')

print('')