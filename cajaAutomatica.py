#Ingresar, retirar, mostrar y salir

#dinero en el cajero
saldo = 4000

#Interface
print('\t--MENU--')
print('1. Ingresar dinero en la cuenta')
print('2. Retirar dinero en la cuenta')
print('3. mostrar dinero que hay en la cuenta')
print('4. Salir')

print('')

opcion = int(input('Elige una opcion del menu:  '))
#opcion
if opcion == 1:
    extra = float(input('cuanto dinero quiere ingresar'))
    saldo += extra
    print(f'Dinero en la cuenta: {saldo:.2f}€')
elif opcion == 2:
    retirar = float(input('cuanto dinero quiere retirar:'))
    if retirar > saldo:
        print('No tiene suficiente dinero en la cuenta')
    else:
        saldo -= retirar
        print(f'Dinero en la cuenta: {saldo:.2f}€')
elif opcion == 3:
    print(f'Dinero en la cuenta: {saldo:.2f}€')
elif opcion == 4:
    print('Gracias por dejar que te saquemos la pasta')
else:
    print('Error, se equivoco de opcion en el menu')
    
'''
operacion = str(input("¿Que quieres Ingresar (Ponga I), Retirar dinero(Ponga R) Mostrar lo que te queda(Ponga M)?"))



if operacion == "I":
    ingresar = int(input("¿Cuanta pasta quiereas ingresar?"))
    suma = (ingresar + saldo)
    print(f'Su saldo actual es{suma}€')
elif operacion == "R":
    retirar = int(input("¿Cuanta pasta queires retirar?"))
    resta = (saldo - retirar)
    print(f'Su saldo es{resta}€')
    '''