# EJERCICIO 3 - Agregar try-except
a = 10
try:
    b = input('Introduce un número: ')
    result = a / b
    print(f'Resultado: {result}')
except:
    print('Se produjo un error.')