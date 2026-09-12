def int_valido(nombre='Número entero'):
    '''Se pide al usuario ingresar un entero y se repite hasta obtener un valor válido'''
    # Se inicializa una bandera de validación de datos con valor falso
    dato_valido = False
    # Se repite el bucle de ingreso de datos mientras la bandera tenga valor falso
    while not dato_valido:
        string_ingresado = input(f'{nombre}: ').strip()   
        # Si el campo está vacío, se reinicia el bucle  
        if string_ingresado == '':
            print('---Error: Campo vacío---')
            continue
        # Se inicializa una bandera de dígitos detectados con valor falso
        digito_detectado = False
        # Se inicializa una bandera de caracteres inválidos con valor falso
        caracteres_invalidos = False
        # Se verifica el valor ingresado caracter por caracter
        for i, caracter in enumerate(string_ingresado):
            if caracter == '-':
                if i != 0:
                    caracteres_invalidos = True
                    break
            # Si el caracter no es guion ni dígito, se asigna valor verdadero a la bandera de caracteres inválidos
            elif not caracter.isdigit():
                caracteres_invalidos = True
                break
            # En caso de no cumplirse lo anterior, es dígito así que se asigna valor verdadero a la bandera de dígito detectado
            else:
                digito_detectado = True
        # Si se detectaron caracteres inválidos, se reinicia el bucle
        if caracteres_invalidos:
            print('---Error: Se detectaron caracteres inválidos.---')
            continue
        # Si no se detectaron dígitos, se reinicia el bucle
        if not digito_detectado:
            print('---Error: El valor ingresado debe incluir dígitos.---')
            continue
        # Si se sortearon las condiciones de validación, se convierte el string en int y se asigna valor verdadero a la bandera de validación
        entero_ingresado = int(string_ingresado)
        dato_valido = True
    return entero_ingresado

def int_positivo(nombre='Número entero (>0)'):
    '''Se pide al usuario ingresar un entero mayor que cero y se repite hasta obtener un valor válido'''
    # Se inicializa una bandera de validación de datos con valor falso
    dato_valido = False
    while not dato_valido:
        valor = int_valido(nombre)
        if not valor > 0:
            print('---Error: Debe ingresar un valor mayor que cero')
            continue
        dato_valido = True
    return valor

def int_positivo_o_cero(nombre='Número entero (≥0)'):
    '''Se pide al usuario ingresar un entero mayor o igual que cero y se repite hasta obtener un valor válido'''
    # Se inicializa una bandera de validación de datos con valor falso
    dato_valido = False
    while not dato_valido:
        valor = int_valido(nombre)
        if not valor >= 0:
            print('---Error: Debe ingresar un valor mayor o igual que cero')
            continue
        dato_valido = True
    return valor


def float_valido(nombre='Número decimal'):
    '''Se pide al usuario ingresar un float y se repite hasta obtener un valor válido'''
    # Se inicializa una bandera de validación de datos con valor falso
    dato_valido = False
    # Se repite el bucle de ingreso de datos mientras la bandera tenga valor falso
    while not dato_valido:
        string_ingresado = input(f'{nombre}: ').strip()
        # Si el campo está vacío, se reinicia el bucle 
        if string_ingresado == '':
            print('---Error: Campo vacío.---')
            continue
        # Se inicializa un contador de puntos en cero
        puntos = 0
        # Se inicializa una bandera de puntos extra detectados con valor falso
        punto_extra_detectado = False
        # Se inicializa una bandera de dígitos detectados con valor falso
        digito_detectado = False
        # Se inicializa una bandera de caracteres inválidos con valor falso
        caracteres_invalidos = False
        # Se verifica el valor ingresado caracter por caracter
        for i, caracter in enumerate(string_ingresado):
            if caracter == '-':
                if i != 0:
                    caracteres_invalidos = True
                    break
            # Se cuentan los puntos y si hay más de uno se asigna valor verdadero a la bandera de punto extra detectado
            elif caracter == '.':
                puntos += 1
                if puntos > 1:
                    punto_extra_detectado = True
                    break
            # Si el caracter no es guion, punto ni dígito, se asigna valor verdadero a la bandera de caracteres inválidos
            elif not caracter.isdigit():
                caracteres_invalidos = True
                break
            # En caso de no cumplirse lo anterior, es dígito así que se asigna valor verdadero a la bandera de dígito detectado
            else:
                digito_detectado = True
        # Si se detectaron caracteres inválidos, se reinicia el bucle
        if caracteres_invalidos:
            print('---Error: Se detectaron caracteres inválidos.---')
            continue
        # Si no se detectaron dígitos, se reinicia el bucle
        if not digito_detectado:
            print('---Error: El valor ingresado debe incluir dígitos.---')
            continue
        # Si se detectaron puntos extra, se reinicia el bucle
        if punto_extra_detectado:
            print('---Error: Se detectó más de un punto.---')
            continue
        # Si se sortearon las condiciones de validación, se convierte el string en float y se asigna valor verdadero a la bandera de validación
        float_ingresado = float(string_ingresado)
        dato_valido = True
    return float_ingresado


def float_positivo(nombre='Número decimal (>0.0)'):
    '''Se pide al usuario ingresar un float mayor que cero y se repite hasta obtener un valor válido'''
    # Se inicializa una bandera de validación de datos con valor falso
    dato_valido = False
    while not dato_valido:
        valor = float_valido(nombre)
        if not valor > 0:
            print('---Error: Debe ingresar un valor mayor que cero')
            continue
        dato_valido = True
    return valor


def float_positivo_o_cero(nombre='Número decimal (≥0.0)'):
    '''Se pide al usuario ingresar un float mayor o igual que cero y se repite hasta obtener un valor válido'''
    # Se inicializa una bandera de validación de datos con valor falso
    dato_valido = False
    while not dato_valido:
        valor = float_valido(nombre)
        if not valor >= 0:
            print('---Error: Debe ingresar un valor mayor o igual que cero')
            continue
        dato_valido = True
    return valor


def string_no_vacio(nombre='Cadena de caracteres'):
    '''Se pide al usuario ingresar una cadena de caracteres, se aplica strip() y se verifica que no esté vacía. Se repite hasta obtener un valor válido'''
    # Se inicializa una bandera de validación de datos con valor falso
    dato_valido = False
    # Se repite el bucle de ingreso de datos mientras la bandera tenga valor falso
    while not dato_valido:
        string_ingresado = input(f'{nombre}: ').strip()
        if string_ingresado == '':
            print('---Error: Campo vacío---')
            continue
        dato_valido = True
    return string_ingresado.strip()