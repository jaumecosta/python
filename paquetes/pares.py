
def num_pares(cantidad):
    num = 1
    numList = []

    while num < cantidad:
        numList.append(num * 2) #Lista numeros
        
        num += 1

    return numList

print(num_pares(10))
print('*' * 40)




'''
numero = float(input("Introduce un numero"))
residuo = numero%2
while residuo == 0:
    print("Es un numero par")
    

#f3()

'''

def num_pares_generator(cantidad):
    num = 1
    #No es necesario una lista
    while num < cantidad:
        #construye un objeto iterable
        #almacenando los elementos de uno en uno
        yield num * 2   #Cosechar en ingles

        num += 1

    #No hay return

resultado = num_pares_generator(10)

#for i in resultado:
#    print(i)
#next va mostrando datos de uno en uno
print(next(resultado))
print('.' * 20)
print(next(resultado))
print('.' * 20)
print(next(resultado))
print('.' * 20)
print(next(resultado))
print('.' * 20)


