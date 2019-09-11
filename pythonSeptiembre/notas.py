diccionarioAlumno = {
        'Pepe':1,
        'Juan':2,
        'Miguel':3,
        'Toni':4,
        'Esteban':5,
        'Angel':6,
        'Jose':7,
        'Alejandro':8,
        'Jorge':9,
        'Lucas':10,
        'Mateo':11,
        'Bernardo':12,
        'Luis':13,
        'David':14,
        'Damian':15
}

print(diccionarioAlumno.items())


alumno = input('A que alumno le quieres ver las notas')
notaControl1 = float(input('Introduce la nota de control 1:'))
notaControl2 = float(input('Introduce la nota de control 2:'))
notaControl3 = float(input('Introduce la nota de control 3:'))
notaExamenFinal = float(input('Introduce la nota del examen Final:'))

mediaControl = notaControl1 + notaControl2 + notaControl3
totalControl = mediaControl / 10
print(f'La media de los controles es {round(totalControl)}')
notaExamenFinal = notaExamenFinal * 0.7
sumaTotal = notaExamenFinal + totalControl
#print(notaExamenFinal)
if notaExamenFinal <= 4.9:
    print(F'{sumaTotal} es suspendido, vete a la puta calle')
else:
    print(F'{sumaTotal} aprobado')


notas = diccionarioAlumno['Pepe']
controles = 0
for i in range(3):
    controles += notas[i]
controles = (controles/3) * 0.3

final = (notas[3] * 0.7) + controles
