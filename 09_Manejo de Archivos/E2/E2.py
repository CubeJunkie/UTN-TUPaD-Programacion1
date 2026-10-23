ARCHIVO_TXT = 'E2/productos.txt'

# BLOQUE 1 - Lectura de datos e impresión en pantalla
try:                                                                    # Se utiliza un bloque try-except para filtrar errores por problemas de acceso al archivo
    with open(ARCHIVO_TXT, 'r', encoding='utf-8') as archivo:           # Se usa with para abrir el archivo en modo lectura 'r' y que se cierre automáticamente al finalizar
        print('---LISTA DE PRODUCTOS---')
        for linea in archivo:                                           # Se recorre el archivo línea por línea para imprimir los datos en pantalla
            datos = linea.strip().split(',')                            # Se usa strip y split para obtener los datos aislados separados por coma y capturarlos en una lista
            if len (datos) != 3:                                        # Si la lista no contenía 3 elementos, se imprime un mensaje de registro inválido y continúa con el lazo 
                print('Registro inválido.')
                continue
            nombre, precio, cantidad = datos                            # En caso contrario, se desempaqueta la lista en variables independientes y se las muestra por pantalla
            print(f'Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}')
        print('------------------------')
except FileNotFoundError:
    print(f'Error: No se encontró el archivo {ARCHIVO_TXT}.')
except PermissionError:
    print('Error: Es posible que el archivo esté siendo utilizado por otro proceso.')
except Exception as e:
    print('Error: ', type(e).__name__, ' - ',e)