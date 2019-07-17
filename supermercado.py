#si la compra es mayor de 50 descuento del 15%
# si es menor o igual a 30, frase para incetivar al descuenteo
#entre 0 o 20 euros, no hay descuento

print("\t --Bienvenido al mercado de armas--\n\n")
producto1 = input('Producto:')
precio = float(input(f'Precio del {producto1}:'))
producto2 = input('Producto:')
precio += float(input(f'Precio del {producto2}:'))
producto3 = input('Producto:')
precio += float(input(f'Precio del {producto3}:'))
print(precio)
#if precio > 50:
#    desc = precio * 0.15 
#    resultado = precio - desc
 #   print(f'El total ha pagar es {resultado} €')
if precio > 20 and precio <= 30:
    print("Tiene usted la posibilidad de optar a un gran descuento,"
    f"pero tiene que insertar el codigo postal de su vivienda")
    elegir = input('Y / N: ').upper()
    if elegir == "Y":
        cp = int(input('Codigo Postal:'))
        descuento = precio * 0.5
        print(f'\t {descuento:.2f}€')
        precio -= descuento
    else:
        print("Usted se lo pierde")
elif precio >= 50:
    descuento = precio * 0.5
    precio += descuento
    print(f'\t {descuento:.2f}€')
else:
    print(f"Te jodes no tienes nada{descuento:.2f}€")

#Precio final
#print(f'\t\nTotal Final de compra sin descuento: {precio:.2f}€')


#impuesto = descuento * 0.21
#desc = descuento + impuesto
#print(f"El total del precio con impuestos es{desc:.2f} €")
iva = precio * 0.21
print(f'\t\nIVA: {iva:.2f}€')
print(f'\t\nTotal Final de compra: {precio:.2f}€')
