# EJERCICIO 6 - Validar un número ingresado
try:
    numero = int(input('Ingrese un número entero:'))
except ValueError:
    print('Debe ingresar un número válido.')
except Exception as e:
    print('Se produjo un error inesperado.', type(e).__name__, '-', e)