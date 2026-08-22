# EJERCICIO 3 - Agenda de Turnos con Nombres
print('\n---Ejercicio 3 - Agenda de Turnos con Nombres---\n')

# Se inicializa una bandera auxiliar con valor falso para luego validar el nombre del operador ingresado
nombre_operador_valido = False

# El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
while nombre_operador_valido == False:
    # Se solicita al usuario el nombre del operador, se eliminan espacios en extremos y se aplica formato de mayúsculas iniciales
    nombre_operador = input('Ingrese el nombre del operador: ').strip().upper()
    # Si el nombre del operador es alfabético, se asigna valor verdadero a la bandera
    if nombre_operador.isalpha():
        nombre_operador_valido = True
    # Si no se cumple la condición, esto se indica en pantalla
    else:
        print('- ERROR - Ingrese un nombre válido (letras)')

# Se muestra el menú de opciones
print('''
- MENÚ -
1) Reservar turno
2) Cancelar turno (por nombre)
3) Ver agenda del día
4) Ver resumen general
5) Cerrar sistema''')

# Se inicializan las variables de turnos con valor vacío
lunes_1 = ''
lunes_2 = ''
lunes_3 = ''
lunes_4 = ''
martes_1 = ''
martes_2 = ''
martes_3 = ''

# Se inicializa la variable opcion con un valor fuera de rango
opcion = ''

