# EJERCICIO 1 - Notas de 10 estudiantes
print('\n-----EJERCICIO 1 - Notas de 10 estudiantes-----')

# Se importa el módulo random para poder generar números aleatorios
import random
# Se define la cantidad de estudiantes para el ejercicio en una constante
ESTUDIANTES = 10
# Se define una lista de elementos vacíos con esa longitud
notas=[None]*ESTUDIANTES

# Se utiliza un bucle para recorrer la longitud de la lista
for i in range(len(notas)):
    # En cada iteración, se utiliza el módulo random para generar un float aleatorio, se lo redondea a dos dígitos decimales y se lo asigna al elemento de la lista
    notas[i] = round(random.uniform(0.0,10.0),2)

# Se utiliza un bucle para recorrer la longitud de la lista
for i in range(len(notas)):
    # En cada iteración, se imprime un elemento de la lista
    print(f'{notas[i]}', end='\t')

# Se inicializa una variable float en cero para luego almacenar la suma de los elementos de la lista
suma = 0.0
# Se utiliza un bucle para recorrer la longitud de la lista
for i in range(len(notas)):
    # En cada iteración, se añade el elemento de la lista a la suma
    suma += notas[i]

# Se calcula el promedio dividiendo la suma en la cantidad de estudiantes y se muestra el resultado en pantalla
promedio = round(suma / len(notas), 2)
print(f'\nPromedio: {promedio}', end='\t')

# Se inicializan 2 variables float para luego almacenar la nota mínima y máxima
nota_min = 10.0
nota_max = 0.0

# Se utiliza un bucle para recorrer la longitud de la lista
for i in range(len(notas)):
    # Se compara el elemento de la lista con los valores máximos y mínimos actuales y se los reemplaza de ser necesario
    if notas[i] < nota_min:
        nota_min = notas[i]
    if notas[i] > nota_max:
        nota_max = notas[i]
# Se muestra en pantalla la nota más baja y la más alta
print(f'Nota más baja: {nota_min}\tNota más alta: {nota_max}\n')



# EJERCICIO 2 - Cargar 5 productos en una lista
print('\n-----EJERCICIO 2 - Cargar 5 productos en una lista-----')

# Se define la cantidad de productos para el ejercicio en una constante
PRODUCTOS = 5
# Se define una lista de elementos vacíos con esa longitud
lista_productos = [None] * PRODUCTOS

# Se utiliza un bucle para recorrer la longitud de la lista y pedir al usuario que cargue cada elemento
print(f'Cargue {len(lista_productos)} productos')
for i in range(len(lista_productos)):
    lista_productos[i] = input(f'- Producto n.º {i + 1}: ')

# Se utiliza el método sorted() para obtener una nueva lista con los productos ordenados
lista_productos_ordenados = sorted(lista_productos)

# Se utiliza un bucle para recorrer la longitud de la lista e imprimir cada elemento en pantalla
print('Lista ordenada: ')
for i in range(len(lista_productos_ordenados)):
    print(f'- Producto n.º {i + 1}: {lista_productos_ordenados[i]}')

# Se le pide al usuario que indique qué elemento quiere eliminar
producto_a_eliminar = input('¿Qué producto desea eliminar?: ')
# Si el elemento está contenido en la lista, se lo elimina con remove() y se actualiza la longitud de la lista
if producto_a_eliminar in lista_productos_ordenados:
    lista_productos_ordenados.remove(producto_a_eliminar)
    PRODUCTOS = PRODUCTOS - 1
    # Se utiliza un bucle para recorrer la longitud de la lista e imprimir cada elemento en pantalla
    print('Lista actualizada: ')
    for i in range(len(lista_productos_ordenados)):
        print(f'- Producto n.º {i + 1}: {lista_productos_ordenados[i]}')
    print('')
# Si el elemento no está en la lista, se indica esto en pantalla
else:
    print(f'\"{producto_a_eliminar}\" no estaba en la lista.\n')



# EJERCICIO 3 - Separar pares e impares en lista de 15 números
print('\n-----EJERCICIO 3 - Separar pares e impares en lista de 15 números-----')

