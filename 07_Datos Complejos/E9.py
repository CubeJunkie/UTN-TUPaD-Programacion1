# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se declara un diccionario con la información de agenda
agenda = {
    ('lunes', '10:00'): 'Reunión',
    ('martes', '15:00'): 'Clase de inglés'
}

# Se declara la variable que almacenará la opción de menú seleccionada por el usuario
opcion = ''

# El bucle de menú se repite mientras no se seleccione la opción para salir
while opcion != '4':
    # Se muestra el menú de opciones en pantalla
    print('------------------------')
    print('---MENÚ DE AGENDA---')
    print('1) Consultar actividad')
    print('2) Salir')
    print('------------------------')

    # Se le solicita al usuario ingresar una opción
    opcion = ing.string_opcion(('1', '2'))

    # Se utiliza una estructura case-match para ejecutar la opción seleccionada
    match opcion:
        case '1':
            print('------------------------')
            print('CONSULTA DE ACTIVIDADES')
            # Se solicita al usuario el día a consultar
            dia = ing.string_no_vacio('Día').lower()
            # Se solicita al usuario el horario a consultar
            hora = ing.string_no_vacio('Hora')
            # Si no hay coincidencias en la agenda, se muestra un mensaje
            if agenda.get((dia, hora)) is None:
                print('No se encontraron entradas en la agenda.')
            # En caso contrario se muestra la actividad correspondiente
            else:
                print(f'Actividad: {agenda.get((dia, hora))}')
        case '2':
            # Cuando se selecciona la opción salir se muestra un mensaje de despedida por pantalla
            print('----FIN DEL PROGRAMA----\n')
            exit()

    # Pausa antes de mostrar el menú nuevamente
    print('------------------------')
    input('Presione enter para continuar...')