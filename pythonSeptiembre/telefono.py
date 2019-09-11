print('CONVERSOR NUMERO DE TELEFONO')
print('ESPAÑA +34')
print('ESPAÑA +33')
print('ESPAÑA +351')
print('ESPAÑA +31')


telefono = input('Ponga su numero de telefono: ')
pais = input('''
    [esp]España
    [fr]Francia
    [pt]portugal
    [nl]Holanda
 ''')
prefijo = {
    'esp' : 34,
    'fr' : 33,
    'pt' : 351,
    'nl' : 31,
    'ESP' : 34,
    'FR' : 33,
    'PT' : 351,
    'NL' : 31
}


#convertir el texto a cadena
numero = [i for i in telefono]

''' numero = []
for i in telefono:
    numero.append(i)
'''
#inserar caracteres para cambiar el formato numero
numero.insert(0, f'(+{prefijo[pais]})')
numero.insert(4,'-')
numero.insert(8,'-')

#camciar a formato cadena
numero_cadena = ''.join(numero)
#cambiar caracter- por espacios
numero_blanco = numero_cadena.replace('-','')
#Mostrar los dos formatos de telefono
print(numero_cadena)
print(numero_blanco)