# Se importa el módulo random para poder generar números aleatorios
import random
# Se define la cantidad de estudiantes para el ejercicio en una constante
CANT_NUMEROS = 15
# Se define una lista de elementos vacíos con esa longitud
lista_numeros=[None]*CANT_NUMEROS

# Se utiliza un bucle para recorrer la longitud de la lista
for i in range(len(lista_numeros)):
    # En cada iteración, se utiliza el módulo random para generar un int aleatorio entre 1-100 y se lo asigna al elemento de la lista
    lista_numeros[i] = random.randint(1,100)

# Se utiliza un bucle para recorrer la longitud de la lista e imprimir cada elemento en pantalla
print(f'{len(lista_numeros)} números: ', end='     ')
for i in range(len(lista_numeros)):
    print(f'{lista_numeros[i]}', end='\t')

# Se definen listas vacías para luego almacenar los elementos pares e impares
lista_pares = []
lista_impares = []

# Se recorre la longitud de la lista principal para detectar números pares e impares
for i in range(len(lista_numeros)):
    # Si el elemento es par, se añade a la lista de pares con append()
    if lista_numeros[i] % 2 == 0:
        lista_pares.append(lista_numeros[i])
    # En caso contrario, se añade a la lista de impares con append()
    else:
        lista_impares.append(lista_numeros[i])

# Se utiliza un bucle para recorrer la longitud de la lista de pares e imprimir cada elemento en pantalla
print('\nNúmeros pares: ', end='  ')
for i in range(len(lista_pares)):
    print(f'{lista_pares[i]}', end='\t')

    # Se utiliza un bucle para recorrer la longitud de la lista de impares e imprimir cada elemento en pantalla
print('\nNúmeros impares: ', end='')
for i in range(len(lista_impares)):
    print(f'{lista_impares[i]}', end='\t')

# Se utiliza el método len() para mostrar en pantalla la longitud de las listas de números pares e impares
print(f'\nCantidad de números pares: {len(lista_pares)}')
print(f'Cantidad de números impares: {len(lista_impares)}\n')



# EJERCICIO 4 - Crear nueva lista sin elementos repetidos
print('\n-----EJERCICIO 4 - Crear nueva lista sin elementos repetidos-----')

# Se define la lista provista en la consigna
datos = [1,3,5,3,7,1,9,5,3]

# Se utiliza un bucle para recorrer la longitud de la lista e imprimir cada elemento en pantalla
print('Datos: ', end='    ')
for i in range(len(datos)):
    print(f'{datos[i]}', end='\t')

# Se declara una nueva lista vacía para luego cargar los elementos no repetidos
sin_repetidos = []

# Se recorre la longitud de la lista
for i in range(len(datos)):
    if not datos[i] in sin_repetidos:
        sin_repetidos.append(datos[i])

# Se utiliza un bucle para recorrer la longitud de la lista e imprimir cada elemento en pantalla
print('\nSin rep: ', end='  ')
for i in range(len(sin_repetidos)):
    print(f'{sin_repetidos[i]}', end='\t')
print('\n')



# EJERCICIO 5 - Agregar o quitar estudiantes de la lista
print('\n-----EJERCICIO 5 - Agregar o quitar estudiantes de la lista-----')

# Se define una lista con los nombres de 8 estudiantes como indica la consigna
estudiantes = ['Andrés', 'Carlos', 'Daniel', 'Eduardo', 'Federico', 'Gabriel', 'Juan', 'Luis']

# Se utiliza un bucle para recorrer la longitud de la lista e imprimir cada elemento en pantalla
print('Estudiantes: ')
for i in range(len(estudiantes)):
    print(f'- {estudiantes[i]}',)

# Se inicializa una bandera de número válido en falso para validad la respuesta del usuario
opcion_valida = False
# Se muestran las opciones en pantalla
print('1) Agregar estudiante\t2) Eliminar estudiante')
# Se repite el bucle de carga de datos mientras la bandera tenga valor falso
while opcion_valida == False:
    # Se pide al usuario que ingrese una opción
    opcion = input('Opción: ').strip()
    # Se comprueba que el valor ingresado sea una opción válida
    if opcion == '1' or opcion == '2':
        opcion_valida = True
    else:
        print('ERROR - Ingrese una opción válida')

