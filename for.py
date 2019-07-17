'''
FOR 
Es el bucle que se utiliza en las colecciones
'''
coleccion01 = (1,2,3,4,5,6)

for i in coleccion01:
    print(f'Elemento: {i}')

#*******

coleccion02 = {
    'Pepe': 34,
    'Maria': 67,
    'Joselito': 44

}

# saca la llave -> valor
for i in coleccion02:
    print(f'{i} -> {coleccion02[i]}')

#otro metodo
for llave, valor in coleccion02.items():
    print(f'{llave} -> {valor}')

#Bucle con cada caracter de un string
coleccion03 = 'Hola Mundo'

for i in coleccion03:
    print(f'{i}', end='-')