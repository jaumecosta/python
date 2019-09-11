
mallorca = {
    'llucmajor': 35.057,
    'palma': 402.949,
    'inca': 30.944,
    'manacor': 40.279,
    'soller': 13.791

}

vocales = {
    'á' : 'a',
    'à' : 'a',
    'í' : 'i',
    'ì' : 'i',
    'ú' : 'u',
    'ó' : 'o',
    'ò' : 'o',
    'é' : 'e',
    'è' : 'e'

}

def inicio():
    while True:
        pregunta = str(input('Poblacion de Mallorca (\"s\" para salir: )')).lower()
        if pregunta == 's':
            break

#Si sale un error 
        try:
            print(mallorca[pregunta])
        except KeyError:
                print(f'No tenemos los datos de {pregunta.title()}')



def limpiar(pregunta):
        #todo a minusculas
        minusculas = pregunta.lower()
        #si no ay minuscula
        try:
            minusculas.encode('ascii')
        except UnicodeEncodeError:
           # for i in range(len(pregunta) -1): #comprueba la longitud
                for llave, valor in vocales.items(): #sacan las llaves y valores
                    minusculas = minusculas.replace(llave, valor) #

                    #reemplezado = palabra.replace('h', 'hhh') #


        return minusculas

def insertar(mallorca):
    print('P U R I F I C A C I O N  T O T A L')
    print('Si desea purificar pulse Y')
    print('Si no quiere purificar pulse N')
    limpiar = str(input('Escoja la opcio  que desea realizar'))  
    print(limpiar)

if __name__ == "__main__":
    while True:
        inicio()
        

   #     pregunta = str(input("Poblacion de Mallorca: "))

   #     textoLimpio = limpiar(pregunta)


   

 
  