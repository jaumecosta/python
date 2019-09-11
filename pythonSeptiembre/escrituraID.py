'''
    Guarda la informacion en disco en python
    -------------------p---------------------
    w (escribir)
    r (leer)
    a (escribir al final)
    r+ (lee y escribe)
'''
nombre = input('Nombre: ')

#ESCRITURA
with open('file.txt', 'w') as f:
    for i in range(5):
        f.write(f'{nombre}\n')
    f.close()

#f = open ('file.txt', 'w')
#f.write(f'{nombre}\n')
#f.close()

#Lectura

#with open('file.txt', 'r') as f:
#    for linea in f:
#        print(linea)