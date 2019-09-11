#variables

a = 5
#variable locales se pueden convertir en globales cuando la manera es complivsda
#funciones
def f1(b):
    global sumar
    #Variables locales a y b
    sumar = a + b
   return sumar, a

print(sumar)