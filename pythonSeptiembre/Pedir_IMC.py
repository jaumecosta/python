
print('CALCULO DE INDICE DE MASA CORPORAL (IMC)')
print('')
peso = float(input("Introduza su peso: "))
altura = float(input("Introduzca su altura en centimetros: "))

alturaCuadrado = altura**2
resultado = peso/alturaCuadrado

if resultado < 18.5:
    print(f'\nSu IMC es de {round(resultado, 1)}, su peso es insuficiente')
elif resultado > 18.5 and resultado < 24.9:
    print(f'Su IMC es de {round(resultado, 1)}, su peso es normal, esta en forma')
elif resultado > 25 and resultado < 26.9:
    print(f'Su IMC es de {round(resultado, 1)}, tiene sobrepeso grado I')
elif resultado > 27 and resultado < 29.9:
    print(f'Su IMC es de {round(resultado, 1)}, tiene sobrepeso grado II')
elif resultado > 30 and resultado < 34.9:
    print(f'Su IMC es de {round(resultado, 1)}, tiene obesidad tipo I')
elif resultado > 35 and resultado < 39.9:
    print(f'Su IMC es de {round(resultado, 1)}, tiene obesidad tipo II')
elif resultado > 40 and resultado < 49.9:
    print(f'Su IMC es de {round(resultado, 1)}, tiene obesidad de tipo III(morbida)')
                  
else:
    print(f'Su IMC es de {round(resultado, 1)}, tiene obesidad extrema')