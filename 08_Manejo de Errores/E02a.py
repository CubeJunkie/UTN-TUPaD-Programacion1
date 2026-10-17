# EJERCICIO 2 - Corregir sin excepciones
a = 10

# Se inicializa una bandera de validación de datos con valor falso
dato_valido = False
# Se repite el bucle de ingreso de datos mientras la bandera tenga valor falso
while not dato_valido:
    string_ingresado = input(f'Introduce un número: ').strip()   
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
    b = int(string_ingresado)
    dato_valido = True

result = a / b
print(f'Resultado: {result}')