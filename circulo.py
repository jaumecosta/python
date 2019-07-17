#Longitud area
#2 * pi * r**
#Longitud y area de un circulo 
#area = pi * r**2
#longitud = 2 * pi * r

#libreria pi

import math

radio = float(input('radio ->'))
area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f'\tSi el radio es: {radio:.2f}\n', 
        f'el area tiene que ser {area:.2f}\n'
        f'y la longitud es {longitud:.2f}')