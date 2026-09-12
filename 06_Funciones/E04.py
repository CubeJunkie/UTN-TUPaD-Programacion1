# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se importa las funciones requeridas desde el módulo de geometría del proyecto
from calculos.geometria import calcular_area_circulo, calcular_perimetro_circulo

# Se muestra en pantalla el encabezado
print('\n---EJERCICIO N.º 4 - Cálculo de radio y perímetro de un círculo---')

# INGRESO DE RADIO
# Se hace un llamado a la función definida para ingresar decimales mayores o iguales que cero
radio = ing.float_positivo_o_cero('Radio')

# Se hace un llamado a la función que calcula el área y se guarda el valor en una variable global
area_circulo = calcular_area_circulo(radio)

# Se hace un llamado a la función que calcula el perímetro y se guarda el valor en una variable global
perimetro_circulo = calcular_perimetro_circulo(radio)

# Se muestran los valores por pantalla
print('---------------------------')
print(f'Un círculo de radio {radio:.2f} tiene área {area_circulo:.2f} y perímetro {perimetro_circulo:.2f}\n')