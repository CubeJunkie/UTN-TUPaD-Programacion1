# Se importa el módulo creado para el ingreso de datos validados
import datos.ingreso_datos as ing

# Se le solicita al usuario una frase:
string_frase = ing.string_no_vacio('Frase')

# Se utiliza el método split para convertir el string en lista de palabras
lista_palabras = string_frase.split()

# Se utiliza la función set() para convertir la lista en un conjunto
palabras_unicas = set(lista_palabras)

# Se declara un diccionario para almacenar los datos de conteo de palabras
recuento = {}

# Se recorre el conjunto de palabras únicas con un lazo for
for palabra_unica in palabras_unicas:
    # Se cuentan las apariciones de la palabra única en la lista utilizando el método .count() 
    apariciones = lista_palabras.count(palabra_unica)
    # Se agrega un par palabra-apariciones al diccionario de recuento
    recuento[palabra_unica] = apariciones

# Se muestra por pantalla el conjunto de palabras únicas y el diccionario con el recuento de apariciones de palabras únicas
print(f'Palabras únicas: {palabras_unicas}')
print(f'Recuento: {recuento}')