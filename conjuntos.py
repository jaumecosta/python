'''
CONJUNTOS

En los conjuntos no se pueden repetir los datos, porque no se almacena.
No se puede meter dentro de conjuntos, ni listas, ni tuplas, no otros conjuntos.

Los conjuntos son grupos de datos deshordenados.

'''
#Solo cuando creemos conjuntos vacios
conjunto01 = set()
conjunto01 = {}

#Crear un conjunto
conjunto01 = {1,2,3,4,5,'HOLA',7.9}

#Agregar nuevos elementos. Que se van a insertar en lugares aleatorios(pero no random
# )
conjunto01.add(5.3)
print(conjunto01, '\n')

#Eliminar un valor
conjunto01.discard('HOLA')
print(conjunto01, '\n')

#Buscar Elementos dentro de un conjunto 
print(2 in conjunto01)
print('La Tierra' not in conjunto01, '\n')

# Comprobar si ambos conjuntos son iguales
conjunto01 = {1,2,3}
conjunto02 = {3,1,2,'Hola'}

print(conjunto01 == conjunto02)

#Borrar todo el contenido
#conjunto01.clear()

#Union de dos conjuntos
union = conjunto01 | conjunto02

print(union, '\n')

#Interseccion de dos conjuntos. Los elementos  que se repiten
interseccion = conjunto01 & conjunto02
print(interseccion)

#La diferencia. Elementos que estan solos en el conjunto A
diferencia = conjunto01 - conjunto02
print(diferencia, '\n')

#Diferencia Simetrica. Elementos que estan en A y B, pero en ambos.
simetrica = conjunto01 ^ conjunto02
print(simetrica, '\n')

#saber si es un subconjunto
#Conjunto01 = {1,2,3}
conjunto03 = {1,2,3,4, 'Palma'}
print(conjunto01.issubset(conjunto03))

#saber si un conjunto es un superconjunto
#conjunto01 = {1,2,3,4,5}

conjunto03 = {1,2,3,4,5}

print(conjunto01.issuperset(conjunto03))

#Saber si son disconexos. No tienen  que compartir ningun elemento 
conjunto03 = {1,2,3,4,5}

print(conjunto01.isdisjoint(conjunto03))

#Conjunto sea inmutable
conjunto04 = {3,6,8,100}
conjunto04 = frozenset({3,6,8,100})

##*******************************
