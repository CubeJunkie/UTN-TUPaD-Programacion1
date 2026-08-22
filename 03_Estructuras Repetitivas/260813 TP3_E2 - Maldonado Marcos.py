# EJERCICIO 2 - Acceso al Campus y Menú Seguro
print('\n---Ejercicio 2 - Acceso al Campus y Menú Seguro---')

# Se definen las credenciales correctas
USUARIO_CORRECTO = 'alumno'
CLAVE_CORRECTA = 'python123'
ESTADO_DE_INSCRIPCION = 'Inscripto'
FRASE_MOTIVACIONAL = '¡Vamos que se puede!'

# Se define la cantidad de intentos permitidos
INTENTOS_PERMITIDOS = 3

# Se inicializa una bandera con valor falso para validar si el login fue exitoso
login_exitoso = False

# Se repite el bucle de ingresos de datos en función de la cantidad de intentos permitidos
for intento in range(1, INTENTOS_PERMITIDOS + 1):
    # Se muestra en pantalla el número de intento actual
    print(f'\nINICIO DE SESION - INTENTO {intento} DE {INTENTOS_PERMITIDOS}')

    # Se pide ingresar el usuario
    usuario = input('Usuario: ')

    # Se pide la clave
    clave = input('Clave: ')

    # Si las credenciales son correctas se asigna valor verdadero a la bandera de login exitoso y se sale del lazo de validación de credenciales
    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
        login_exitoso = True
        print('Acceso concedido')
        break
    else:
        print('- ERROR - Credenciales inválidas')
# Si se agotan los intentos sin ingresar credenciales correctas, se indica el bloqueo de cuenta
else:
    print('- CUENTA BLOQUEADA -\n')

# Solo se continúa si hubo login exitoso
if login_exitoso == True:

    # Se muestra el menú de opciones
    print('''
- MENÚ -
1) Estado de inscripción
2) Cambiar clave
3) Mostrar mensaje motivacional
4) Salir''')

    # Se inicializa la variable opcion con un valor fuera de rango
    opcion = ''

    # El lazo de menú se repite mientras no se seleccione la opción 4 (salir)
    while opcion != '4':

        # Se inicializa una bandera auxiliar con valor falso para luego validar la opción ingresada
        opcion_valida = False

        # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
        while opcion_valida == False:
            # Se solicita al usuario ingresar un número de opción y se eliminan espacios en extremos
            opcion = input('\nOpción: ').strip()
            
            # Si la opción es un valor numérico, se hace la comprobación de rango entero
            if opcion.isdigit():
                # Si el rango entero es correcto, se asigna valor verdadero a la bandera
                if 1 <= int(opcion) <= 4:
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
                # Se muestra el estado de inscripción
                print(f'Estado de inscripción: {ESTADO_DE_INSCRIPCION}')
            case '2':
                # Se solicita una clave nueva
                # Se inicializa una bandera con valor falso para luego validar la nueva clave
                clave_nueva_valida = False

                # Se repite el lazo de ingreso mientras la bandera tenga valor falso
                while clave_nueva_valida == False:
                    # Se pide al usuario ingresar una nueva clave
                    clave_nueva = input('Nueva clave (min. 6 caracteres): ')

                    # Si la clave tiene al menos 6 caracteres, se asigna valor verdadero a la bandera
                    if len(clave_nueva) >= 6:
                        clave_nueva_valida = True
                    # En caso contrario se indica el error en pantalla
                    else:
                        print('- ERROR - La clave debe tener 6 caracteres como mínimo')

                # Se pide confirmación de clave nueva y se chequea que coincidan
                confirmacion_clave_nueva = input('Una vez más para confirmar: ')
                if clave_nueva == confirmacion_clave_nueva:
                    CLAVE_CORRECTA = clave_nueva
                    print(f'La nueva clave es: {CLAVE_CORRECTA}')
                # Si la confirmación no coincide, se indica el error en pantalla y se cancela el cambio
                else:
                    print('La confirmación de clave no coincide. Cambio cancelado')
                
            case '3':
                # Se muestra un mensaje motivacional
                print(f'{FRASE_MOTIVACIONAL}')
            case '4':
                # Se muestra mensaje de despedida de menú
                print('Menú cerrado\n')