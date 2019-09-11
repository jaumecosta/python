#COMPARACION NUMEROS mayor y menor

def menorque():
    a = int(input('a ->'))
    b = int(input('b ->'))
    c = int(input('c ->'))
    triple = [a,b,c]
    triple.sort(reverse=True)
    print(f'Numero mas alto: {triple[0]}')
    triple.reverse()
    print(f'Numero mas bajo: {triple[0]}')
    print(f'El numero equilibrado es: {triple[1]}')
    thisset =  a == b == c
    print(f'son iguales{thisset}')
    #total = thisset.pop()
    #print(f'Losnumeros son iguales{total}')
menorque()


