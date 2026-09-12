def tabla_multiplicar(numero):
    '''Recibe un número entero e imprime la tabla de multiplicar de ese número del 1 al 10.'''
    print('------------')
    for i in range(1,11):
        print(f'{numero} × {i} = {numero * i}')
    print('------------')