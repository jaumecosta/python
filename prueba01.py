
#Variables
# **********************

nombre = 'Jon'
apellidos = 'Nieve'

print('Mi nombre es ' + nombre + 'y mi primer apellido ' + apellidos)

#Calcular el area de un circulo
#********************
pi = 3.14159
radio = 3

area = pi * radio**2

print(area)

#Entrada de datos
#**************************************************
nombre1 = input('¿Cual es tu nombre? ')

print('Hola, ' + nombre1 + '!')


#Prioridadres de Operadores Geneticos
#*******************************************
# 1. ()
# 2. **
# 3. *, /, mod, not
# 4. +, -, and
# 5. >, <, ==, >=, <=, !=, or



# Operadores de Asignacion
#
#a = 0

#a = a**2
#a += 5
#a -= 5
#a *= 5
#a /= 5
#a **= 2
#a %= 2



#Concatenar con string y variables

nombre2 = 'Danerys'
altura = 2.23

#primera opcion
print('Hola me llamo',nombre2,'y mido',altura,'metros de estatura')

# Segunda Opcion Python 2
#print('Hola me llamo {} y mido {} metros de estatura').format(nombre2, altura)

#Tercera Opcion
print(f'Hola me llamo {nombre}'
         f'y mido {altura} metros de estatura')

#Entrada de datos

#inout te guarda datos tipo cadena
edad = int(input('Tu edad: '))
nombre4 = float(input('Tu nombre: '))
altura = float(input('Tu altura:'))

print(f'Hola tu {nombre4} y tu edad es {edad}, como tu altura{altura}')

#FUNCIONES INTEGRADAS

#Convertir un string en entero
n = '10'
n = int('10')
print(n)

#convertir un string a decimal
n = float('10.4')
print(n)

#convertir un numero a string
n = str(10)
print(n)

# convertir un  numero a binario
n = bin(10) 
print(n)

#convertir un numero a hexadecimal
n = hex(10) 
print(n)

#convertir un binario a entero
n = int('0b1010', 2)
print(n)

# convertir un hexadecimal a entero 
n = int('0xa', 16)
print(n)

# convertir un negativo en positivo
n = abs(-12)
print(n)

#convertir de numero decimal a entero
n = round(4.8)
print(n)

# cuenta cantidad de caracteres
n = len('Toni')
print(n)
