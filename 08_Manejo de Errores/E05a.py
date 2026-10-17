# EJERCICIO 5 - Agregar else y finally
a = 10
try:
    b = input('Introduce un número: ')
    result = a / b
except TypeError:
    print('Una función recibió un dato de tipo no aceptado.')
except ValueError:
    print('No se ingresó un entero válido.')
except ZeroDivisionError:
    print('Error de división por cero.')
except Exception as e:
    print('Se produjo un error.')
else:
    print(f'Resultado: {result}')
finally:
    print('Fin de bloque try-except.')