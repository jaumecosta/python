#Calculadora

numero1 = float(input("Introduce un numero: "))
numero2 = float(input("Introduce otro numero: "))
calcular = str(input('Elige el tipo de Operador (S/M/D/R): ')).upper()

if calcular == "S":
    suma = numero1 + numero2
    print(f'La respuesta es {suma}')
elif calcular == "M":
    multiplicar = numero1 * numero2
    print(f'La respuesta es {multiplicar}')
elif calcular == "D":
    dividir = numero1 / numero2
    print(f'La respuesta es {dividir}')
elif calcular == "R":
    resta = numero1 - numero2
    print(f'La respuesta es {resta}')
else:
    print('ERROR PEPONA')