# El lazo de menú se repite mientras no se seleccione la opción 5 (cerrar sistema)
while opcion != '5':

    # Se inicializa una bandera auxiliar con valor falso para luego validar la opción ingresada
    opcion_valida = False

    # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
    while opcion_valida == False:
        # Se solicita al usuario ingresar un número de opción y se eliminan espacios en extremos
        opcion = input('\nOpción: ').strip()
        
        # Si la opción es un valor numérico, se hace la comprobación de rango entero
        if opcion.isdigit():
            # Si el rango entero es correcto, se asigna valor verdadero a la bandera
            if 1 <= int(opcion) <= 5:
                opcion_valida = True
            # Si el valor está fuera de rango, se indica el error en pantalla
            else:
                print('- ERROR - Ingrese un valor dentro del rango')
        # Si no es un dígito se indica el error en pantalla
        else:
            print('- ERROR - Ingrese un dígito válido')

    # Se utiliza una estructura match-case para realizar la acción correspondiente a la opción seleccionada
    match opcion:
        case '1':
            # Se inicializa una bandera auxiliar con valor falso para luego validar la opción ingresada
            opcion_dia_valida = False

            # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
            while opcion_dia_valida == False:
                # Se solicita al usuario ingresar un número de opción y se eliminan espacios en extremos
                opcion_dia = input('\nReservar - Elegir día (1=Lunes, 2=Martes): ').strip()
                
                # Si la opción es un valor numérico, se hace la comprobación de rango entero
                if opcion_dia.isdigit():
                    # Si el rango entero es correcto, se asigna valor verdadero a la bandera
                    if 1 <= int(opcion_dia) <= 2:
                        opcion_dia_valida = True
                    # Si el valor está fuera de rango, se indica el error en pantalla
                    else:
                        print('- ERROR - Ingrese un valor dentro del rango')
                # Si no es un dígito se indica el error en pantalla
                else:
                    print('- ERROR - Ingrese un dígito válido')

            # Se inicializa una bandera auxiliar con valor falso para luego validar el nombre del paciente ingresado
            nombre_paciente_valido = False

            # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
            while nombre_paciente_valido == False:
                # Se solicita al usuario el nombre del paciente, se eliminan espacios en extremos y se aplica formato de mayúsculas iniciales
                nombre_paciente = input('Ingrese el nombre del paciente: ').strip().upper()
                # Si el nombre del paciente es alfabético, se asigna valor verdadero a la bandera
                if nombre_paciente.isalpha():
                    nombre_paciente_valido = True
                # Si no se cumple la condición, esto se indica en pantalla
                else:
                    print('- ERROR - Ingrese un nombre válido (letras)')

            # Si el paciente eligió la opción 1...
            if opcion_dia == '1':
                # Se comprueba que el paciente no tenga un turno en ese día
                if lunes_1 == nombre_paciente or lunes_2 == nombre_paciente or lunes_3 == nombre_paciente or lunes_4 == nombre_paciente:
                    print('El paciente ya tiene un turno programado ese día')
                # Si no había turno existente se programa el primer turno disponible
                else:
                    if lunes_1 == '':
                        lunes_1 = nombre_paciente
                        print(f'Se programó el turno 1 del lunes para {nombre_paciente}')
                    elif lunes_2 == '':
                        lunes_2 = nombre_paciente
                        print(f'Se programó el turno 2 del lunes para {nombre_paciente}')
                    elif lunes_3 == '':
                        lunes_3 = nombre_paciente
                        print(f'Se programó el turno 3 del lunes para {nombre_paciente}')
                    elif lunes_4 == '':
                        lunes_4 = nombre_paciente
                        print(f'Se programó el turno 4 del lunes para {nombre_paciente}')
                    # Si no se pudo asignar el turno, se indica que no quedaban turnos disponibles
                    else:
                        print('No quedan turnos disponibles el día lunes')

            # Si el paciente eligió la opción 2...
            elif opcion_dia == '2':
                # Se comprueba que el paciente no tenga un turno en ese día
                if martes_1 == nombre_paciente or martes_2 == nombre_paciente or martes_3 == nombre_paciente:
                    print('El paciente ya tiene un turno programado ese día')
                # Si no había turno existente se programa el primer turno disponible
                else:
                    if martes_1 == '':
                        martes_1 = nombre_paciente
                        print(f'Se programó el turno 1 del martes para {nombre_paciente}')
                    elif martes_2 == '':
                        martes_2 = nombre_paciente
                        print(f'Se programó el turno 2 del martes para {nombre_paciente}')
                    elif martes_3 == '':
                        martes_3 = nombre_paciente
                        print(f'Se programó el turno 3 del martes para {nombre_paciente}')
                    # Si no se pudo asignar el turno, se indica que no quedaban turnos disponibles
                    else:
                        print('No quedan turnos disponibles el día martes')

        case '2':
            # Se inicializa una bandera auxiliar con valor falso para luego validar la opción ingresada
            opcion_dia_valida = False

            # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
            while opcion_dia_valida == False:
                # Se solicita al usuario ingresar un número de opción y se eliminan espacios en extremos
                opcion_dia = input('\nCancelar - Elegir día (1=Lunes, 2=Martes): ').strip()
                
                # Si la opción es un valor numérico, se hace la comprobación de rango entero
                if opcion_dia.isdigit():
                    # Si el rango entero es correcto, se asigna valor verdadero a la bandera
                    if 1 <= int(opcion_dia) <= 2:
                        opcion_dia_valida = True
                    # Si el valor está fuera de rango, se indica el error en pantalla
                    else:
                        print('- ERROR - Ingrese un valor dentro del rango')
                # Si no es un dígito se indica el error en pantalla
                else:
                    print('- ERROR - Ingrese un dígito válido')

            # Se inicializa una bandera auxiliar con valor falso para luego validar el nombre del paciente ingresado
            nombre_paciente_valido = False

            # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
            while nombre_paciente_valido == False:
                # Se solicita al usuario el nombre del paciente, se eliminan espacios en extremos y se aplica formato de mayúsculas iniciales
                nombre_paciente = input('Ingrese el nombre del paciente: ').strip().upper()
                # Si el nombre del paciente es alfabético, se asigna valor verdadero a la bandera
                if nombre_paciente.isalpha():
                    nombre_paciente_valido = True
                # Si no se cumple la condición, esto se indica en pantalla
                else:
                    print('- ERROR - Ingrese un nombre válido (letras)')

            # Si el paciente eligió la opción 1...
            if opcion_dia == '1':
                # En caso de haber un turno programado para el paciente, se cancela y se indica en pantalla
                if lunes_1 == nombre_paciente:
                    lunes_1 = ''
                    print('Se canceló el turno 1 del lunes')
                elif lunes_2 == nombre_paciente:
                    lunes_2 = ''
                    print('Se canceló el turno 2 del lunes')
                elif lunes_3 == nombre_paciente:
                    lunes_3 = ''
                    print('Se canceló el turno 3 del lunes')
                elif lunes_4 == nombre_paciente:
                    lunes_4 = ''
                    print('Se canceló el turno 4 del lunes')
                # Si no se encontró un turno programado, esto se indica en pantalla
                else:
                    print('Este paciente no tenía turnos programados el día lunes')

            # Si el paciente eligió la opción 2...
            elif opcion_dia == '2':
                # En caso de haber un turno programado para el paciente, se cancela y se indica en pantalla
                if martes_1 == nombre_paciente:
                    martes_1 = ''
                    print('Se canceló el turno 1 del martes')
                elif martes_2 == nombre_paciente:
                    martes_2 = ''
                    print('Se canceló el turno 2 del martes')
                elif martes_3 == nombre_paciente:
                    martes_3 = ''
                    print('Se canceló el turno 3 del martes')
                # Si no se encontró un turno programado, esto se indica en pantalla
                else:
                    print('Este paciente no tenía turnos programados el día martes')
        case '3':
            # Se inicializa una bandera auxiliar con valor falso para luego validar la opción ingresada
            opcion_dia_valida = False

            # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
            while opcion_dia_valida == False:
                # Se solicita al usuario ingresar un número de opción y se eliminan espacios en extremos
                opcion_dia = input('\nAgenda - Elegir día (1=Lunes, 2=Martes): ').strip()
                
                # Si la opción es un valor numérico, se hace la comprobación de rango entero
                if opcion_dia.isdigit():
                    # Si el rango entero es correcto, se asigna valor verdadero a la bandera
                    if 1 <= int(opcion_dia) <= 2:
                        opcion_dia_valida = True
                    # Si el valor está fuera de rango, se indica el error en pantalla
                    else:
                        print('- ERROR - Ingrese un valor dentro del rango')
                # Si no es un dígito se indica el error en pantalla
                else:
                    print('- ERROR - Ingrese un dígito válido')

            # Si el operador eligió la opción 1...
            if opcion_dia == '1':
                # Se muestra los turnos en pantalla
                print('- AGENDA DEL DÍA LUNES-')

                if lunes_1 == '':
                    print('Turno 1: LIBRE')
                else:
                    print(f'Turno 1: {lunes_1}')

                if lunes_2 == '':
                    print('Turno 2: LIBRE')
                else:
                    print(f'Turno 2: {lunes_2}')

                if lunes_3 == '':
                    print('Turno 3: LIBRE')
                else:
                    print(f'Turno 3: {lunes_3}')

                if lunes_4 == '':
                    print('Turno 4: LIBRE')
                else:
                    print(f'Turno 4: {lunes_4}')

            # Si el operador eligió la opción 2...
            elif opcion_dia == '2':
                # Se muestra los turnos en pantalla
                print('- AGENDA DEL DÍA MARTES-')

                if martes_1 == '':
                    print('Turno 1: LIBRE')
                else:
                    print(f'Turno 1: {martes_1}')

                if martes_2 == '':
                    print('Turno 2: LIBRE')
                else:
                    print(f'Turno 2: {martes_2}')

                if martes_3 == '':
                    print('Turno 3: LIBRE')
                else:
                    print(f'Turno 3: {martes_3}')

        case '4':
                # Se muestra el resumen general en pantalla
                print('- RESUMEN GENERAL-')

                if lunes_1 == '':
                    print('Lunes 1: LIBRE')
                else:
                    print(f'Lunes 1: {lunes_1}')

                if lunes_2 == '':
                    print('Lunes 2: LIBRE')
                else:
                    print(f'Lunes 2: {lunes_2}')

                if lunes_3 == '':
                    print('Lunes 3: LIBRE')
                else:
                    print(f'Lunes 3: {lunes_3}')

                if lunes_4 == '':
                    print('Lunes 4: LIBRE')
                else:
                    print(f'Lunes 4: {lunes_4}')

                print('---------------')

                if martes_1 == '':
                    print('Martes 1: LIBRE')
                else:
                    print(f'Martes 1: {martes_1}')

                if martes_2 == '':
                    print('Martes 2: LIBRE')
                else:
                    print(f'Martes 2: {martes_2}')

                if martes_3 == '':
                    print('Martes 3: LIBRE')
                else:
                    print(f'Martes 3: {martes_3}')

                # Se inicializa un contador de turnos disponibles en cero
                turnos_disponibles = 0
                # Se inicializa un contador de turnos en lunes
                turnos_lunes = 0
                # Se inicializa un contador de turnos en martes
                turnos_martes = 0

                # Se cuenta analizando turno por turno
                if lunes_1 == '':
                    turnos_disponibles += 1
                else:
                    turnos_lunes += 1
                if lunes_2 == '':
                    turnos_disponibles += 1
                else:
                    turnos_lunes += 1
                if lunes_3 == '':
                    turnos_disponibles += 1
                else:
                    turnos_lunes += 1
                if lunes_4 == '':
                    turnos_disponibles += 1
                else:
                    turnos_lunes += 1
                if martes_1 == '':
                    turnos_disponibles += 1
                else:
                    turnos_martes += 1
                if martes_2 == '':
                    turnos_disponibles += 1
                else:
                    turnos_martes += 1
                if martes_3 == '':
                    turnos_disponibles += 1
                else:
                    turnos_martes += 1

                # Se indica en pantalla la cantidad de turnos ocupados y disponibles
                print('--------------------')
                print(f'Turnos Ocupados: {7 - turnos_disponibles}')
                print(f'Turnos Disponibles: {turnos_disponibles}')

                # Se indica en pantalla el día con más turnos o empate
                if turnos_lunes > turnos_martes:
                    print(f'Día con más turnos: Lunes ({turnos_lunes})')
                elif turnos_martes > turnos_lunes:
                    print(f'Día con más turnos: Martes ({turnos_martes})')
                else:
                    print(f'Día con más turnos: Empate ({turnos_lunes})')

        case '5':
            # Se muestra mensaje de despedida de menú
            print('Menú cerrado\n')