# Se utiliza una estructura match-case para realizar acciones en función de la opción seleccionada
match opcion:
    case '1':
        # Se inicializa una bandera con valor falso para validad el nombre
        nombre_valido = False
        # Se repite el bucle de carga de datos mientras la bandera tenga valor falso
        while nombre_valido == False:
            estudiante_a_agregar = input('Nombre del estudiante a agregar: ').strip().capitalize()
            if estudiante_a_agregar == '':
                print('ERROR - Debe ingresar un nombre')
            else:
                nombre_valido = True
        # Se agrega el estudiante a la lista
        estudiantes.append(estudiante_a_agregar)
        
    case '2':
        # Se inicializa una bandera con valor falso para validad el nombre
        nombre_valido = False
        # Se repite el bucle de carga de datos mientras la bandera tenga valor falso
        while nombre_valido == False:
            estudiante_a_eliminar = input('Nombre del estudiante a eliminar: ').strip().capitalize()
            if estudiante_a_eliminar == '':
                print('ERROR - Ingrese un nombre válido')
            # Se verifica que el nombre ingresado esté en la lista
            elif not estudiante_a_eliminar in estudiantes:
                print('ERROR - Ese estudiante no está en la lista')
            else:
                nombre_valido = True
        # Se elimina el estudiante de la lista
        estudiantes.remove(estudiante_a_eliminar)

# Se utiliza un bucle para recorrer la longitud de la lista e imprimir cada elemento en pantalla
print('Estudiantes: ')
for i in range(len(estudiantes)):
    print(f'- {estudiantes[i]}',)



# EJERCICIO 6 - Rotar elementos de lista 1 posición hacia la derecha
print('\n-----EJERCICIO 6 - Rotar elementos de lista 1 posición hacia la derecha-----')

# Se importa el módulo random para poder generar números aleatorios
import random

# Se define la cantidad de productos para el ejercicio en una constante
ELEMENTOS = 7
# Se define una lista de elementos vacíos con esa longitud
lista_elementos = [None] * ELEMENTOS

# Se utiliza un bucle para recorrer la longitud de la lista
for i in range(len(lista_elementos)):
    # En cada iteración, se utiliza el módulo random para generar un entero aleatorio y se lo asigna al elemento de la lista
    lista_elementos[i] = random.randint(1,100)

# Se utiliza un bucle para recorrer la longitud de la lista e imprimir cada elemento en pantalla
print(f'Lista inicial: ', end='  ')
for i in range(len(lista_elementos)):
    print(f'{lista_elementos[i]}', end='\t')

# Se saca y captura el último elemento de la lista utilizando el método pop()
elemento_auxiliar = lista_elementos.pop(len(lista_elementos)-1)

# Se utiliza el método insert() para insertar el elemento capturado en la primera posición y desplazar todo a la derecha
lista_elementos.insert(0, elemento_auxiliar)

# Se utiliza un bucle para recorrer la longitud de la lista e imprimir cada elemento en pantalla
print(f'\nLista nueva: ', end='    ')
for i in range(len(lista_elementos)):
    print(f'{lista_elementos[i]}', end='\t')
print('\n')



# EJERCICIO 7 - Promedio de temperaturas max y min, y mayor amplitud térmica
print('\n-----EJERCICIO 7 - Promedio de temperaturas max y min, y mayor amplitud térmica-----')

# Se importa el módulo random para poder generar números aleatorios
import random

# Se declara una lista vacía para cargar los datos de temperatura de la semana
temperaturas = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0]
]

# Se declara una lista auxiliar con los nombres de los días de la semana
dias_semana = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']

# Se recorre los elementos de la matriz para cargar los datos de temperaturas máximas y mínimas
for i in range(len(temperaturas)):
    temperaturas[i][0] = random.randint(0,8)
    temperaturas[i][1] = random.randint(20,30)

