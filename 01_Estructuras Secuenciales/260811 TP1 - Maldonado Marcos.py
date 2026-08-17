# Actividad 1 - Imprimir "Hola Mundo!"
print("\nACTIVIDAD 1")
# Se utiliza la función print para mostrar el mensaje en pantalla
print("Hola Mundo!")

# Actividad 2 - Saludar al usuario por su nombre
print("\nACTIVIDAD 2")
# Se utiliza la función input para que el usuario ingrese su nombre
nombre = input("Escribe tu nombre: ")
# Se utiliza la función print con fstring para mostrar la respuesta con el nombre en pantalla
print(f"Hola {nombre}!")

# Actividad 3 - Oración con datos del usuario
print("\nACTIVIDAD 3")
# Se utiliza la función input para que el usuario cargue sus datos
nombre = input("Escribe tu primer nombre: ")
apellido = input("Escribe tu apellido: ")
edad = input("Escribe tu edad: ")
lugar = input("Escribe tu lugar de residencia: ")
# Se utiliza la función print con fstring para mostrar el mensaje con los datos en pantalla
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# Actividad 4 - Calcular área y perímetro de un círculo de radio X
print("\nACTIVIDAD 4")
# Se declara la variable pi
pi = 3.14159
# Se pide al usuario el radio del círculo y se convierte ese valor en float
radio = float(input("Ingresa el radio del círculo: "))
# Se calcula el área y el perímetro del círculo
area = pi * radio ** 2
perimetro = 2 * pi * radio
# Se utiliza la función print con fstring para mostrar el área y el perímetro del círculo
print(f"Área: {area}; Perímetro: {perimetro}")

# Actividad 5 - Calcular el equivalente en horas de X segundos
print("\nACTIVIDAD 5")
# Se pide al usuario la cantidad de segundos y se convierte ese valor en int
seg = int(input("Ingrese una cantidad de segundos: "))
# Se calcula la cantidad de horas equivalente
horas = seg / 60 / 60
# Se utiliza la función print con fstring para mostrar el equivalente en horas
print(f"Eso equivale a {horas} horas.") 

# Actividad 6 - Mostrar la tabla de multiplcar de un número X
print("\nACTIVIDAD 6")
# Se pide al usuario un número entero y se convierte el string en int
x = int(input("Ingrese un número entero: "))
# Se muestra en pantalla la tabla de multiplicar del número ingresado
print(f"{x} × 1 = {x * 1}")
print(f"{x} × 2 = {x * 2}")
print(f"{x} × 3 = {x * 3}")
print(f"{x} × 4 = {x * 4}")
print(f"{x} × 5 = {x * 5}")
print(f"{x} × 6 = {x * 6}")
print(f"{x} × 7 = {x * 7}")
print(f"{x} × 8 = {x * 8}")
print(f"{x} × 9 = {x * 9}")
print(f"{x} × 10 = {x * 10}")

# Actividad 7 - Suma, división, multiplicación y resta de dos números enteros
print("\nACTIVIDAD 7")
# Se pide al usuario que ingrese dos números enteros distintos de cero
x = int(input("Ingrese un primer número distinto de 0: "))
y = int(input("Ingrese un segundo número distinto de 0: "))
# Se muestra en pantalla la suma de los números
print(f"{x} + {y} = {x + y}")
# Se muestra en pantalla la multiplicación de los números
print(f"{x} × {y} = {x * y}")
# Se muestra en pantalla la división de los números
print(f"{x} ÷ {y} = {x / y}")
# Se muestra en pantalla la resta de los números
print(f"{x} − {y} = {x - y}")

# Actividad 8 - Cálculo de índice de masa corporal (IMC)
print("\nACTIVIDAD 8")
# Se pide al usuario su altura en cm y se la convierte a metros en float
altura = float(input("Ingrese su altura en cm: ")) / 100
# Se pide al usuario que ingrese su peso en kg y se convierte ese valor en float
peso = float(input("Ingrese su peso en kg: "))
# Se calcula el IMC
imc = peso / altura ** 2
# Se muestra en pantalla el IMC
print(f"Su índice de masa corporal es {imc}")

# Actividad 9 - Convertir grados Celsius a Fahrenheit
print("\nACTIVIDAD 9")
# Se pide al usuario una temperatura en Celsius y se convierte en float
c = float(input("Ingrese una temperatura en Celsius: "))
# Se calcula la temperatura equivalente en Fahrenheit
f = c * (9 / 5) + 32
# Se muestra en pantalla la temperatura equivalente en Fahrenheit
print(f"Equivalente en Fahrenheit: {f}")

# Actividad 10 - Promedio de 3 números
print("\nACTIVIDAD 10")
# Se le pide al usuario 3 números y se los convierte en float
x = float(input("Ingrese un primer número: "))
y = float(input("Ingrese un segundo número: "))
z = float(input("Ingrese un tercer número: "))
# Se calcula el promedio de los 3  números
promedio = (x + y + z) / 3
# Se muestra en pantalla el promedio de los 3 números
print(f"El promedio de los tres números es: {promedio}\n")