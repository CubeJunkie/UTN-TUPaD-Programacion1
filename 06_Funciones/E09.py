# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se importa la función requerida desde el módulo de conversiones del proyecto
from calculos.conversiones import celsius_a_fahrenheit

# Se muestra en pantalla el encabezado
print('\n---EJERCICIO N.º 9 - Conversión de Celsius a Fahrenheit---')

# INGRESO DE TEMPERATURA EN CELSIUS
# Se hace un llamado a la función definida para ingresar decimales válidos
celsius = ing.float_valido('Temperatura en °C')

# Se hace un llamado a la función que convierte Celsius a Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)

# Se muestra el resultado por pantalla
print('---------------------------')
print(f'{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F\n')