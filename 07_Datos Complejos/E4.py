# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

agenda = {}

# Se le pide al usuario ingresar 5 contactos (nombre-número), los cuales se agregan a un diccionario
for i in range(5):
    print(f'---CONTACTO N.º {i + 1}---')
    string_nombre = ing.string_alpha_espacios('Nombre')
    string_numero = ing.string_telefono('Número')
    agenda[string_nombre] = string_numero

# Se muestra la agenda en pantalla
print('------------------------------')
print('AGENDA')
print(agenda)
print('------------------------------')

# Se solicita al usuario un nombre para consultar el número en la agenda
print('Consulte un número ingresando el nombre.')
nombre_consulta = ing.string_alpha_espacios('Nombre')
if agenda.get(nombre_consulta) is None:
    print('Ese nombre no está en la agenda.')
else:
    print(f'Número: {agenda.get(nombre_consulta)}')
print('------------------------------\n')