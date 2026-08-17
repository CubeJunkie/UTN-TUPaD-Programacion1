# EJERCICIO 1 - Caja del Kiosco
print('\n---Ejercicio 1 - Caja del Kiosco---\n')

# Se inicializa una bandera auxiliar con valor falso para luego validar el nombre del cliente ingresado
nombre_cliente_valido = False

# El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
while nombre_cliente_valido == False:
    # Se solicita al usuario el nombre del cliente, se eliminan espacios en extremos y se aplica formato de mayúsculas iniciales
    nombre_cliente = input('Ingrese el nombre del cliente: ').strip().capitalize()
    # Si el nombre del cliente es alfabético, se asigna valor verdadero a la bandera
    if nombre_cliente.isalpha():
        nombre_cliente_valido = True
    # Si no se cumple la condición, esto se indica en pantalla
    else:
        print('- ERROR - Ingrese un nombre válido (letras)')

# Se inicializa una bandera auxiliar con valor falso para luego validar la cantidad de productos ingresada
cant_productos_valida = False

# El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
while cant_productos_valida == False:
    # Se solicita al usuario la cantidad de productos a comprar y se eliminan espacios en extremos
    cant_productos = input('Ingrese la cantidad de productos a comprar: ').strip()
    # Si se comprueba que la cantidad está formada solo por dígitos, se asigna valor verdadero a la bandera y se convierte el valor en entero
    if cant_productos.isdigit():
        # Se convierte la cantidad de productos de string a int
        cant_productos = int(cant_productos)
        # Si el valor ingresado es un entero positivo, se le da valor verdadero a la bandera
        if cant_productos > 0:
            cant_productos_valida = True
        # En caso contrario se indica en pantalla el problema
        else:
            print('- ERROR - Ingrese un valor positivo')
    # Si el valor no está formado por dígitos, esto se indica en pantalla
    else:
        print('- ERROR - Ingrese una cantidad válida (número entero positivo)')

# Se inicializa las variables de montos totales y descuento
total_sin_descuento = 0
total_con_descuento = 0
DESCUENTO = 0.1

# Se repite el lazo para la cantidad de productos ingresada
for num_producto in range(1, cant_productos+1):
    # Se muestra en pantalla el producto para el cual se pedirán datos
    print(f'\nPRODUCTO {num_producto}')
    # Se inicializa una bandera auxiliar con valor falso para luego validar el precio
    precio_valido = False

    # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
    while precio_valido == False:
        # Se solicita al usuario el precio del producto y se eliminan espacios en extremos
        precio = input('Precio: ').strip()

        # Si se comprueba que la cantidad está formada solo por dígitos, se asigna valor verdadero a la bandera y se convierte el valor en entero
        if precio.isdigit():
            precio_valido = True
            precio = int(precio)

        # En caso contrario, se muestra el error en pantalla
        else:
            print('- ERROR - Ingrese un número entero')

    # Se inicializa una bandera auxiliar con valor falso para luego validar el descuento
    descuento_valido = False

    # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
    while descuento_valido == False:
        # Se solicita al usuario el precio del producto, se eliminan espacios en extremos y se convierte en mayúsculas
        descuento = input('Descuento (S/N): ').strip().upper()

        # Si se comprueba que la variable descuento tiene formato válido, se asigna valor verdadero a la bandera
        if descuento in 'SN':
            descuento_valido = True

        # En caso contrario, se indica el error en pantalla
        else:
            print('ERROR - Seleccione una opción válida')

    # Se suma el precio al total sin descuentos
    total_sin_descuento += precio

    # Si hay descuento, se suma el precio con descuento al total con descuentos
    if descuento == 'S':
        total_con_descuento += precio * (1-DESCUENTO)
    # En caso contrario, se suma el precio sin descuento al total con descuentos  
    else:
        total_con_descuento += precio
        
# Salida por pantalla
print(f'''
Cliente: {nombre_cliente}
Cantidad de productos: {cant_productos}
Total sin descuentos: ${total_sin_descuento}
Total con descuentos: ${total_con_descuento:.2f}
Ahorro: ${total_sin_descuento - total_con_descuento:.2f}
Promedio por producto: ${total_con_descuento / cant_productos:.2f}
''')