import os
import documentacion.razas as razas  #Conecta el archivo que esta en la carpeta documentacion raza y el archivo razas

bucle = True


def pregunta(pregunta):
    if pregunta.upper() == 'E':
        print(razas.España)
        yield razas.España
    if pregunta.upper() == 'U':
        print(razas.Usa)
        yield razas.Usa
    if pregunta.upper() == 'F':
        print(razas.Francia)
        yield razas.Francia
    if pregunta.upper() == 'A':
        print(razas.Alemania)
        yield razas.Alemania


# pregunta
os.system('clear')
pais = input("Introduce el pais que quiere visitar:")
pregunta(pais)



# funciones
'''
bucle = True

def pais_raza(tecla):
    if tecla.upper() == 'E':
        print(razas.p_espanya)
    if tecla.upper() == 'I':
        print(razas.p_italia)
    if tecla.upper() == 'F':
        print(razas.p_francia)

#inicio
os.system('clear')
tecla = input("""De que pais quieres informacions:
    [E]spaña
    [I]talia
    [F]rancia
""")
pais_raza(tecla)
'''


'''



razasDePerros = {
        'España':['Galgo Español','Pator Catalan','Dogo Mallorquin'],
        'Estados unidos':['Demogorgon','Perro Esquimal','Cocker'],
        'Francia':['Briard','Bully','Pudelpointer'],
        'Alemania':['Teckel','Pastor Aleman','Gran Danes']
    }

contador = 0
while contador<10:
        pais = str(input("Introduce el pais que quiere visitar:"))
        print(pais)
        print(razasDePerros[pais])
        '''
