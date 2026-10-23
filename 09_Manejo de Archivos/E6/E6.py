ARCHIVO_TXT = 'E6/productos.txt'
productos = []

# BLOQUE 1 - Lectura de datos
try:                                                                    # Se utiliza un bloque try-except para filtrar errores por problemas de acceso al archivo
    with open(ARCHIVO_TXT, 'r', encoding='utf-8') as archivo:           # Se usa with para abrir el archivo en modo lectura 'r' y que se cierre automáticamente al finalizar
        for linea in archivo:                                           # Se recorre el archivo línea por línea para imprimir los datos en pantalla
            datos = linea.strip().split(',')                            # Se usa strip y split para obtener los datos aislados separados por coma y capturarlos en una lista
            if len (datos) != 3:                                        # Si la lista no contenía 3 elementos, se imprime un mensaje de registro inválido y continúa con el lazo 
                print('Registro inválido.')
                continue
            nombre, precio, cantidad = datos                            # En caso contrario, se desempaqueta la lista en variables independientes y se las muestra por pantalla
            producto_dict = {                                           # Se declara un diccionario con los datos del producto para sumarlo a la lista
                'nombre': nombre,
                'precio': float(precio),
                'cantidad': int(cantidad)
            }
            productos.append(producto_dict)                             # Se añade el producto a la lista de diccionarios
            
except FileNotFoundError:
    print(f'Error: No se encontró el archivo {ARCHIVO_TXT}.')
except PermissionError:
    print('Error: Es posible que el archivo esté siendo utilizado por otro proceso.')
except Exception as e:
    print('Error: ', type(e).__name__, ' - ',e)

# MENÚ DE OPCIONES
while True:                                                                         # Se muestra el menú de opciones repetidamente hasta que el usuario decide salir
    print('''
---MENU DE INVENTARIO---
1) Ver lista de productos
2) Buscar producto
3) Agregar producto
4) Salir
------------------------''')
    opcion = input('Opción: ')
    match opcion:
        case '1':                                                                   # OPCIÓN 1 - MOSTRAR LISTA DE PRODUCTOS
            print('---LISTA DE PRODUCTOS---')
            for producto in productos:                                              # Se recorre la lista producto por producto y se muestran los detalles
                print(f'Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}')
            print('------------------------')
            input('Presione enter para continuar...')
        case '2':                                                                   # OPCIÓN 2 - BUSCAR PRODUCTO
            print('------------------------')
            print('BÚSQUEDA DE PRODUCTO')
            print('------------------------')
            while True:                                                             # Se pide el nombre del producto a buscar repetidamente hasta obtener un valor no vacío 
                nombre_buscado = input('Nombre: ').strip().lower()
                if nombre_buscado:
                    break
                print('Error: El nombre no puede estar vacío.')
            producto_encontrado = False                                             # Se inicializa una bandera de producto encontrado con valor falso
            for producto in productos:                                              # Se recorre la lista de productos
                if producto['nombre'].lower() == nombre_buscado:                    # Si el nombre del producto coincide, se imprime por pantalla y se asigna valor verdadero a la bandera
                    print(f'Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}')
                    producto_encontrado = True                                      
            if not producto_encontrado:                                             # Si la bandera tiene valor falso, se informa que no hubo coincidencias
                print('No se encontró el producto en la lista.')
            print('------------------------')
            input('Presione enter para continuar...')
        case '3':                                                                   # OPCIÓN 3 - AGREGAR PRODUCTO
            print('------------------------')
            print('AGREGAR PRODUCTO')
            print('------------------------')
            while True:                                                             # Se pide el nombre del producto repetidamente hasta obtener un valor no vacío
                nombre = input('Nombre: ').strip().capitalize()
                if nombre:
                    break
                print('Error: El nombre no puede estar vacío.')
            while True:                                                             # Bloque try-except que se repite hasta obtener un precio float válido de parte del usuario 
                try:
                    precio = float(input('Precio: ').strip())
                    break
                except ValueError:
                    print('Error: Debe ingresar un valor numérico válido para el precio.')         
            while True:                                                             # Bloque try-except que se repite hasta obtener una cantidad entera válida de parte del usuario 
                try:
                    cantidad = int(input('Cantidad: ').strip())
                    break
                except ValueError:
                    print('Error: Debe ingresar un valor entero válido para la cantidad.')        
            producto_dict = {                                                       # Se declara un diccionario con los datos del producto para sumarlo a la lista
                'nombre': nombre,
                'precio': precio,
                'cantidad': cantidad
            }
            productos.append(producto_dict)                                         # Se añade el producto a la lista de diccionarios
            print('------------------------')
            print('Producto añadido.')
            input('Presione enter para continuar...')
        case '4':                                                                   # OPCIÓN 4 - SALIR
            try:                                                                    # Se utiliza un bloque try-except para filtrar errores por problemas de acceso al archivo
                
                with open(ARCHIVO_TXT, 'w', encoding='utf-8') as archivo:           # Se usa with para abrir el archivo en modo escritura 'w' y que se cierre automáticamente al finalizar 
                    for producto in productos:                                      # Se recorre la lista y se agrega cada producto al archivo en forma de un string separado por comas y un salto de línea al final
                        archivo.write(f'{producto["nombre"]},{str(producto["precio"])},{str(producto["cantidad"])}\n')
                print('Datos guardados con éxito.')                                 # Mensaje de operación exitosa
                print('------------------------')
                exit()
            except PermissionError:
                print('Error: Es posible que el archivo esté siendo utilizado por otro proceso.')
            except Exception as e:
                print('Error: ', type(e).__name__, ' - ',e)
        case _:                                                                     # Si el usuario ingresa una opción inválida, se muestra un mensaje y se reinicia el bucle de menú
            print('Error: Debe seleccionar una opción válida.')
            print('------------------------')
            input('Presione enter para continuar...')