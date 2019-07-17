#COMPARACION NUMEROS mayor y menor

def menorque():
    a = float(input('a ->'))
    b = float(input('b ->'))
    c = float(input('c ->'))

    triple = [a,b,c]
    triple.sort(reverse=True)

    print(f'Numero mas alto: {triple[0]}')
    triple.reverse()
    print(f'Numero mas bajo: {triple[0]}')
    print(f'El numero equilibrado es: {triple[1]}')


menorque()

def tripleAnalisis():
    conjuntoA = {float(input('a ->'))}
    conjuntoB = {float(input('b ->'))}
    conjuntoC = {float(input('c ->'))}

    total = conjuntoA | conjuntoB | conjuntoC


tripleAnalisis()