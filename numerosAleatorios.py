#FASE 1:Poner una lista de numeros aleatorios 50
#____________________________
#Ordenar lista
#____________________________
#Aplicar BB binario
#   input(¿?)
#CREAR LISTA AUTOMATICA
#def aletario():



import random

lista_aleatoria = []

def lista():
    while len(lista_aleatoria) < 50:
        aleatorio = random.randint(0,200)
        lista_aleatoria.append(aleatorio)
        if lista_aleatoria.count(aleatorio) > 1:
            lista_aleatoria.pop()   #borra el ultimo dato
    
    lista_aleatoria.sort()

def busquedaBinaria():
       for i in range(0)



if __name__ == "__main__":
    lista()
    busquedaBinaria()
    print(lista_aleatoria)
    print(len(lista_aleatoria))
