'''
    Python, Decoradores
    Funciones que a su vez añaden funcionalidades a otra funciones
    Decoran a otras funciones
    Decorar es añadir funcionalidades

    Estructura de un decorador:
    3 funciones(A, B y C) donde A recibe como parametro a B para devolver C

    Un decorador se aplica a una funcion o metodo con el simbolo @

    LOS DECORADORES ES CODIGO MUY HABITUAL EN PYTHON Y EN SUS FRAMEWORKS
'''

#Una funcion que recibe a una funcion
def proteger(func):

    #Encapsular dentro de  proteger
    def envolver(password):
        if password == 'muevete':
            return func()
        else:
            print('Contraseña incorrecta')
            
    return envolver

@proteger   # decorador
def proteger_login():
    print('Tu contraseña es correcta')

if __name__ == "__main__":
    password = str(input('Escribe tu contraseña: '))   #pide el password

    proteger_login(password)

    # Pypi (Python package index)
    # Repositorios de terceros
    # instalacion herramienta pip


    #python get-pip.py
    #pip install virtualenv   MAQUINA VIRTUAL
    #virtualenv venz es como el composer de php pero para python
    #pip freeze hacerlo con consola bash  (source activate)   (venv)
    #ayuda a recuperar requeriments

    #estar en entorno correcto
    #lib donde se instalan las librerias
    #y en site-packages
    