# Se recorre la lista para obtener las sumas de máximas y mínimas
prom_min = round(sum(fila[0] for fila in temperaturas)/len(temperaturas), 1)
prom_max = round(sum(fila[1] for fila in temperaturas)/len(temperaturas), 1)

# Se declaran una lista auxiliar para cargar las amplitudes
amplitudes_temperatura = [0] * 7

# Se recorre la lista de amplitudes y se cargan una por una
for i in range(len(amplitudes_temperatura)):
    amplitudes_temperatura[i] = temperaturas[i][1] - temperaturas[i][0]

# Se obtiene la mayor amplitud con el método max()
amplitud_max = max(amplitudes_temperatura)

# Se obtiene la posición de la amplitud máxima con el método index() para determinar el día de la semana
pos_amplitud_max = amplitudes_temperatura.index(amplitud_max)

# Se muestran los datos por pantalla
for i in range(len(temperaturas)):
    print(f'{dias_semana[i]}:', end = '  \t')
    print(f'Min.: {temperaturas[i][0]} °C', end = '\t')
    print(f'Máx.: {temperaturas[i][1]} °C', end = '\t')
    print(f'Amp.: {amplitudes_temperatura[i]} °C')
print(f'- Prom. mínimas: {prom_min} °C')
print(f'- Prom. máximas: {prom_max} °C')
print(f'- Amplitud máx.: {dias_semana[pos_amplitud_max]} ({amplitud_max} °C)\n')



# EJERCICIO 8 - Promedios de notas por estudiante y por materia
print('\n-----EJERCICIO 8 - Promedios de notas por estudiante y por materia-----')

# Se importa el módulo random para poder generar números aleatorios
import random

# Se declara una lista vacía para cargar las notas de los estudiantes
notas = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Se recorre los elementos de la matriz para cargar las notas
for i in range(len(notas)):
    notas[i][0] = round(random.uniform(0.0,10.0),1)
    notas[i][1] = round(random.uniform(0.0,10.0),1)
    notas[i][2] = round(random.uniform(0.0,10.0),1)

prom_materia_1 = round(sum(fila[0] for fila in notas)/len(notas),1)
prom_materia_2 = round(sum(fila[1] for fila in notas)/len(notas),1)
prom_materia_3 = round(sum(fila[2] for fila in notas)/len(notas),1)

# Se muestran los datos por pantalla
for i in range(len(notas)):
    print(f'Alumno {i + 1}:', end = '  \t')
    print(f'Materia 1: {notas[i][0]}', end = '  \t')
    print(f'Materia 2: {notas[i][1]}', end = '  \t')
    print(f'Materia 3: {notas[i][2]}', end = '  \t')
    print(f'Promedio: {round((sum(notas[i]))/len(notas[i]),1)}')
print(f'Prom. Materia 1: {prom_materia_1}')
print(f'Prom. Materia 2: {prom_materia_2}')
print(f'Prom. Materia 3: {prom_materia_3}\n')



# EJERCICIO 9 - Ta-Te-Ti
print('\n-----EJERCICIO 9 - Ta-Te-Ti-----')

# Se declara una lista para el tablero
tablero = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# Se muestra el tablero vacío en pantalla
for i in range(len(tablero)):
    for j in range(len(tablero[i])):
        print(f' {tablero[i][j]}', end =' ')
    print('')

# Se define una variable int para contar las rondas
rondas = 0
# Se define una variable string para indicar el turno comenzando por X
turno = 'X'
# Se define una variable string para el ganador con valor inicial vacío
ganador = ''

