# EJERCICIO 4 - Escape Room: La Bóveda
print('\n---Ejercicio 4 - Escape Room: La Bóveda---\n')

# 3 cerraduras
# energia
# tiempo

# Valores iniciales por consigna
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# La bandera de bloqueo se inicializa con valor falso
bloqueo = False

# El contador de cerraduras forzadas se inicializa en cero
cont_forzadas = 0

# Se inicializa una bandera auxiliar con valor falso para luego validar el nombre del operador ingresado
nombre_agente_valido = False

# El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
while nombre_agente_valido == False:
    # Se solicita al usuario el nombre de agente, se eliminan espacios en extremos y se aplica formato de mayúsculas iniciales
    nombre_agente = input('Ingrese su nombre de agente: ').strip().upper()
    # Si el nombre del operador es alfabético, se asigna valor verdadero a la bandera
    if nombre_agente.isalpha():
        nombre_agente_valido = True
    # Si no se cumple la condición, esto se indica en pantalla
    else:
        print('- ERROR - Ingrese un nombre válido (letras)')

# Se muestra en pantalla las estadísticas iniciales
print(f'\nCerraduras: {cerraduras_abiertas}/3')
if alarma == True:
    print(f'Alarma: ¡ACTIVA!', end='')
else:
    print(f'Alarma: -', end='')
print(f'\nForzadas consecutivas: {cont_forzadas} / Código: {codigo_parcial}')
print(f'Energía: {energia} / Tiempo: {tiempo}')

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and bloqueo == False:
    # Se muestra el menú de opciones
    print('1) Forzar, 2) Hackear, 3) Descansar')

    # Se inicializa una bandera auxiliar con valor falso para luego validar la opción ingresada
    opcion_valida = False

    # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
    while opcion_valida == False:
        # Se solicita al usuario ingresar un número de opción y se eliminan espacios en extremos
        opcion = input('Opción: ').strip()
        
        # Si la opción es un valor numérico, se hace la comprobación de rango entero
        if opcion.isdigit():
            # Si el rango entero es correcto, se asigna valor verdadero a la bandera
            if 1 <= int(opcion) <= 3:
                opcion_valida = True
            # Si el valor está fuera de rango, se indica el error en pantalla
            else:
                print('- ERROR - Ingrese un valor dentro del rango')
        # Si no es un dígito se indica el error en pantalla
        else:
            print('- ERROR - Ingrese un dígito válido')

    # Se utiliza una estructura match-case para realizar la acción correspondiente a la opción seleccionada
    match opcion:
        case '1': # FORZAR CERRADURA
            # Se incrementa el contador de cerraduras forzadas consecutivas
            cont_forzadas += 1
            # Se paga el costo de energía y tiempo for forzar cerradura
            energia -= 20
            tiempo -= 2
            # Los siguientes efectos solo se producen si no hay alarma activa
            if alarma == False:
                # Si se alcanzaron las 3 cerraduras forzadas consecutivas, la cerradura se traba y suena la alarma
                if cont_forzadas == 3:
                    alarma = True
                # Si la energía está por debajo de 40 hay "riesgo de alarma"
                elif energia < 40:
                    print('\n¡Hay riesgo de alarma!')

                    # Se inicializa una bandera auxiliar con valor falso para luego validar la opción ingresada
                    numero_valido = False

                    # El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
                    while numero_valido == False:
                        # Se solicita al usuario ingresar un número de opción y se eliminan espacios en extremos
                        numero = input('Ingrese un número del 1 al 3: ').strip()
                        
                        # Si la opción es un valor numérico, se hace la comprobación de rango entero
                        if numero.isdigit():
                            # Si el rango entero es correcto, se asigna valor verdadero a la bandera
                            if 1 <= int(numero) <= 3:
                                numero_valido = True
                            # Si el valor está fuera de rango, se indica el error en pantalla
                            else:
                                print('- ERROR - Ingrese un valor dentro del rango')
                        # Si no es un dígito se indica el error en pantalla
                        else:
                            print('- ERROR - Ingrese un dígito válido')
                    # Si el número ingresado es 3, la alarma se activa
                    if numero == '3':
                        alarma = True
                # Si no hubo disparo de alarmas, se abre 1 cerradura
                else:
                    cerraduras_abiertas += 1
            # Regla de bloqueo
            if alarma == True and tiempo <= 3:
                bloqueo = True

        case '2': # HACKEAR PANEL
            # Se reinicia el contador de cerraduras forzadas
            cont_forzadas = 0
            # Se realizan 4 pasos de suma de letra para el código parcial
            for paso in range(4):
                codigo_parcial += 'A'
            # Si la longitud del código parcial es mayor o igual que 8, se abre 1 cerradura y se reinicia el código parcial
            if len(codigo_parcial) >= 8:
                cerraduras_abiertas += 1
                codigo_parcial = ''
            # Se paga el costo de energía y tiempo por hackear panel
            energia -= 10
            tiempo -= 3
            # Regla de bloqueo
            if alarma == True and tiempo <= 3:
                bloqueo = True

        case '3': # DESCANSAR
            # Se reinicia el contador de cerraduras forzadas
            cont_forzadas = 0
            # Se gana energía con un tope de 100
            energia += 15
            if energia > 100:
                energia = 100
            # Se paga el costo en tiempo por descansar
            tiempo -= 1
            # Si la alarma está encendida se paga un costo en energía
            if alarma == True:
                energia -= 10
            # Regla de bloqueo
            if alarma == True and tiempo <= 3:
                bloqueo = True

    # Se muestra en pantalla las estadísticas
    print(f'\nCerraduras: {cerraduras_abiertas}/3')
    if alarma == True:
        print(f'Alarma: ¡ACTIVA!', end='')
    else:
        print(f'Alarma: -', end='')
    print(f'\nForzadas consecutivas: {cont_forzadas} / Código: {codigo_parcial}')
    print(f'Energía: {energia} / Tiempo: {tiempo}')


# MENSAJE DE CIERRE
if cerraduras_abiertas == 3 and energia > 0 and tiempo > 0:
    print('- ¡VICTORIA!\nAbriste las 3 cerraduras')
else:
    print(f'- ¡DERROTA!')
    if tiempo <= 0:
        print('- Se agotó el TIEMPO.')
    if energia <= 0:
        print('- Se agotó tu ENERGÍA.')
    if bloqueo == True:
        print('- Hubo un BLOQUEO POR ALARMA.')
print('')
