'''
    AGENDA 2019/2020
    ----------------
    nombre / teléfono / email
'''
#clases
class Ficha:
       
    def __init__ (self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Agenda:
#***************Constructor
    def __init__ (self):
        self._contactos = []
# ************METODOS
#Añadir contacto
    def nuevo(self, name, phone, email):
        contacto = Ficha(name, phone, email)
        self._contactos.append(contacto)

        print('''
        >>>
        \tContacto Añadido Correctamente
        ''')
#MOSTRAR TODOS LOS CONTACTOS
    def mostrar_todo(self):
        for contacto in self._contactos:
            self._mostrar(contacto)
       
        print('''
        >>>
        \tMostrados todos los contactos
        ''')
#Formato de contacto para el metodo mostrar
    def _mostrar(self, contacto):
        print('---*---*---*---*---*---*---*---*---*---*---*---*---*---*')
        print('Nombre: {}'.format(contacto.name)) #te mete dentro de las llaves
        print('Telefono: {}'.format(contacto.phone))
        print('Email: {}'.format(contacto.email))
        print('---*---*---*---*---*---*---*---*---*---*---*---*---*---*')

#borrar contacto
    def borrar(self, name):
        for index, contacto in enumerate(self._contactos):
            if contacto.name.lower() == name.lower():
                del self._contactos[index]
                break

        print('''
        \tContacto Borrado
        ''')

#buscar contacto
    def buscar(self, name):
        for contacto in self._contactos:
            if contacto.name.lower() == name.lower():
                self._mostrar(contacto)
                break
            else: 
                self._no_encontrado()
        
            print('''
            \tBusqueda finalizada con exito
            ''')
 #Actualizar contacto
    def actualizar(self, name, phone, email):
        for contacto in self._contactos:
            if contacto.name.lower() == name.lower():
                contacto.phone = phone
                contacto.email = email
                break
            else:
                self._no_encontrado()     

        print('''
        \tContacto actualizado con exito
        ''')

    def _no_encontrado(self):
        print('*****************')
        print('No encontrado')
        print('********************')

#FUNCIONES
def run():
#Creamos un objeto llamado agenda de Jaume
    agenda_de_Jaume = Agenda()


    # *Menu de la Agenda
    while True:
        menu = input('''
        ¿Qué deseas hacer?
​
        [a]ñadir contacto
        [ac]ualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir
        ''')
        if menu == 'a':
            # Se le piden los datos de contacto
            name = input('Escribe el nombre del contacto:')
            phone = input('Escribe el telefono del contacto:')
            email = input('Escribe el email del contacto:')      
            #Se llama al metodo de añadir contacto
            agenda_de_Jaume.nuevo(name, phone, email)      
        elif menu == 'ac':
            name = input('Escribe el nombre del contacto:')
            phone = input('Escribe el telefono del contacto:')
            email = input('Escribe el email del contacto:') 
            #Se llama al metodo de actualizar contacto
            agenda_de_Jaume.actualizar(name, phone, email)
        elif menu == 'b':
            name = input('Escribe el contacto que quires buscar')
            agenda_de_Jaume.buscar(name)
        elif menu == 'e':
            name = input('Eliminar el contacto')
            agenda_de_Jaume.borrar(name)
        elif menu == 'l':
            agenda_de_Jaume.mostrar_todo()
        elif menu == 's':
            break
        else:
            print('Prueba otra vez!')
# *Inicio
if __name__ == "__main__":
    run()
      