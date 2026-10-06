# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se declara una lista de asistencias con los datos de la consigna:
lista_asistencias = ['Ana', 'Luis', 'Ana', 'María', 'Luis', 'Pedro', 'Ana']

# Se muestra la lista de asistencias en pantalla
print('LISTA DE ASISTENCIAS')
print(lista_asistencias)

# Se utiliza la función set() para convertir la lista en un conjunto
conjunto_asistentes = set(lista_asistencias)

# Se declara un diccionario para almacenar los datos de conteo de asistencias
recuento = {}

# Se recorre el conjunto de asistentes con un lazo for
for nombre in conjunto_asistentes:
    # Se cuentan las apariciones del nombre en la lista de asistencias utilizando el método .count() 
    apariciones = lista_asistencias.count(nombre)
    # Se agrega un par nombre-apariciones al diccionario de recuento
    recuento[nombre] = apariciones

# Se muestra por pantalla el recuento de asistencias
print(f'Recuento: {recuento}')