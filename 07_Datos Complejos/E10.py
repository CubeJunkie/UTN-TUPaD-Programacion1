# Se declara un diccionario con países y capitales según la consigna
original = {
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago'
}

# Se declara un nuevo diccionario donde las claves y valores estarán invertidos
invertido = {}

# Se utiliza un lazo for para recorrer los pares del diccionario
for pais, capital in original.items():
    invertido[capital] = pais

# Se muestran ambos diccionarios por pantalla
print(original)
print(invertido)