# Se repite el bucle de juego mientras no haya un ganador
while ganador == '' and rondas < 9:
    # Se asigna valor incial falso a la bandera de posición válida
    posicion_valida = False
    print('----------------------------')
    # El bucle de ingreso de datos se repite mientras la bandera de posición válida tenga valor falso
    while posicion_valida == False:
        posicion = input(f'Turno {turno} (fila,columna): ').strip()
        if (len(posicion) != 3) or (not posicion[0].isdigit()) or (posicion[1] != ',') or (not posicion[2].isdigit()):
            print('ERROR - Ingrese una posición con formato válido')
            continue
        elif not (posicion[0] in '123' and posicion[2] in '123'):
            print('ERROR - Ingrese una posición dentro de rango (1-3,1-3)')
            continue
        elif tablero[int(posicion[0])-1][int(posicion[2])-1] != '-':
            print('ERROR - Posición ocupada')
            continue
        posicion_valida = True
    tablero[int(posicion[0])-1][int(posicion[2])-1] = turno

    # Se muestra el tablero en pantalla
    print('')
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(f' {tablero[i][j]}', end =' ')
        print('')
    print('')

    # Se verifica si hay 3 en línea y de ser así se asigna el ganador
    if tablero[0][0] == tablero[0][1] == tablero[0][2] and tablero[0][0] != '-':
        ganador = turno
        continue
    elif tablero[1][0] == tablero[1][1] == tablero[1][2] and tablero[1][0] != '-':
        ganador = turno
        continue
    elif tablero[2][0] == tablero[2][1] == tablero[2][2] and tablero[2][0] != '-':
        ganador = turno
        continue
    elif tablero[0][0] == tablero[1][0] == tablero[2][0] and tablero[0][0] != '-':
        ganador = turno
        continue
    elif tablero[0][1] == tablero[1][1] == tablero[2][1] and tablero[0][1] != '-':
        ganador = turno
        continue
    elif tablero[0][2] == tablero[1][2] == tablero[2][2] and tablero[0][2] != '-':
        ganador = turno
        continue
    elif tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != '-':
        ganador = turno
        continue
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != '-':
        ganador = turno
        continue
    # Se incrementa el contador de rondas
    rondas += 1
    # Se cambia de turno antes de repetir el lazo
    if turno == 'X':
        turno = 'O'
    else:
        turno = 'X'

print('----------------------------')
# Se muestra el ganador en pantalla
if ganador != '':
    print(f'---------GANADOR: {ganador}---------\n')
else:
    print('-----------EMPATE-----------\n')



# EJERCICIO 10 - Ventas de 4 productos en 7 días
print('\n-----EJERCICIO 10 - Ventas de 4 productos en 7 días-----')

# Se importa el módulo random para poder generar números aleatorios
import random

# Se declara una constante con la cantidad de productos
PRODUCTOS = 4

# Se declara una lista para el registro
registro = [[0] * 7 for _ in range(PRODUCTOS)]

# Se declara una lista auxiliar con los nombres de los días de la semana
dias_semana = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']

# Se declara una lista auxiliar con los nombres de los días de la semana abreviados
dias_semana_abreviados = ['L','M','M','J','V','S','D']

# Se declara una lista para contener las ventas totales por producto
ventas_por_producto = [0] * PRODUCTOS

# Se declara una lista para contener las ventas totales por día
ventas_por_dia = [0] * 7

# Se recorre los elementos de la matriz para cargar datos aleatorios de ventas
for i in range(len(registro)):
    for j in range(len(registro[i])):
        registro[i][j] = random.randint(0,30)

# Se calculan las ventas totales por producto
for i in range(PRODUCTOS):
    ventas_por_producto[i] = sum(registro[i])

# Se calculan las ventas totales por día
for i in range(7):
    ventas_por_dia[i] = sum(fila[i] for fila in registro)

# Se muestran los datos y resultados por pantalla
for i in range(len(dias_semana_abreviados)):
    print(f'\t{dias_semana_abreviados[i]}', end = '')
print('\t|  Totales', end = '')
print('\n---------------------------------------------------------------------------')

# Datos del registro y ventas por producto
for i in range(len(registro)):
    print(f'{i + 1} |', end = '\t')
    for j in range(len(registro[i])):
        print(f'{registro[i][j]}', end = '\t')
    print(f'|  {ventas_por_producto[i]}')
print('---------------------------------------------------------------------------')

# Ventas por dia
for i in range(len(ventas_por_dia)):
    print(f'\t{ventas_por_dia[i]}', end = '')

# Día con más ventas
print(f'\t> Más ventas: {dias_semana[ventas_por_dia.index(max(ventas_por_dia))]}\n')



