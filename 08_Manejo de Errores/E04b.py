# EJERCICIO 4 - Excepciones múltiples
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print('El índice utilizado está fuera de rango.')
except:
    print('Se produjo un error.')