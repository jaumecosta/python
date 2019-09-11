"""
    COMPENSIONS
    son constructos que nos permiten generar a partir de otra secuencia
"""
#usuario inserta casa => string('casa')
cadena = input('escribe algo:')

# lista ['c','a','s','a']
comprehensions = [i for i in cadena if i !='z']
