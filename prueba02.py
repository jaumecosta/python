# IF, condicional
if 10 > 0:
    print('Esto es un if')
    print('otra linea')
elif 10 == 0:
    print('Esto se parece a else if')
else:
    print('esto es un else')

#IF anidado

edad = int(input('¿Cual es tu edad? '))
if 0 < edad < 120:
    print('La introduccion de datos es correcta')
    if edad >= 18:
        print('Eres mayor de edad')
    if edad < 18:
        print('Eres un pitufino')
else:
    print('Te has equivocado con la introduccion de la edad, Tonto, mas que tonto')