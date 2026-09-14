# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se importa la funcion requerida desde el modulo de saludos del proyecto
from auxiliar.saludos import saludar_usuario

# Se muestra en pantalla el encabezado
print('\n---EJERCICIO N.º 2 - Saludar al usuario por su nombre---')

# INGRESO DE NOMBRE
# Se hace un llamado a la función definida para ingresar strings no vacíos
nombre = ing.string_no_vacio('Nombre')

# Se hace un llamado a la función saludar_usuario()
saludar_usuario(f'{nombre}')

print('')