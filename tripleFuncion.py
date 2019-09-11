#triple funcion
import numerosPrimos
import calculadoraDeDivisas
import palindromo

print('PON NUMERO 1 PARA HACER LOS NUMEROS PRIMOS')
print('PON NUMERO 2 PARA HACER LOS NUMEROS PRIMOS')
print('PON NUMERO 3 PARA HACER LOS NUMEROS PRIMOS')


eleccion = int(input('ESCOJE LA OPCION QUE DESEAS APLICAR:'))

if eleccion == 1:
    numerosPrimos.inicio()
elif eleccion == 2:
    calculadoraDeDivisas.inicio()
elif eleccion == 3:
    palindromo.inicio()
else:
    print('OPCION NO VALIDA')

#inicio de la calculadra

if __name__ == "__main__":
        numerosPrimos.inicio()
        calculadoraDeDivisas.inicio()
        palindromo.inicio()

