ARCHIVO_TXT = 'E5/productos.txt'
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

# BLOQUE 2 - Impresión en pantalla
print('---LISTA DE PRODUCTOS---')
for producto in productos:                                      # Se recorre la lista y se imprime en pantalla la información de cada producto
    print(f'Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}')

# BLOQUE 3 - Búsqueda de producto
print('------------------------')
print('BÚSQUEDA DE PRODUCTO')
print('------------------------')
while True:                                                     # Se pide el nombre del producto repetidamente hasta obtener un valor no vacío
    nombre_buscado = input('Nombre: ').strip().lower()
    if nombre_buscado:
        break
    print('Error: El nombre no puede estar vacío.')
producto_encontrado = False                                     # Se inicializa una bandera de producto encontrado con valor falso
for producto in productos:                                      # Se recorre la lista de productos
    if producto['nombre'].lower() == nombre_buscado:            # Si el nombre del producto coincide, se imprime por pantalla y se asigna valor verdadero a la bandera
        print(f'Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}')
        producto_encontrado = True
if not producto_encontrado:                                     # Si la bandera tiene valor falso, se informa que no hubo coincidencias
    print('No se encontró el producto en la lista.')
print('------------------------')