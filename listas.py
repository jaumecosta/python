'''
LISTAS
Parecidas a los arreglos
'''

grupo = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 20, True, 0.42] 

#Multiplicar elementos de una lista
#grupo = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 20, True, 0.42] * 4

#Imprimir elementos de una lista
print(grupo[2:5],'\n')

#agregar elementos al final de la lista
grupo.append('FINAL')
print(grupo,'\n')

#Agregar elementos entre la lista
grupo.insert(2, 'CENTRO')
print(grupo,'\n')

#Varios Elementos en una lista al final
grupo.extend([20,'Hola','patata',100])
print(grupo,'\n')

#Podemos concatenar listas 
otroGrupo = ['La Tierra', 'La Luna', 'Jupiter']

grupoFinal = grupo + otroGrupo
print(grupoFinal,'\n')

#saber si un valor esta dentro de una lista
print('La Tierra' in grupoFinal)

# Saber en que indice esta el elemento
print(grupoFinal.index('CENTRO'))

#Contar cuantas veces se repite un elemento
print(grupoFinal.count('Lunes'))

#Eliminar el ultimo elemento de la lista 
grupoFinal.pop()
print(grupoFinal, '\n')

#Eliminar el elemento index de la lista 
grupoFinal.pop(5)
print(grupoFinal, '\n')
   
#Eliminar el elemento exacto de una lista
grupoFinal.remove('La Luna')
print(grupoFinal, '\n')

#Voltear Lista
grupoFinal.reverse()

# 0rdenar una lista
#grupoFinal.sort()
grupoFinal.sort(reverse=True)

#Borrar todo el contenido de la lista
grupoFinal.clear()

# Cambiar un elemento de la lista
grupoFinal[5] = 'Cosa'
