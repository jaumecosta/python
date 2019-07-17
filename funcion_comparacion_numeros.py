#COMPARACION NUMEROS mayor y menor
numero1 = float(input('Intro un numero '))
numero2 = float(input('Introduce un segundo numero '))
numero3 = float(input('Introduce un tercer numero '))
#Numero 1 es mas mayor con numeros diferentes
if numero1 > numero2 and numero1 > numero3:
    print(f'{numero1} Es mas mayor')
#todos los numeros son iguales
elif numero1 == numero2 and numero1 == numero3 and numero2 == numero3:
    print("Son iguales")
#numero 1 es mayor que 2 pero los demas numeros son iguales
elif numero1 < numero2 and numero1 == numero3 and numero2 == numero3:
    print(f'{numero1:.2f} Es mas mayor')
#numero 1 es mayor que 3 pero los demas son iguales
elif numero1 == numero2 and numero1 < numero3 and numero2 == numero3:
    print(f'{numero1:.2f} Es mas mayor')
#numero 2 es mayor que 3 y el resto son iguales
elif numero1 == numero2 and numero1 == numero3 and numero2 < numero3:
    print(f'{numero2:.2f} Es mas mayor')
#numero 2 es mayor que 1 pero los demas son iguales
elif numero1 > numero2 and numero1 == numero3 and numero2 == numero3:
    print(f'{numero2:.2f} Es mas mayor')
#numero 2 es mayor que 1 y 3
elif numero2 > numero1 and numero2 > numero3:
    print(f'{numero2:.2f} Es mas mayor')
#numero 3 es mayor que 1 y 2
elif numero3 > numero1 and numero3 > numero2:
    print(f'{numero3:.2f} Es mas mayor')
#numero 3 inferior a 1 y 2 iguales
elif numero3 < numero1 and numero3 < numero2 and numero1 == numero2:
    print(f'{numero3:.2f} Es el mas pequeño')
#numero 1 inferior a 2 y 3 iguales
elif numero1 < numero2 and numero1 < numero3 and numero2 == numero3:
    print(f'{numero1:.2f} Es el mas pequeño')
elif numero2 < numero1 and numero2 < numero3 and numero1 == numero3:
    print(f'{numero2:.2f} Es el mas pequeño')
else:
    print('ERROR EPICO')