# ACTIVIDAD 1
print("\nACTIVIDAD 1")
# Se le solicita al usuario su edad y se convierte ese valor en entero
edad = int(input("Ingrese su edad: "))
# Si la edad es mayor o igual a 18, se indica que el es usuario es mayor de edad
if (edad >= 18):
    print("Es mayor de edad")
# En caso contrario, no se hace nada (este bloque puede omitirse)
else:
    pass


# ACTIVIDAD 2
print("\nACTIVIDAD 2")
# Se le solicita al usuario su nota y se convierte el valor a float
nota = float(input("Ingrese su nota: "))
# Si la nota es mayor o igual que 6, se indica que está aprobado
if (nota >= 6):
    print("Aprobado")
# En caso contrario, se indica que está desaprobado
else:
    print("Desaprobado")


# ACTIVIDAD 3
print("\nACTIVIDAD 3")
# Se le pide al usuario que ingrese un número par y se lo convierte en entero
numero = int(input("Ingrese un número par: "))
# Si el número es par, se confirma esto por pantalla
if (numero % 2 == 0):
    print("Ha ingresado un número par")
# En caso contrario, se indica que se debe ingresar un número par
else:
    print("Por favor, ingrese un número par")


# ACTIVIDAD 4
print("\nACTIVIDAD 4")
# Se le solicita al usuario que ingrese su edad y se convierte ese número en entero:
edad = int(input("Ingrese su edad: "))
# Si la edad es menor a 12, se indica "Niño/a"
if (edad < 12):
    print("Niño/a.")
# Si la edad es mayor o igual que 12 y menor que 18, se indica "Adolescente"
elif (edad >= 12 and edad < 18):
    print("Adolescente")
# Si la edad es mayor o igual que 18 y menor que 30, se indica "Adulto/a joven"
elif (edad >= 18 and edad < 30):
    print("Adulto/a joven")
# Si la edad es mayor o igual que 30 años, se indica "Adulto/a"
elif (edad >= 30):
    print("Adulto/a")


# ACTIVIDAD 5
print("\nACTIVIDAD 5")
# Se le solicita al usuario que ingrese una contraseña de entre 8 y 14 caracteres
contrasena = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
# Se obtiene la longitud de la contraseña y se la almacena en la variable "longitud"
longitud = len(contrasena)
# Si la longitud es mayor o igual que 8 y menor o igual que 14 se la considera correcta
if (longitud >= 8 and longitud <= 14):
    print("Ha ingresado una contraseña correcta")
# De lo contrario, se indica que debe tener esas características
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# ACTIVIDAD 6
print("\nACTIVIDAD 6")
# Se le solicita al usuario ingresar su consumo mensual de energía eléctrica
consumo = float(input("Ingrese su consumo mensual de energía eléctrica en kWh: "))
# Si el consumo es menor que 150 kWh, se indica "Consumo bajo"
if (consumo < 150):
    print("Consumo bajo")
# Si el consumo es de 150-300 kWh, se indica "Consumo medio"
elif (consumo >= 150 and consumo <= 300):
    print("Consumo medio")
# Si el consumo supera los 300 kWh, se indica "Consumo alto"
elif (consumo > 300):
    print("Consumo alto")
# Adicionalmente, si el consumo supera los 500 kWh, se recomienda considerar medidas de ahorro energético
if (consumo > 500):
    print("Considere medidas de ahorro energético")


# ACTIVIDAD 7
print("\nACTIVIDAD 7")
# Se le solicita al usuario ingresar una palabra o frase
string_usuario = input("Ingrese una palabra o frase: ")
# Si el último caracter es una vocal, se añade un signo de exclamación al string ingresado
if (string_usuario[-1] in "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"):
    string_usuario = string_usuario + "!"
# En caso contrario, no se añade nada (este bloque puede omitirse)
else:
    pass
# En cualquier caso, se muestra el string en pantalla
print(string_usuario)


# ACTIVIDAD 8
print("\nACTIVIDAD 8")
# Se le solicita al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")
# Se le solicita al usuario que seleccione entre las opciones 1, 2 y 3
opcion = int(input("Seleccione una opción [1=MAYUS 2=minus 3=Mayus_Inic]: "))
# Se utiliza una estructura match-case para realizar acciones en función de la opción seleccionada
match opcion:
    # Si la opción es 1, se muestra el nómbre en mayúsculas
    case 1:
        print(nombre.upper())
    # Si la opción es 2, se muestra el nómbre en minúsculas
    case 2:
        print(nombre.lower())
    # Si la opción es 3, se muestra el nómbre con mayúsculas iniciales
    case 3:
        print(nombre.title())
    # Si se ingresó una opción diferente de 1, 2 o 3, se muestra un mensaje de error
    case _:
        print("No seleccionó una opción válida.")


# ACTIVIDAD 9
print("\nACTIVIDAD 9")
# Se le solicita al usuario que ingrese la magnitud de un terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))
# Se muestra en pantalla la categoría correspondiente a esa magnitud
if (magnitud < 3):
    print("\"Muy leve\" (imperceptible).")
elif (magnitud >= 3 and magnitud < 4):
    print("\"Leve\" (ligeramente perceptible).")
elif (magnitud >= 4 and magnitud < 5):
    print("\"Moderado\" (sentido por personas, pero generalmente no causa daños)")
elif (magnitud >= 5 and magnitud < 6):
    print("\"Fuerte\" (puede causar daños en estructuras débiles)")
elif (magnitud >= 6 and magnitud < 7):
    print("\"Muy Fuerte\" (puede causar daños significativos)")
elif (magnitud >= 7):
    print("\"Extremo\" (puede causar graves daños a gran escala)")


# ACTIVIDAD 10
print("\nACTIVIDAD 10")
# Se le solicita al usuario que indique en qué hemisferio se encuentra
hemisferio = input("Hemisferio (N/S): ")
# Se le solicita al usuario que indique en qué mes se encuentra
mes = int(input("Mes del año (1-12): "))
# Se le solicita al usuario que indique en qué día del mes se encuentra
dia = int(input("Día del mes (1-31): "))
# Se convierte el mes en string controlando que tenga 2 caracteres.
if (mes < 10):
    mes = "0" + str(mes)
else:
    mes = str(mes)
# Se convierte el mes en string controlando que tenga 2 caracteres.
if (dia < 10):
    dia = "0" + str(dia)
else:
    dia = str(dia)
# Se genera una fecha compuesta para poder hacer comparaciones
fecha = mes + dia
# Se considera el caso del hemisferio norte
if (hemisferio.lower() == "n"):
# Se asigna la estación en función de la fecha
    if (fecha >= "1221" or fecha <= "0320"):
        estacion = "Invierno"
    elif (fecha >= "0321" and fecha <= "0620"):
        estacion = "Primavera"
    elif (fecha >= "0621" and fecha <= "0920"):
        estacion = "Verano"
    elif (fecha >= "0921" and fecha <= "1220"):
        estacion = "Otoño"
# Se considera el caso del hemisferio sur
elif (hemisferio.lower() == "s"):
# Se asigna la estación en función de la fecha
    if (fecha >= "1221" or fecha <= "0320"):
        estacion = "Verano"
    elif (fecha >= "0321" and fecha <= "0620"):
        estacion = "Otoño"
    elif (fecha >= "0621" and fecha <= "0920"):
        estacion = "Invierno"
    elif (fecha >= "0921" and fecha <= "1220"):
        estacion = "Primavera"
# Se muestra en pantalla la estación del año
print(f"Estación: {estacion}")
print("\n")