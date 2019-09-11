>>> cadena = 'hola mundo'
>>> print (cadena.capitalize())
Hola mundo
>>> print (cadena.lower())
hola mundo
>>> print (cadena.upper())
HOLA MUNDO
>>> print (cadena.swapcase())
HOLA MUNDO
>>> cadena = 'hola mundo'
>>> print (cadena.swapcase())
HOLA MUNDO
>>> print (cadena.title())
Hola Mundo
>>> cadena = 'hola mundo' .capitalize()
>>> print(cadena.center(50,'*'))
********************Hola mundo********************
>>> print(cadena.ljust(50,'*'))
Hola mundo****************************************
>>> print(cadena.rjust(50,'*'))
****************************************Hola mundo

>>>
>>> numeroDeFactura = 2345
>>> print(str(numeroDeFactura).zfill(10))
0000002345
>>> print(str(numeroDeFactura).zfill(30))
000000000000000000000000002345
>>> print(cadena)
Hola mundo
>>> print(cadena.count('o'))
2
>>> print(cadena.count('m'))
1
>>> print(cadena.count('mundo'))
1
>>> texto = 'Despertar por la mañana!!!' .capitalize()
>>> print(texto.find('mañana'))
17
>>> #SLICES
...
 texto = 'Hola'
texto[1:]
'ola'
texto[1:3]
'ol'
texto[1:4:2]
'oa'
#INVERTIR
texto[::-1]
'aloH'

#invertir en java
 new StringBuilder(my_string).reverse().toString()
#CONTINUE el bucle sigue
#break no haria nada