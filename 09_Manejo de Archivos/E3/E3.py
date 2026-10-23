ARCHIVO_TXT = 'E3/productos.txt'

# BLOQUE 1 - Lectura de datos e impresión en pantalla
try:                                                                    # Se utiliza un bloque try-except para filtrar errores por problemas de acceso al archivo
    with open(ARCHIVO_TXT, 'r', encoding='utf-8') as archivo:           # Se usa with para abrir el archivo en modo lectura 'r' y que se cierre automáticamente al finalizar
        for linea in archivo:                                           # Se recorre el archivo línea por línea para imprimir los datos en pantalla
            datos = linea.strip().split(',')                            # Se usa strip y split para obtener los datos aislados separados por coma y capturarlos en una lista
            if len (datos) != 3:                                        # Si la lista no contenía 3 elementos, se imprime un mensaje de registro inválido y continúa con el lazo 
                print('Registro inválido.')
                continue
            nombre, precio, cantidad = datos                            # En caso contrario, se desempaqueta la lista en variables independientes y se las muestra por pantalla
            print(f'Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}')
            
except FileNotFoundError:
    print(f'Error: No se encontró el archivo {ARCHIVO_TXT}.')
except PermissionError:
    print('Error: Es posible que el archivo esté siendo utilizado por otro proceso.')
except Exception as e:
    print('Error: ', type(e).__name__, ' - ',e)

# BLOQUE 2 - Carga de datos
try:                                                                    # Se utiliza un bloque try-except para filtrar errores por problemas de acceso al archivo
    print('\n---Registro de Productos---')

    while True:                                                         # Se pide el nombre del producto repetidamente hasta obtener un valor no vacío
        nombre = input('Nombre: ').strip().capitalize()
        if nombre:
            break
        print('Error: El nombre no puede estar vacío.')

    while True:                                                         # Bloque try-except que se repite hasta obtener un precio float válido de parte del usuario 
        try:
            precio = float(input('Precio: ').strip())
            break
        except ValueError:
            print('Error: Debe ingresar un valor numérico válido para el precio.')
    
    while True:                                                         # Bloque try-except que se repite hasta obtener una cantidad entera válida de parte del usuario 
        try:
            cantidad = int(input('Cantidad: ').strip())
            break
        except ValueError:
            print('Error: Debe ingresar un valor entero válido para la cantidad.')        
    
    with open(ARCHIVO_TXT, 'a', encoding='utf-8') as archivo:           # Se usa with para abrir el archivo en modo añadir 'a' y que se cierre automáticamente al finalizar 
        archivo.write(f'{nombre},{precio},{cantidad}\n')                # Se agrega una línea al archivo que consta de un string con los datos separados por coma y un salto de línea

    print('Producto registrado con éxito.')                             # Mensaje de operación exitosa

except PermissionError:
    print('Error: Es posible que el archivo esté siendo utilizado por otro proceso.')
except Exception as e:
    print('Error: ', type(e).__name__, ' - ',e)