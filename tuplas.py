'''
TUPLAS 
Sirven concretamente para Buscar
Consumen menos memoria de la listas
son mas rapidas
Pero...Despues de crearlas son inmodificables
'''
tupla01 = ('Lunes', 'Martes', 'Miercoles')
print(tupla01, '\n')

#Nos de la longitud de esta tupla
print(len(tupla01), '\n')

#SABER SI UN VALOR ESTA DENTRO DE LA TUPLA
print('Martes' in tupla01)

#Saber en que indice esta un elemento
print(tupla01.index('Miercoles'))

print(tupla01.count('Miercoles'))

#Copiar el contenido de Una tupla a una Lista
nueveLista = list(tupla01)

#Copiar el contenido de una lista a una tupla
nuevaTupla = tuple(grupoFinal)