#CALCULADORA DE DIVISAS
#1 Libras -> 1.11 EUROS
def librasAeuros(montante):
    #divisa de la libra a dia de hoy (22/06/2019)
    libras = 1.11
    #Calculo de libras a euros
    return libras * montante


def inicio():
    #BONITO EN PANTALLA
    print('SUPER CONVERSOR DE DIVIDAS')
    print('')
    print('Convierte tus libras a euros')
    print('----------------------------')
    print('')

    #PREGUNTA
    montante = float(input("Cantida de Libras: "))
    #llamada a la uncion
    resultado = librasAeuros(montante)

    print(f'Tus {montante:.2f} libras, equivale a {resultado:.2f} euro/s')

# inicio de la calculadora
if __name__ == "__main__":
    inicio()