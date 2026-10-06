print('---Precios Frutas---')
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
print(precios_frutas)

# Ejercicio 1 - Añadir frutas al diccionario precio_frutas
print('---E1 - Agregar frutas---')

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


# Ejercicio 2 - Actualizar precios en el diccionario precio_frutas
print('---E2 - Actualizar precios---')

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)

# Ejercicio 3 - Lista de frutas sin precios
print('---E3 - Lista de frutas sin precios---')

lista_precios = list(precios_frutas.keys())

print(lista_precios)