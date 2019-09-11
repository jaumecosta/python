
mallorca = {
    'llucmajor': 35.057,
    'palma': 402.949,
    'inca': 30.944,
    'manacor': 40.279,
    'soller': 13.791

}

vocales = {
    'à' : 'a',
    'í' : 'i',
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
                print('Nombre de población con acentos')
def limpiar(pregunta):
        try:
            pregunta.encode('ascii')
        except UnicodeEncodeError:
            print('Nombre de población con acentos')

if __name__ == "__main__":
  inicio()

