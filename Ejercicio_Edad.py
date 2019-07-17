#personas con mas edad
#personas con mas edad
persona1 = str(input("Introduzca tu nombre Persona 1 "))
edad1 = int(input(f'¿Cual es tu edad {persona1}?:'))

persona2 = str(input("Introduzca tu nombre Persona 2 "))
edad2 = int(input(f'¿Cual es tu edad {persona2}?:'))

persona3 = str(input("Introduzca tu nombre Persona 3 "))
edad3 = int(input(f'¿Cual es tu edad {persona3}?:'))

#buscar cual tiene mas edad
if edad1 > edad2 and edad1 > edad3:
    compo1 = edad1 - edad2
    compo2 = edad1 - edad3
    print(f'{persona1} es la mas mayor y supera a {persona2} por {compo1} edad y supera a {persona3} por {compo2}')

if edad2 > edad1 and edad2 > edad3:
    compo1 = edad2 - edad1
    compo2 = edad2 - edad3
    print(f'{persona2} es la mas mayor y supera a {persona1} por {compo1} edad y supera a {persona3} por {compo2}')

if edad3 > edad1 and edad3 > edad2:
    compo1 = edad3 - edad1
    compo2 = edad3 - edad2
    print(f'{persona3} es la mas mayor y supera a {persona1} por {compo1} edad y supera a {persona2} por {compo2}')
else:
    print('Eres una pepona')
