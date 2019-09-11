#tortuguit

import turtle

lienzo = turtle.Screen()
tortuguita = turtle.Turtle()

coordenadas = int(input('Indique las coordinadas '))
for i in coordenadas:
    print(i)
    tortuguita.forward(i)
    tortuguita.left(i)
    tortuguita.forward(i)
    tortuguita.left(i)
    tortuguita.forward(i)
    tortuguita.left(i)
    tortuguita.forward(i)
    tortuguita.left(i)

#turtle.mainloop()