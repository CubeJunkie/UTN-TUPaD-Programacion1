# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se declara un diccionario con nombres y stock de productos
inventario = {
    'martillo':15,
    'destornillador':23,
    'pinza':12,
    'llave inglesa':8,
    'taladro':3,
    'serrucho':10
}

# Se declara la variable que almacenará la opción de menú seleccionada por el usuario
opcion = ''

# El bucle de menú se repite mientras no se seleccione la opción para salir
while opcion != '4':
    # Se muestra el menú de opciones en pantalla
    print('------------------------')
    print('---MENÚ DE INVENTARIO---')
    print('1) Consultar stock')
    print('2) Agregar stock')
    print('3) Agregar producto')
    print('4) Salir')
    print('------------------------')

    # Se le solicita al usuario ingresar una opción
    opcion = ing.string_opcion(('1', '2', '3', '4'))

    # Se utiliza una estructura case-match para ejecutar la opción seleccionada
    match opcion:
        case '1':
            print('------------------------')
            print('CONSULTA DE STOCK')
            # Se solicita al usuario el nombre del producto a consultar
            producto = ing.string_no_vacio('Producto').lower()
            # Si el producto no está en el inventario, se muestra un mensaje de error
            if inventario.get(producto) is None:
                print('Stock: Error - Ese producto no está en el inventario.')
            # En caso contrario se muestra el stock del producto consultado
            else:
                print(f'Stock: {inventario.get(producto)}')
        case '2':
            print('------------------------')
            print('AGREGAR STOCK')
            # Se solicita al usuario el nombre del producto a reponer
            producto = ing.string_no_vacio('Producto').lower()
            # Si el producto no está en el inventario, se muestra un mensaje de error
            if inventario.get(producto) is None:
                print('Stock: Error - Ese producto no está en el inventario.')
            else:
                # En caso contrario, se solicita la cantidad a agregar
                cantidad = ing.int_positivo('Cantidad')
                # Se actualiza el stock y se muestra el valor actualizado en pantalla
                inventario[producto] += cantidad
                print(f'Stock actualizado: {inventario.get(producto)}')
        case '3':
            print('------------------------')
            print('AGREGAR PRODUCTO')
            # Se solicita al usuario el nombre del producto a agregar
            producto = ing.string_no_vacio('Producto').lower()
            # Si el producto no estaba en el inventario, se lo agrega y se confirma por pantalla
            if inventario.get(producto) is None:
                inventario[producto] = 0
                print('Producto agregado.')
            # Si el producto ya estaba en inventario, se muestra un mensaje de error
            else:
                print(f'Error - Ese producto ya está re')
        case '4':
            # Cuando se selecciona la opción salir se muestra un mensaje de despedida por pantalla
            print('----FIN DEL PROGRAMA----\n')
            exit()

    # Pausa antes de mostrar el menú nuevamente
    print('------------------------')
    input('Presione enter para continuar...')