
agenda01 = {
    'Pepe':[33, 1.72],
    'Maria':[24,1.80],
    'Juan':[44, 1.64],
    'Eva':[4, 1.00]
}

print(agenda01['Maria'])

agenda02 = {
    'Pepe':{'edad':33, 'altura':1.72},
    'Maria':{'edad':45, 'altura':1.42},
    'Juan':{'edad':12, 'altura':1.92},
    'Eva':{'edad':13, 'altura':1.50}
}

print(agenda02['Maria'])

#******************************
equipoNBA = {
    23:'Michael Jordan',
    00:'Robert Parish',
    21:'Dominique Wilkins',
    33:'Larry Bird',
    10:'Dennis Rodman',
    34:'Shaquile Oneal',
    24:'Moses Malone'
}

#Sacar el valor, sabiendo que existe la llave
print(equipoNBA[00])

#Sino sabes que la llave puede existir, aqui nos ayuda la funcion get()
print(equipoNBA.get(23,'No existe'))

#Busqueda directa
print(33 in equipoNBA)

#Enseñar solo las key's
print(equipoNBA.keys())

#Enseñar solo los valores
print(equipoNBA.values())

# Enseñar llave-valor
print(equipoNBA.items())

#Borrar todo el contenido del diccionario
equipoNBA.clear()