# EJERCICIO 11 - Búsqueda en lista de 10 estudiantes
print('\n-----EJERCICIO 11 - Búsqueda en lista de 10 estudiantes-----')

# Se declara una lista con los nombres de 10 estudiantes
estudiantes = ['Andrés', 'Carlos', 'Daniel', 'Eduardo', 'Federico', 'Gabriel', 'Juan', 'Luis', 'Miguel', 'Pablo']

# Se muestra la lista en pantalla
for i in range(len(estudiantes)):
    print(f'{i + 1}: {estudiantes[i]}')
print('-------------------------')

# Se inicializa una bandera con valor falso para validad el nombre
nombre_valido = False
# Se repite el bucle de carga de datos mientras la bandera tenga valor falso
while nombre_valido == False:
    estudiante_a_buscar = input('Ingrese un nombre a buscar: ').strip().capitalize()
    if estudiante_a_buscar == '':
        print('ERROR - Debe ingresar un nombre')
    else:
        nombre_valido = True

# Si el estudiante está en la lista, se muestra la posición por pantalla
if estudiante_a_buscar in estudiantes:
    print(f'{estudiante_a_buscar} está en la posición {estudiantes.index(estudiante_a_buscar) + 1}\n')
# En caso contrario, se indica en pantalla que el estudiante no está en la lista
else:
    print(f'{estudiante_a_buscar} no está en la lista\n')



# EJERCICIO 12 - Ordenar lista de 8 números
print('\n-----EJERCICIO 12 -Ordenar lista de 8 números-----')

# Se importa el módulo random para poder generar números aleatorios
import random

# Se define una constante para almacenar la cantidad de números
CANT_NUMEROS = 8

# Se define la lista para almacenar los valores
lista_original = []

# Se cargan valores aleatorios en la lista
for _ in range(CANT_NUMEROS):
    lista_original.append(random.randint(1,100))

# Se utiliza la función sorted() para obtener una lista ordenada de menor a mayor
lista_menor_mayor = sorted(lista_original)

# Se utiliza el método copy() para generar una copia y luego el método reverse para obtener la lista de mayor a menor
lista_mayor_menor = lista_menor_mayor.copy()
lista_mayor_menor.reverse()

# Se muestra la lista en pantalla
print('Lista original:')
for i in range(CANT_NUMEROS):
    print(lista_original[i], end = '\t')

print('\n-------------------------------------------------------------')

# Se muestra la lista ordenada de menor a mayor
print('Ordenada de menor a mayor:')
for i in range(CANT_NUMEROS):
    print(lista_menor_mayor[i], end = '\t')

print('\n-------------------------------------------------------------')

# Se muestra la lista ordenada de mayor a menor
print('Ordenada de mayor a menor:')
for i in range(CANT_NUMEROS):
    print(lista_mayor_menor[i], end = '\t')
print('\n-------------------------------------------------------------')



# EJERCICIO 13 - Puntajes de videojuegos
print('\n-----EJERCICIO 13 - Puntajes de videojuegos-----')

# Se define la lista provista por el enunciado
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# Se muestra la lista en pantalla
print('Lista de puntajes:')
for i in range(len(puntajes)):
    print(puntajes[i], end = '\t')
print('\n----------------------------------------------------')

# Se utiliza la función sorted() para obtener una lista ordenada de menor a mayor
ranking = sorted(puntajes)

# Se utiliza el método reverse() para invertir el ranking y que quede ordenado de mayor a menor
ranking.reverse()

# Se muestra el ranking en pantalla
print('Ranking:')
for i in range(len(puntajes)):
    print(f'{i + 1}: {ranking[i]}')
print('----------------------------------------------------')

# Se utilizan las funciones max() y min() para mostrar los puntajes más alto y más bajo
print(f'Puntaje más alto: {max(puntajes)}')
print(f'Puntaje más bajo: {min(puntajes)}')

# Se utiliza el método index() para indicar la posición en el ranking del puntaje 990
if 990 in ranking:
    print(f'Posición del puntaje 990: {ranking.index(990) + 1}\n')