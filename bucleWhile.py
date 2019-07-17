'''
BUCLE 
WHILE, es mas generico que el FOR
'''
import math

numero = float(input('Escribe un número:'))

#El bucle comprobar con la condicion, si el numero insertado por el usuario es negativo.
#Si es asi, itera el contenido.
#Sino se cumple la condicion, pasa a la siguiente linia.

while numero < 0:
    print('¡Error, debe escribir un numero positivo')
    numero = int(input('Escribe un número:'))
print(f'\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}')

#variable iteradora
i = 1

while i < 5:
    print('Hola Mundo')
    i += 1
print('FINAL')
