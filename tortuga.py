import turtle

#funcion que se encarga de la activacion de la ventaan de dibujo y de llamar a la funcion haz rectangulo

def oceano():
    window = turtle.Screen()
    tortuguita = turtle.Turtle()

    haz_rectangulo(tortuguita)
    turtle.mainloop()

#funcion que nos hace las preguntas  de largo y alto
def haz_rectangulo(tortuguita):
    largo = float(input('Largo: '))
    alto = float(input('Alto: '))

    for i in range(2):
        haz_linea(tortuguita, largo)
        haz_alto(tortuguita, alto)

def haz_linea(tortuguita, largo):
    tortuguita.forward(largo)
    tortuguita.left(90)

def haz_alto(tortuguita, alto):
    tortuguita.forward(alto)
    tortuguita.left(90)
#Para definir donde comenzara nuestro codigo vamos a usar esta linia
if __name__ == '__main__':
    oceano()
