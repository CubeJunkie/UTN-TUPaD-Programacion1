# EJERCICIO 6 - Permitir reintentar el ingreso
while True:
    try:
        numero = int(input('Ingrese un número entero: '))
    except ValueError:
        print('Debe ingresar un número válido.')
    except Exception as e:
        print('Se produjo un error inesperado.', type(e).__name__, '-', e)
    else:
        print(numero)
        break