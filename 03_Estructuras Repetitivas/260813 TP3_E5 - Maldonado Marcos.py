# EJERCICIO 5 - Escape Room: La Arena del Gladiador
print('\n---Ejercicio 5 - Escape Room: La Arena del Gladiador---\n')

# Mensaje de bienvenida
print('--- BIENVENIDO A LA ARENA ---')

# Se inicializa una bandera auxiliar con valor falso para luego validar el nombre del operador ingresado
nombre_gladiador_valido = False

# El lazo de ingreso de datos se repite mientras la bandera de validación sea falsa
while nombre_gladiador_valido == False:
    # Se solicita al usuario el nombre de gladiador, se eliminan espacios en extremos y se aplica formato de mayúsculas iniciales
    nombre_gladiador = input('Nombre del Gladiador: ').strip().capitalize()
    # Si el nombre del operador es alfabético, se asigna valor verdadero a la bandera
    if nombre_gladiador.isalpha():
        nombre_gladiador_valido = True
    # Si no se cumple la condición, esto se indica en pantalla
    else:
        print('- ERROR - Solo se permiten letras')

# Valores iniciales por consigna
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
db_ataque_pesado = 15
db_enemigo = 12
turno_gladiador = True

# La batalla continuará mientras los dos combatientes tengan energía
while vida_gladiador > 0 and vida_enemigo > 0:
    # Turno del gladiador
    if turno_gladiador == True:
        # Se muestran en pantalla las estadísticas
        print('==============')
        print(f'{nombre_gladiador} (HP:{vida_gladiador}) vs Enemigo: (HP:{vida_enemigo}) | Pociones: {pociones}')

        # Se muestra el menú de opciones
        print('1) Ataque Pesado, 2) Ráfaga Veloz, 3) Curar')

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
            case '1': # Ataque Pesado
                # Si la vida del enemigo es menor que 20, el daño final recibe un multiplicador de 1.5
                if vida_enemigo < 20:
                    dmg_final = db_ataque_pesado * 1.5
                # En caso contrario, el daño final es igual al daño base
                else:
                    dmg_final = db_ataque_pesado
                # Se resta el daño final a la energía del enemigo y se indica esto por pantalla
                vida_enemigo -= dmg_final
                print(f'¡Atacaste al enemigo por {dmg_final:.1f} puntos de daño!')

            case '2': # Ráfaga Veloz
                # Se usa un lazo for para realizar la ráfaga de 3 golpes de 5 puntos y se indica esto por pantalla
                print('¡Inicias una ráfaga de golpes!')
                for golpe in range(3):
                    vida_enemigo -= 5
                    print('> Golpe conectado por 5 de daño')

            case '3': # Curar
                # Si aún quedan pociones, se utiliza una elevando la energía del gladiador
                if pociones > 0:
                    vida_gladiador += 30
                    pociones -= 1
                    print('¡La poción te dio 30 puntos de HP adicionales!')
                # Si no quedan pociones, se indica esto por pantalla
                else:
                    print('¡No quedan pociones!')
        # Termina el turno del gladiador
        turno_gladiador = False

    # Turno del enemigo
    else:
        # Los puntos de ataque base del enemigo se sustraen de la energía del gladiador, y esto se indica por pantalla 
        vida_gladiador -= db_enemigo
        print(f'¡El enemigo contrataca por {db_enemigo} puntos de daño!')
        # Termina el turno del enemigo
        turno_gladiador = True

# Fin del juego
# Si la energía del gladiador es mayor que cero, se declara la victoria
if vida_gladiador > 0:
    print(f'¡VICTORIA! {nombre_gladiador} ha ganado la batalla.')
# En caso contrario, se declara la derrota
else:
    print(f'DERROTA. Has caído en combate.')
print('')