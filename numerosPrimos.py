'''
NUMEROS PRIMOS
    Divisibles por 1 por ellos mismos.
    Tabla de NP empieza con 2 
    El usuario nos inserta un numero y le decimos si es primo o no
'''

#funciones
def si_es_primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero > 2 and numero % 2 == 0:
        return False
    else:
        for i in range(3, numero):
            if numero % i == 0:
                return False

    return True






def inicio():
    print('D E S C U B R E  S I  T U  N U M E R O  E S  P R I M O')
    print('------------------------------------------------------')
    print('')
    numero = int(input('Introduce un numero entero:'))

    resultado = si_es_primo(numero)

    if resultado is True:
        print('Tu numero es Primo')
    else:
        print('Tu numero NO es primo')
  #  dividir = numero % 2
  #  if dividir <= 1:
   #     print("Tu numero es primo")
   # else:
    #    print("Tu numero NO es primo")



#inicio de la calculadra

if __name__ == "__main__":
    for i in range(1, 100):
        inicio()