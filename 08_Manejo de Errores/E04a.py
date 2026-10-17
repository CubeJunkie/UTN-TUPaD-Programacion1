# EJERCICIO 4 - Excepciones múltiples
a = 10
try:
    b = input('Introduce un número: ')
    result = a / b
    print(f'Resultado: {result}')
except TypeError:
    print('Una función recibió un dato de tipo no aceptado.')
except ValueError:
    print('No se ingresó un entero válido.')
except ZeroDivisionError:
    print('Error de división por cero.')
except Exception as e:
    print('Se produjo un error.')